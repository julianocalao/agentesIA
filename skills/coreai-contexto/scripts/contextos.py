#!/usr/bin/env python3
"""ContextOS portable bootstrap and evidence-backed elicitation. No network."""
import argparse, json, re, shutil, sys, hashlib
from pathlib import Path
from datetime import datetime, timezone
try:
    import yaml
except ImportError:
    sys.exit('Install requirements.txt in a virtual environment (PyYAML required).')
BASE = Path(__file__).resolve().parents[1]
EMPTY = {'', 'null', '~', 'fill_this', 'tbd', 'todo', 'incomplete', 'preencher', 'n/a'}
def real(v):
    if v is None: return False
    if isinstance(v, str): return v.strip().lower() not in EMPTY and not re.match(r'^(fill[_ ]?|todo:|tbd:)', v.strip(), re.I)
    if isinstance(v, (list,dict)): return bool(v) and any(real(x) for x in (v.values() if isinstance(v,dict) else v))
    return True

def safe(root, rel=''):
    p=root / rel
    if not p.is_relative_to(root): raise ValueError('Path outside root')
    for x in [p,*p.parents]:
        if x.is_symlink(): raise ValueError('Symlink forbidden: '+str(x))
        if x == root: break
    if not p.resolve().is_relative_to(root.resolve()): raise ValueError('Path escape')
    return p

def write(p, data, exclusive=False):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x' if exclusive else 'w', encoding='utf-8') as f:
        if p.suffix=='.json': json.dump(data,f,ensure_ascii=False,indent=2)
        elif p.suffix=='.yaml': yaml.safe_dump(data,f,allow_unicode=True,sort_keys=False)
        else: f.write(data)

def load(p,default=None):
    if not p.exists(): return default
    return yaml.safe_load(p.read_text(encoding='utf-8'))

def questions(mode):
    data=json.loads((BASE/'data'/f'questions-{mode}.json').read_text(encoding='utf-8'))
    if mode=='quick': return data
    return [dict(q,phase=phase['id']) for phase in data['DEEP_PHASES'] for q in phase['questions']]

def key(q): return q['file']+'::'+q['ypath']

def main(argv=None):
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--root',required=True,type=Path)
    a.add_argument('command',choices=['init','add-business','set-active','status','questions','import-answers','consolidate'])
    a.add_argument('--business'); a.add_argument('--mode',choices=['quick','deep'],default='quick')
    a.add_argument('--answers',type=Path);a.add_argument('--reviewed',action='store_true')
    args=a.parse_args(argv)
    root=args.root.expanduser().absolute();safe(root)
    cfgp=safe(root,'config.json');cfg=load(cfgp)
    # Padrao cerebro do Context OS (negocios/<slug>/cerebro): o scaffold deste script
    # recriaria em businesses/<slug>/ o formato antigo (context/, brand-dna/, evidence/...)
    # e gravaria config.json, que nesse padrao e camada gerada. So status continua.
    if safe(root,'negocios').is_dir() and args.command!='status':
        raise ValueError('Raiz no padrao cerebro (negocios/<slug>/cerebro): use a skill coreai-contextos '
            '(CoreAI:ContextOS:Criar/Perguntar/Status). Para trocar o negocio ativo nesta maquina: '
            'node <raiz>/nucleo/motor/negocio-ativo.mjs trocar <slug>.')
    if args.command=='init':
        for part in ('businesses','data','dashboard','.cache'):safe(root,part).mkdir(parents=True,exist_ok=True)
        if cfg is None:
            cfg=load(BASE/'references/templates/config.yaml');cfg['created_at']=datetime.now(timezone.utc).isoformat();write(cfgp,cfg,True)
        for src in [BASE/'references/templates/user.yaml',*sorted((BASE/'data').glob('*.json'))]:
            dst=safe(root,src.name if src.name=='user.yaml' else 'data/'+src.name)
            if not dst.exists(): dst.write_bytes(src.read_bytes())
        return {'status':'INITIALIZED','root':str(root),'active_business':cfg.get('active_business')}
    if cfg is None: raise ValueError('Run init with explicit --root first')
    if args.command=='status':
        result=[]
        for p in sorted(safe(root,'businesses').iterdir()):
            safe(root,str(p.relative_to(root)))
            if p.is_dir():
                records=load(safe(root,str(p.relative_to(root))+'/evidence/answers.json'),{})
                result.append({'business':p.name,'answers':len(records),'quick_total':len(questions('quick')),'deep_total':len(questions('deep')),'consolidated':safe(root,str(p.relative_to(root))+'/contexto.md').is_file(),'semantic_review':'not_automatically_verified'})
        out={'active_business':cfg.get('active_business'),'businesses':result}
        if safe(root,'negocios').is_dir():out['layout']='cerebro';out['nota']='answers conta o formato antigo; no padrao cerebro use node <raiz>/nucleo/onboarding/entrevistar.mjs todos'
        return out
    slug=args.business
    if not slug or not re.fullmatch(r'[a-z][a-z0-9_-]*',slug): raise ValueError('Explicit valid --business required')
    b=safe(root,'businesses/'+slug)
    def bp(rel):
        if Path(rel).is_absolute() or '..' in Path(rel).parts: raise ValueError('Client path escape')
        return safe(root,'businesses/'+slug+'/'+rel)
    if args.command=='add-business':
        for src in sorted((BASE/'references/templates/business').rglob('*.yaml')):
            dst=bp(str(src.relative_to(BASE/'references/templates/business')))
            if not dst.exists(): dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(src.read_bytes())
        for part in ('products','intelligence/meetings','intelligence/decisions','sources','outputs'):bp(part).mkdir(parents=True,exist_ok=True)
        idx=bp('intelligence/memory-index.yaml')
        if not idx.exists():write(idx,{'meetings':[],'decisions':[],'learnings':[]},True)
        if not any(x['slug']==slug for x in cfg['registered_businesses']):
            cfg['registered_businesses'].append({'slug':slug,'status':'setup'});write(cfgp,cfg)
        return {'status':'SCAFFOLD_ONLY','business':slug,'contexto_created':False}
    if not b.is_dir(): raise ValueError('Unknown business')
    if args.command=='set-active':
        if not any(x['slug']==slug for x in cfg['registered_businesses']):raise ValueError('Unregistered business')
        cfg['active_business']=slug;write(cfgp,cfg);return {'active_business':slug}
    qs=questions(args.mode)
    records=load(bp('evidence/answers.json'),{})
    if args.command=='questions':return {'mode':args.mode,'questions':[dict(q,id=key(q),answered=key(q) in records) for q in qs]}
    if args.command=='import-answers':
        if args.answers is None: raise ValueError('--answers JSON list required')
        items=json.loads(args.answers.read_text(encoding='utf-8'));known={key(q):q for q in questions('quick')+questions('deep')}
        if not isinstance(items,list):raise ValueError('Expected JSON list')
        pending={};newrecords=dict(records)
        for item in items:
            k=item['id'];q=known.get(k)
            if not q:raise ValueError('Unknown question: '+k)
            v=item['value'];source=item['source']
            if not real(v):raise ValueError('Empty/placeholder answer')
            if not isinstance(source,str) or not source.startswith('sources/'):raise ValueError('source must be client-relative sources/file')
            sp=bp(source)
            if not sp.is_file() or not sp.read_text(encoding='utf-8').strip():raise ValueError('Source missing/empty')
            if q.get('type')=='number' and (isinstance(v,bool) or not isinstance(v,(int,float))):raise ValueError('Number required')
            if q.get('type')=='list' and not isinstance(v,list):raise ValueError('List required')
            if k in records and records[k]['value']!=v:raise ValueError('Existing answer conflict; no overwrite')
            path=bp(q['file']);doc=pending.setdefault(q['file'],load(path));cur=doc;parts=q['ypath'].split('.')
            for part in parts[:-1]:
                if part not in cur:cur[part]={}
                cur=cur[part]
                if not isinstance(cur,dict):raise ValueError('Incompatible YAML path')
            old=cur.get(parts[-1])
            if real(old) and old!=v:raise ValueError('Existing YAML value conflict; no overwrite')
            cur[parts[-1]]=v
            newrecords[k]={'value':v,'source':source,'source_sha256':hashlib.sha256(sp.read_bytes()).hexdigest(),'question':q['q']}
        for rel,doc in pending.items():write(bp(rel),doc)
        write(bp('evidence/answers.json'),newrecords)
        return {'status':'ANSWERS_RECORDED','total':len(newrecords),'consolidated':False}
    if args.command=='consolidate':
        if not args.reviewed:raise ValueError('User review required: --reviewed')
        if not records:raise ValueError('BLOCKED_CONTEXT: no collected answers')
        essentials=['company_essence.trade_name','company_essence.one_liner','core_icp.one_sentence_definition','pricing_foundation.pricing_model']
        missing=[s for s in essentials if not any(k.endswith('::'+s) and real(v['value']) for k,v in records.items())]
        if missing:raise ValueError('BLOCKED_CONTEXT: missing essentials '+', '.join(missing))
        lines=['# ContextOS — '+slug,'','Consolidado de respostas com revisão humana declarada. Não certifica completude nem veracidade.','']
        for k,v in records.items():
            sp=bp(v['source'])
            if hashlib.sha256(sp.read_bytes()).hexdigest()!=v['source_sha256']:raise ValueError('Source changed; review required')
            lines += ['## '+v['question'],json.dumps(v['value'],ensure_ascii=False),f"Fonte: {v['source']} | SHA256: {v['source_sha256']}",f'Campo: {k}','']
        out=bp('contexto.md');content='\n'.join(lines)
        if out.exists() and out.read_text(encoding='utf-8')!=content:raise ValueError('Consolidated context exists; no overwrite')
        if not out.exists():write(out,content,True)
        return {'status':'CONSOLIDATED','answers':len(records),'semantic_review':'human_declared','output':str(out)}
if __name__=='__main__':
    try:print(json.dumps(main(),ensure_ascii=False,indent=2))
    except (ValueError,KeyError,TypeError,OSError) as e:
        print(json.dumps({'status':'BLOCKED_CONTEXT','reason':str(e)},ensure_ascii=False));sys.exit(2)
