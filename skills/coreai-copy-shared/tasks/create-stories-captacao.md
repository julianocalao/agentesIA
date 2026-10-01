# Task — Criar Stories de Captação

> **Squad:** copy · **Tipo:** task de execução
> **Gatilhos:** "stories de captação", "story único" (a peça), "me cria stories pra captar lead no Instagram"
> **Template:** `templates/stories-captacao-tmpl.md`
> **Template HTML:** `templates/stories-captacao-html-tmpl.html`
> **NÃO é:** o funil completo (`workflows/funil-story-unico.md`). Esta task entrega só a PEÇA (o banco de stories).

---

## Quando usar
Quando o usuário pede stories de captação para Instagram (a peça): um banco de variações de
story único pra postar e captar lead via palavra-chave no Direct.

## Inputs obrigatórios (perguntar se não vierem)
1. **Cliente/business slug** (rodar o gate `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>` e carregar o `contexto.md` das `sources`; voz em `negocios/<slug>/cerebro/areas/marketing/contexto/brand.yaml`, campo `voice_dna`).
2. **A isca** (o que a pessoa recebe ao responder: relatório, guia, estudo de caso, diagnóstico, reunião).
3. **A palavra-chave** do Direct (1 palavra, CAIXA ALTA, ex: AGENTE, REUNIÃO, BOARD).
4. **Quantas variações** (default: 15).
5. **Contexto da oferta/produto** (pra ancorar abertura e contexto).

## Passos

### 1. Carregar contexto
- Voz do cliente (`negocios/<slug>/cerebro/areas/marketing/contexto/brand.yaml`, campo `voice_dna`, e `negocios/<slug>/cerebro/areas/marketing/voice/` se existir). Arquivo ausente = lacuna declarada.
- ICP do cliente (`negocios/<slug>/cerebro/empresa/contexto/icp.yaml`, pra calibrar dor/desejo).
- Ler o template `templates/stories-captacao-tmpl.md` (estrutura + 5 tipos de abertura + regras).

### 2. Gerar o banco
- Produzir N variações seguindo a estrutura de 3 blocos (abertura + contexto + CTA).
- **Alternar os 5 tipos de abertura** (como/número/dor/caso/tese). Não repetir tipo em sequência.
- Mesma palavra-chave em todas.
- Número específico sempre que possível.

### 3. Gravar o .md
- Path: `<raiz>/businesses/<slug>/outputs/campanhas/<campanha>/stories/stories-captacao-{tema}.md` (validar com o gate `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <esse caminho>` antes de gravar; exigir READY)
- Listar as N variações numeradas, cada uma com abertura/contexto/CTA.

### 4. Validar (OBRIGATÓRIO)
- `Revisar a campanha com `validators/filtro-anti-ia.md` desta biblioteca; revisão assistida, sem alegar execução de validador automático` → exit 0 ou corrigir.
- Oráculo Torriani 10/10 (`checklists/oraculo-torriani.md`).
- Sugarman ≥ 15 triggers no banco.
- Corrigir e revalidar até passar. NUNCA declarar pronto sem exit 0.

### 5. Gerar o HTML (saída visual)
- Copiar `templates/stories-captacao-html-tmpl.html`.
- Preencher: título da recompensa, palavra-chave, e o array `stories` (n/a/c) com as variações.
- Gravar como `.html` na mesma pasta.
- Servir local (porta 8765) e dar o link IP pro usuário ver no celular, se ele pedir.

## Output
- 1 arquivo `.md` com o banco de N stories de captação (validado).
- 1 arquivo `.html` interativo (cards, copiar, marcar usado).
- Resumo: quantos stories, palavra-chave, isca, e a instrução de uso (1 por dia, alternar temas).

## Veto conditions
- Sem isca definida → PARAR (story que promete sem entregar = desconfiança).
- Sem palavra-chave clara → PARAR (CTA confuso = não responde).
- Anti-IA exit != 0 → NÃO entregar.
- Travessão ou emoji no corpo → reprovar e refazer.
