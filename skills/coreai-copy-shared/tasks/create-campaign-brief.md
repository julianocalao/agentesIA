# Create Campaign Brief

Interactive task that guides the user through creating a `campaign-brief.yaml` for a specific product campaign. Auto-fills what it can from loaded product context and asks for what's missing.

## Metadata

```yaml
task:
  name: Create Campaign Brief
  id: create-campaign-brief
  version: "1.0.0"
  category: strategy
  estimated_time: "10-20 min"
  executor: copy-chief
  primary_agents:
    - copy-chief
  elicit: true
  outputs:
    - campaign-brief.yaml
  template: "[DEPENDÊNCIA NÃO EMPACOTADA: campaign-brief]"
```

---

## Purpose

Create the minimum viable campaign brief that unlocks copy creation commands. This is the gate artifact — without it, all creation commands (`*ads`, `*sales-page`, `*vsl`, etc.) remain blocked.

---

## Pre Conditions
- Business slug e product slug definidos (via session context ou argumento)
- Gate `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>` em READY, com brand e product truth acessiveis
- Usuario disponivel para responder 15 perguntas interativas
- Template de campaign brief disponivel (nao empacotado; sem ele, usar o schema desta task)
- Gate do contrato (`../coreai-shared/scripts/gate.py`, Python 3.9+) disponivel

## Required Inputs

```yaml
required:
  - business_slug (from session context or --business arg)
  - product_slug (from session context or --product arg)

optional:
  - campaign_slug (if not provided, generate from objective + date)
```

---

## Workflow

### Step 0: Load Product Context (Auto)

Load from session context — DO NOT ask the user for data that already exists:

```yaml
auto_fill_from:
  # caminhos relativos à raiz do Context OS; rodar antes o gate do contrato:
  # ../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>
  contexto: "businesses/<slug>/contexto.md"   # sempre em sources do gate
  icp: "negocios/<slug>/cerebro/empresa/contexto/icp.yaml"
  brandbook: "negocios/<slug>/cerebro/areas/marketing/contexto/brand.yaml"
  offerbook: "negocios/<slug>/cerebro/areas/produto/"
  proof: "negocios/<slug>/cerebro/empresa/contexto/evidencias/"
  testimonials: "negocios/<slug>/cerebro/empresa/contexto/credentials.yaml"
  pricing: "negocios/<slug>/cerebro/areas/vendas/contexto/pricing.yaml"
  # arquivo ausente = lacuna declarada, nunca invenção"
```

### Step 1: Campaign Identity (Elicit)

Ask the user:

```
1. Qual o OBJETIVO principal desta campanha?
   (Ex: vender turma 2, captar leads, remarketing, lançamento)

2. Qual o nome/slug da campanha?
   (Ex: turma2-lancamento-abril, ads-cohort-advanced-q2)
   → Se não souber, eu gero baseado no objetivo + data.

3. Qual o período da campanha?
   (Ex: 15/03 a 08/04/2026)
```

### Step 2: Channels & Assets (Elicit)

Ask the user:

```
4. Quais CANAIS serão usados? (marque os que aplicam)
   [ ] Meta Ads (Feed + Stories + Reels)
   [ ] Google Ads (Search + YouTube)
   [ ] TikTok Ads
   [ ] Email marketing
   [ ] WhatsApp
   [ ] Orgânico (Instagram/YouTube/X)
   [ ] Landing page / Sales page
   [ ] Webinar / VSL
   [ ] Outro: ___

5. Quais ASSETS precisam ser criados?
   [ ] Anúncios (copy de ads)
   [ ] Página de vendas / Landing page
   [ ] Email sequence
   [ ] VSL / Webinar script
   [ ] Headlines / Hooks
   [ ] WhatsApp messages
   [ ] Outro: ___
```

### Step 3: Audience Slice (Elicit — only what's NOT in ICP)

Show the user what was auto-loaded from ICP, then ask:

```
ICP carregado: {icp_name} ({icp_age_range}, {n} archetypes)

6. Para esta campanha, qual SEGMENTO priorizar?
   [ ] Todos os archetypes
   (listar archetypes carregados do icp.yaml dinamicamente)

7. Qual o NÍVEL DE CONSCIÊNCIA do público desta campanha?
   [ ] Unaware (não sabe que tem o problema)
   [ ] Problem-aware (sabe que tem o problema)
   [ ] Solution-aware (sabe que existem soluções)
   [ ] Product-aware (conhece o produto mas não comprou)
   [ ] Most-aware (já conhece, precisa do push final)

8. Tráfego: frio, morno ou quente?
   [ ] Frio (nunca ouviu falar)
   [ ] Morno (já viu conteúdo/live)
   [ ] Quente (já está na lista/comunidade)
```

### Step 4: Offer & CTA (Elicit — fill from offerbook, confirm)

Show what was auto-loaded, ask for confirmation/overrides:

```
Oferta carregada: {product_name} (do offerbook.yaml)
Preço carregado: {price} ({vagas} vagas)

9. O preço e condições para esta campanha são os mesmos?
   Se diferente, qual o preço/parcelamento?

10. Qual o CTA principal?
    [ ] Link para página de vendas
    [ ] Link para WhatsApp
    [ ] Link para formulário de aplicação
    [ ] Link para webinar/VSL
    [ ] Outro: ___

11. Existe escassez REAL para esta campanha?
    (Ex: 50 vagas, data limite, bônus expirando)
```

### Step 5: Mood & Constraints (Elicit)

```
12. Qual o MOOD da campanha? (selecione 1-2)
    [ ] Urgente / escassez (últimas vagas, tempo acabando)
    [ ] Inspiracional (transformação, sonho, possibilidade)
    [ ] Proof-heavy (resultados, números, depoimentos)
    [ ] Provocativo (desafio, confronto de crenças)
    [ ] Educacional (demonstração de valor, conteúdo)
    [ ] Emocional (histórias de transformação)

13. Existe alguma RESTRIÇÃO ou DON'T específico?
    (Além dos forbidden words da marca)

14. Referências visuais ou de copy?
    (Links, exemplos, campanhas anteriores)
```

### Step 6: Success Metrics (Elicit)

```
15. Como medir SUCESSO desta campanha?
    [ ] CPL (Custo por Lead) — target: R$___
    [ ] CPA (Custo por Aquisição) — target: R$___
    [ ] ROAS — target: ___x
    [ ] Vagas preenchidas — target: ___/50
    [ ] CTR — target: ___%
    [ ] Outro: ___
```

### Step 7: Generate & Save

1. Compile all answers into `campaign-brief.yaml`
2. Auto-fill `source_of_truth` with canonical file paths
3. Auto-fill `proof` section from loaded proof.yaml and testimonials.yaml
4. Auto-fill `constraints.brand_constraints` from brandbook.yaml forbidden words
5. Save to `<raiz>/businesses/<slug>/outputs/campanhas/{campaign_slug}/campaign-brief.yaml` (gate READY antes de gravar)
6. Report campaign_slug in the session (do not persist selection without user authorization)
7. Show confirmation with the gate status

### Step 8: Verify Gate

Run `python ../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>` and show result.

If READY, show the now-unlocked creation commands.

---

## Output Contract

File saved to: `<raiz>/businesses/<slug>/outputs/campanhas/{campaign_slug}/campaign-brief.yaml`

Session context updated with `campaign_slug`.

---

## Quality Checklist

- [ ] All 15 questions answered or explicitly skipped
- [ ] Auto-filled data traced to source files (no invention)
- [ ] campaign_slug is explicit and slugified
- [ ] File saved to correct path
- [ ] Session context updated
- [ ] Gate check returns ALLOWED after save

---

## Guardrails

1. DO NOT invent answers — if the user doesn't know, mark as `TBD` and note it as a blocker.
2. DO NOT skip the elicitation — this task is interactive by design.
3. Auto-fill aggressively from loaded context — minimize user effort.
4. If pricing is `nao_divulgado_publicamente` in source, ask the user explicitly.
5. The brief is MINIMUM VIABLE — it unlocks the gate. The full campaign planning pack (`*campaign-planning-pack`) adds message architecture, creative brief, and asset briefs on top.

## Output Example

```yaml
# campaign-brief.yaml — Mentoria Elite

campaign:
  name: "Lançamento Mentoria Elite Q2-2026"
  slug: "mentoria-elite-q2"
  type: "internal-launch"
  status: "active"

product:
  name: "Mentoria Elite"
  price: 12000
  currency: "BRL"
  format: "Mentoria individual (12 semanas)"
  mechanism: "Método 3R — Diagnóstico + Implementação Guiada"

audience:
  icp: "Mentores/consultores faturando R$5-15k/mês querendo escalar"
  awareness_level: "solution-aware"
  sophistication: 3
  traffic_temperature: "warm"

objective:
  revenue_target: 240000
  sales_target: 20
  timeline: "45 dias"

channels:
  - "email-sequence"
  - "webinar"
  - "call-de-vendas"

blockers: []
```

## Veto Conditions
- Projeto sem objetivo claro definido pelo cliente
- Falta de informacao minima sobre produto, mercado ou publico
- Cliente nao aprovou escopo antes de iniciar producao
