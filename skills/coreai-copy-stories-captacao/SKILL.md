---
name: coreai-copy-stories-captacao
description: "Cria um BANCO de stories de captação (a peça): stories únicos que captam lead via palavra-chave no Direct. Saída em .md + HTML interativo."
when-to-use: >
  Quando o usuário quiser stories de captação, story único (a PEÇA, não o funil), banco de stories
  pra Instagram, stories pra captar lead, ou disser "stories de captação", "story único",
  "me cria stories pra captar", ou coreai-copy-stories-captacao. NÃO é o funil completo (esse é
  copy-funil-story-unico). Aqui entrega só a peça: o banco de variações de story.
argument-hint: "[cliente / isca / palavra-chave / quantidade]"
allowed-tools: "Read, Write, Bash, Glob, Grep, Agent"
user-invocable: true
---

## Contrato CoreAI obrigatório

Nome de apresentação: **CoreAI:stories-captacao**. Resolva todos os caminhos relativos a este SKILL.md, nunca ao diretório de trabalho. Antes dos passos abaixo, leia `../coreai-shared/contextos-contract.md`. O contrato comum prevalece sobre qualquer instrução antiga de descoberta de cliente neste documento. Confirme cliente, produto pertinente e fontes carregadas; sem contexto necessário, bloqueie produção e encaminhe a `coreai-contexto`. Nunca invente dados nem use outro cliente como padrão. O contexto do cliente fica fora da instalação global.

A biblioteca obrigatória é `../coreai-copy-shared/`. Se faltar, use `coreai-setup`; não execute os comandos antigos de instalação deste documento. Ferramentas de subagentes dependem do ambiente: se indisponíveis, declare a limitação e não alegue delegação realizada. Scores de revisão são avaliação assistida, não testes automáticos.


# Copy: Stories de Captação (a peça)

Cria um banco de stories de captação no formato canônico Torriani. Cada story é UMA tela
completa (abertura + contexto/isca + CTA) que leva a pessoa a mandar uma palavra-chave no Direct.

> **NÃO confundir:** esta skill entrega A PEÇA (o banco de stories). O FUNIL macro
> (48h silêncio → story → ManyChat → isca → reunião → venda) é a skill `copy-funil-story-unico`.

## PASSO 1 — ContextOS

Execute `../coreai-shared/contextos-contract.md` e mantenha cliente, produto e fontes explícitos antes de produzir.

## PASSO 2 — Material de referência (LER ANTES DE ESCREVER)
- Template/método: `../coreai-copy-shared/templates/stories-captacao-tmpl.md` (estrutura de 3 blocos,
  5 tipos de abertura, regras de voz, exemplos-ouro).
- Task de execução: `../coreai-copy-shared/tasks/create-stories-captacao.md` (passo-a-passo).
- Template HTML de saída: `../coreai-copy-shared/templates/stories-captacao-html-tmpl.html`.

## PASSO 3 — Inputs obrigatórios (perguntar se faltar)
1. Cliente/slug. 2. A isca (relatório, guia, estudo de caso, diagnóstico, reunião).
3. Palavra-chave do Direct (1 palavra CAIXA ALTA). 4. Quantidade (default 15). 5. Contexto da oferta.
Sem isca ou sem palavra-chave clara → PARAR (story sem entrega = desconfiança; CTA confuso = não responde).

## PASSO 4 — Gerar o banco
Seguir `create-stories-captacao.md`: produzir N variações de 3 blocos, alternando os 5 tipos de
abertura, mesma palavra-chave, número específico sempre que possível.

## PASSO 5 — Validação obrigatória
1. Filtro Anti-IA (`../coreai-copy-shared/validators/filtro-anti-ia.md` ou `scripts/anti-ia-validate.mjs`) — exit 0 / nota 10 ou refaz.
2. Oráculo Torriani (`../coreai-copy-shared/validators/oraculo-torriani.md`) — 10/10. Sugarman ≥ 15 no banco.

## PASSO 6 — Saída
- Gravar `.md` com o banco em `<raiz>/businesses/<slug>/outputs/campanhas/<campanha>/stories/`, depois de rodar `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <esse caminho>` e obter READY (revalidar imediatamente antes da escrita).
- Gerar o `.html` interativo a partir do template (cards, copiar, marcar usado).
- Listar: quantos stories, palavra-chave, isca, instrução de uso (1 por dia, alternar temas).

## Regras
1. Estrutura de 3 blocos sempre (abertura + contexto + CTA). Uma ideia por story.
2. Toda peça passa pelos 2 validadores. Copy 10/10 ou refaz.
3. PT-BR, acentuação completa, ZERO emoji e ZERO travessão no corpo.

## Disponibilidade antes de executar

Leia `../coreai-copy-shared/ROUTE-COVERAGE.md` antes de qualquer processo abaixo. Seus estados por rota e restrições prevalecem sobre promessas antigas de entrega pronta. Classificação estrutural não é teste runtime.
