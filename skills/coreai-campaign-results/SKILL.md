---
name: campaign-results
description: >
  Registra resultados de uma campanha existente do business ativo do
  ContextOS deste pacote. Lista campanhas, deixa escolher uma, pergunta
  métricas (leads, vendas, ROI, CPA, learnings) e preenche results.yaml.
  Acionar quando o usuário disser "resultados de campanha", "preencher
  results", "fechar campanha", ou /coreai:campaign-results.
---

# Campaign Results

Coleta e registra métricas finais de uma campanha.

## Pré-requisitos

- Leia `../coreai-shared/contextos-contract.md` e resolva o negócio ativo antes
  de qualquer escrita. Sem READY, bloqueie e ofereça `coreai-contexto`.
- Campanha criada via `coreai-campaign-new`.
- Arquivo `results.yaml` existe na pasta da campanha.
- A raiz do Context OS chega por parâmetro (`--root`/`--context-root`); `BUSINESS_ROOT`
  é `<raiz>/businesses/<slug>` e as campanhas ficam em `$BUSINESS_ROOT/outputs/campanhas/`.

## Passos

### 1. Listar campanhas

Use `business_root` retornado pelo gate:

```bash
ls "$BUSINESS_ROOT/outputs/campanhas/" | grep -v '^_' | grep -v assets
```

Mostre numerada e peça escolha.

### 2. Coletar métricas (perguntas em ordem)

- Início (YYYY-MM-DD)
- Fim (YYYY-MM-DD)
- Canais usados (lista separada por vírgula)
- Investimento total em BRL (número)
- Investimento por canal (Meta Ads, Google Ads, outros)
- Impressões, cliques, CTR
- Leads, qualified leads
- Reuniões agendadas / realizadas
- Vendas, receita BRL
- CPA, CPL, ROI, ROAS
- O que funcionou (lista)
- O que não funcionou (lista)
- Ações pra próxima campanha (lista)
- Notas livres

Aceite "skip" ou vazio para pular.

### 3. Escrever YAML

Valide o destino com o gate antes de escrever:

```bash
python "${CLAUDE_SKILL_DIR}/../coreai-shared/scripts/gate.py" --root "<raiz>" --business "<slug>" --output "$BUSINESS_ROOT/outputs/campanhas/<campanha>/results.yaml"   # precisa devolver READY
```

Atualize `$BUSINESS_ROOT/outputs/campanhas/<campanha>/results.yaml` preservando estrutura do template. Use Python inline com `yaml.safe_dump(allow_unicode=True, sort_keys=False)`.

### 4. Atualizar índice

Em `$BUSINESS_ROOT/outputs/campanhas/_index.yaml` (também validado pelo gate), mude `status: planejada` → `status: encerrada` e adicione `encerrada_em`.

### 5. Resumo

```
Resultados registrados: <campanha>
ROI: <X>x | Vendas: <Y> | Receita: R$<Z>
Local: <business_root>/outputs/campanhas/<campanha>/results.yaml
```

## Edge cases

- Nenhuma campanha → sugerir `coreai-campaign-new`.
- `results.yaml` ausente → copiar de `${CLAUDE_SKILL_DIR}/../coreai-campaign-new/templates/results.yaml` e seguir.
