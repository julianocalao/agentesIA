---
name: campaign-new
description: >
  Cria nova campanha de marketing dentro do business ativo do ContextOS
  deste pacote. Pergunta nome, slugifica como YYYY-MM-slug, cria pasta em
  outputs/campanhas/ (validada pelo gate) e copia os templates brief.md, execution.md,
  results.yaml embutidos nesta skill. Acionar quando o usuário disser
  "nova campanha", "criar campanha", "registrar campanha", ou
  /coreai:campaign-new.
---

# Campaign New

Cria pasta de campanha com templates iniciais, dentro do ContextOS já resolvido.

## Pré-requisitos

- Leia `../coreai-shared/contextos-contract.md` e resolva o negócio ativo antes
  de qualquer escrita. Sem READY, bloqueie e ofereça `coreai-contexto`.
- Templates desta skill: `${CLAUDE_SKILL_DIR}/templates/brief.md`,
  `${CLAUDE_SKILL_DIR}/templates/execution.md`, `${CLAUDE_SKILL_DIR}/templates/results.yaml`
  (embutidos, resolvidos pela pasta da skill, nunca pelo diretório atual).
- A raiz do Context OS chega por parâmetro (`--root`/`--context-root`); `BUSINESS_ROOT`
  é `<raiz>/businesses/<slug>`.

## Passos

### 1. Coletar nome

Pergunte: "Qual o nome da campanha?" (ex: "Black Friday 2026").

Slugify: lowercase, sem acentos, espaços → hífen.

Prefixo: `YYYY-MM-` baseado em data atual.

Exemplo: `2026-04-black-friday-2026`

### 2. Criar pasta

Use `business_root` retornado pelo gate como raiz do negócio ativo
(`BUSINESS_ROOT=<raiz>/businesses/<slug>`). O destino fica sempre em
`outputs/campanhas/` e passa pelo gate antes de qualquer escrita:

```bash
DEST="$BUSINESS_ROOT/outputs/campanhas/<campanha>"
python "${CLAUDE_SKILL_DIR}/../coreai-shared/scripts/gate.py" --root "<raiz>" --business "<slug>" --output "$DEST"   # precisa devolver READY
mkdir -p "$DEST/assets"
```

### 3. Copiar templates

```bash
TPL="${CLAUDE_SKILL_DIR}/templates"  # pasta desta skill, nunca o cwd
cp "$TPL/brief.md" "$DEST/"
cp "$TPL/execution.md" "$DEST/"
cp "$TPL/results.yaml" "$DEST/"
```

### 4. Atualizar índice

Adicionar entry em `$BUSINESS_ROOT/outputs/campanhas/_index.yaml` (mesmo gate, com `--output` apontando para esse arquivo):

```yaml
campaigns:
  - slug: <campanha>
    nome: <nome>
    status: planejada
    criada_em: <YYYY-MM-DD>
```

### 5. Confirmar

```
Campanha criada: <campanha>
Local: <business_root>/outputs/campanhas/<campanha>/

Próximos passos:
  - Edite brief.md com objetivo, público, oferta, canais.
  - Edite execution.md com plano de execução e cronograma.
  - Após executar, rode coreai-campaign-results pra registrar números.
```

## Edge cases

- Pasta já existe → adicione sufixo `-2`, `-3`, etc.
- Sem contexto de negócio válido → orientar `coreai-contexto`.
