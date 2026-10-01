"""Read-only structural resolver; never grants semantic approval."""
import argparse,json,re,sys
from pathlib import Path

def resolve(root,business=None,required=None):
    if not root:return {'status':'BLOCKED_CONTEXT','reason':'Explicit root required'}
    try:
        root=Path(root).expanduser().resolve(strict=True)
        config=root/'config.json'
        if config.is_symlink():raise ValueError('Symlink config rejected')
        data=json.loads(config.read_text(encoding='utf-8')) if config.is_file() else None
        if data is None:
            yaml=root/'config.yaml'
            if yaml.is_symlink():raise ValueError('Symlink config rejected')
            text=yaml.read_text(encoding='utf-8');values=re.findall(r'^active_business:\s*([a-z0-9_-]+)\s*(?:#.*)?$',text,re.M)
            if len(values)>1:raise ValueError('Duplicate active business')
            data={'active_business':values[0] if values else None}
        if not isinstance(data,dict):raise ValueError('Config object required')
        parent=root/'businesses'
        if parent.is_symlink():raise ValueError('Symlink businesses rejected')
        options=sorted(d.name for d in parent.iterdir() if d.is_dir() and not d.is_symlink() and re.fullmatch(r'[a-z0-9][a-z0-9_-]*',d.name))
        chosen=business or data.get('active_business')
        if chosen and chosen not in options:raise ValueError('Business absent or symlink')
        if not chosen:
            if len(options)>1:return {'status':'SELECT_BUSINESS','businesses':options}
            if not options:raise ValueError('No business')
            chosen=options[0]
        folder=parent/chosen;sources=[]
        for name in dict.fromkeys(['contexto.md']+list(required or [])):
            relative=Path(name)
            if relative.is_absolute() or '..' in relative.parts:raise ValueError('Source must remain inside business')
            path=folder/relative
            current=folder
            for part in relative.parts:
                current=current/part
                if current.is_symlink():raise ValueError('Symlink source rejected')
            if not path.resolve().is_relative_to(folder):raise ValueError('Source escapes business')
            if not path.is_file() or not path.read_text(encoding='utf-8').strip():raise ValueError('Missing or empty source: '+name)
            sources.append(str(path))
        return {'status':'READY','validation':'structural_only','semantic_review_required':True,'context_root':str(root),'business_slug':chosen,'business_root':str(folder),'sources':sources}
    except (OSError,ValueError,TypeError) as e:return {'status':'BLOCKED_CONTEXT','reason':str(e)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--root');p.add_argument('--business');p.add_argument('--require',action='append');a=p.parse_args()
    result=resolve(a.root,a.business,a.require);print(json.dumps(result,ensure_ascii=False));return 0 if result['status']=='READY' else 2
if __name__=='__main__':sys.exit(main())
