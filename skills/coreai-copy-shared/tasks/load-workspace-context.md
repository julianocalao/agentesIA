# Load Workspace Context Task

Task para carregar contexto operacional do Context OS (raiz recebida por `--root <raiz>`, contrato `../coreai-shared/contextos-contract.md`) antes de executar qualquer task de copy.

## Metadata

```yaml
task:
  name: Load Workspace Context
  id: load-workspace-context
  version: "1.0.0"
  category: research
  estimated_time: "10-20 min"
  executor: copy-chief
  dependencies:
    - ../coreai-shared/contextos-contract.md
    - ../coreai-shared/scripts/gate.py
    - <raiz>/businesses/<slug>/contexto.md
    - <raiz>/negocios/<slug>/cerebro/   # somente leitura
    - templates/   # desta biblioteca (coreai-copy-shared)
  outputs:
    - <raiz>/businesses/<slug>/outputs/campanhas/{campaign_slug}/campaign-context-brief.yaml
```

---

## Objective

Garantir que o squad de copy use dados reais e regras vigentes do Context OS.

---

## Pre Conditions
- Raiz do Context OS informada nesta sessão (`<raiz>`)
- Gate `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>` retornando READY
- Business slug identificado para carregar brand e product truth
- Pelo menos um template disponivel em `templates/` desta biblioteca

## Phase 1: Governance Snapshot

1. Ler `../coreai-shared/contextos-contract.md`.
2. Rodar `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>` e ler integralmente as `sources` devolvidas (sempre inclui `businesses/<slug>/contexto.md`).
3. Extrair:
   - princípios obrigatórios
   - rules por superfície (`S1`, `S2`, `S3`)
   - stage source of truth
   - campaign slug policy
   - quality gates aplicáveis ao deliverable solicitado
4. Registrar em `governance_constraints`.

---

## Phase 2: Durable Truth Snapshot

1. Carregar a camada `brand`:
   - `negocios/<slug>/cerebro/empresa/contexto/` (`company-profile`, `icp`, `founder-dna`, `credentials`)
   - `negocios/<slug>/cerebro/areas/marketing/contexto/brand.yaml` (`voice_dna`, `brand_core`, `brand_essence`, `promises`)
2. Carregar a camada `product`:
   - `negocios/<slug>/cerebro/areas/produto/`
   - `negocios/<slug>/cerebro/areas/vendas/contexto/pricing.yaml`
   - `negocios/<slug>/cerebro/empresa/contexto/evidencias/`
   - (caminhos relativos à raiz; ver "Onde ler o detalhe" no `contexto.md`; arquivo ausente = lacuna declarada)
3. Registrar:
   - brand truth disponível
   - product truth disponível
   - gaps críticos que impedem `FINAL`

---

## Phase 3: Campaign Snapshot

1. Identificar `campaign_slug` quando o trabalho for estratégico, multi-asset, high-ticket ou `FINAL`.
2. Carregar a camada `campaign` em `<raiz>/businesses/<slug>/outputs/campanhas/{campaign_slug}/` quando existir.
3. Registrar:
   - `campaign_brief`
   - `message_architecture`
   - `creative_brief`
   - `asset_briefs`
4. Se `campaign_slug` não existir:
   - marcar `campaign_context.status: implicit_draft_only`
   - impedir promoção para `FINAL`

---

## Phase 4: Template Snapshot

1. Carregar templates relevantes em `templates/` desta biblioteca.
2. Para cada template usado, mapear:
   - campos obrigatórios
   - campos opcionais
   - lacunas de input do usuário

---

## Output Contract

Salvar arquivo `<raiz>/businesses/<slug>/outputs/campanhas/{campaign_slug}/campaign-context-brief.yaml` (gate READY antes de gravar) com:

```yaml
campaign_context_brief:
  generated_at: "YYYY-MM-DDTHH:mm:ssZ"
  request_type: "<sales-page|email-sequence|ad-copy|...>"
  business_slug: ""
  product_slug: ""
  campaign_slug: ""
  governance_constraints:
    surface: "S1|S2|S3"
    required_rules: []
    quality_gates: {}
    promotion_rule: ""
  source_of_truth:
    brand_layer: []
    product_layer: []
    campaign_layer: []
    delivery_layer:
      - "businesses/<slug>/outputs/copy/..."
  brand_truth:
    available_files: []
    missing_files: []
  product_truth:
    available_files: []
    missing_files: []
  campaign_context:
    status: "ready|missing|implicit_draft_only"
    available_files: []
    missing_files: []
    final_allowed: false
  workflow_alignment:
    selected_workflow: ""
    execution_track: ""
    canonical_artifacts_expected: []
  templates_loaded:
    - path: ""
      required_fields: []
      missing_inputs: []
  assumptions: []
  blockers: []
```

---

## Quality Checklist

- [ ] Leu o contrato e as `sources` do gate READY.
- [ ] Selecionou superfície correta (`S1`, `S2` ou `S3`).
- [ ] Mapeou brand truth, product truth e campaign truth separadamente.
- [ ] Carregou pelo menos 1 template de `templates/`.
- [ ] Registrou `assumptions` e `blockers` no output final.

---

## Fallback

Se algum arquivo obrigatório do Context OS não existir:

1. Reportar exatamente o caminho faltante.
2. Não inventar schema/campos.
3. Se faltar `campaign_slug` ou `campaign-brief.yaml` em trabalho estratégico, marcar `implicit_draft_only`.
4. Pedir insumo mínimo faltante antes de continuar execução de copy.

## Output Example

```yaml
# campaign-context-brief.yaml — Contexto Carregado

workspace_status: "loaded"
timestamp: "2026-04-02T14:30:00Z"

governance:
  source: "businesses/<slug>/contexto.md"
  tone: "direto, confiante, sem hype"
  forbidden_words: ["revolucionário", "incrível", "fantástico"]
  max_qualifiers_per_section: 1

product_context:
  source: "negocios/<slug>/cerebro/areas/produto/"
  name: "Programa Acelerador Digital"
  price: 997
  mechanism: "Método 3R"
  proof_points: 3

campaign_active:
  slug: "acelerador-q2-2026"
  brief_path: "businesses/<slug>/outputs/campanhas/acelerador-q2-2026/campaign-brief.yaml"
  status: "in_production"

missing_files: []
blockers: []
context_quality: "complete"
```

## Veto Conditions
- Gate nao retorna READY ou as sources estao vazias
- Conflito entre contexto carregado e premissa-core.md
