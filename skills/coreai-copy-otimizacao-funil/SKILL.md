---
name: copy-otimizacao-funil
description: "Otimiza um funil existente (CRO): diagnostica gargalos e reescreve as peças fracas."
when-to-use: >
  Quando o usuário quiser otimização de funil, CRO, melhorar conversão, otimizar funil, aumentar conversão, ou disser "otimização de funil", "CRO", "melhorar conversão", ou /copy:otimizacao-funil.
argument-hint: "[produto / oferta / contexto]"
allowed-tools: "Read, Write, Bash, Glob, Grep, Agent"
user-invocable: true
---

# Copy: Otimização de funil (CRO)

Atalho de otimização de funil (CRO). Despacha o especialista certo e segue o workflow de referência.

## PASSO 1 — Contexto do cliente (ContextOS)

Leia `../coreai-shared/contextos-contract.md` antes de qualquer produção. Resolva o negócio ativo, rode o gate e só prossiga com READY. Sem contexto validado, bloqueie a redação e ofereça `coreai-contexto`.

## PASSO 2 — DNA permanente + material de apoio
Ler `../coreai-copy-shared/references/premissa-core.md` e `manual-craft.md`.
Workflow de referência: `../coreai-copy-shared/workflows/otimizacao-funil.md` (seguir as etapas dele).
Apoio disponível: `../coreai-copy-shared/templates/`, `../coreai-copy-shared/frameworks/`,
`../coreai-copy-shared/swipe/`, `../coreai-copy-shared/checklists/`.

## PASSO 3 — Triagem
Confirmar faixa de preço, temperatura do público e oferta/contexto. Verificar premissas
(tese, big idea, mecanismo único). Sem isso, avisar que sai genérico.

## PASSO 4 — Executar o workflow
Seguir as etapas de `../coreai-copy-shared/workflows/otimizacao-funil.md`. Em cada peça, despachar o
copywriter certo via Agent tool (especialista sugerido: **claude-hopkins**), passando o
contexto + a persona (`../coreai-copy-shared/agents/{escritor}.md`) + os frameworks dele
(`../coreai-copy-shared/frameworks/{escritor}/`).

## PASSO 5 — Validação obrigatória (cada peça)
1. Filtro Anti-IA (`../coreai-copy-shared/validators/filtro-anti-ia.md`) — nota 10 ou refaz.
2. Oráculo Torriani (`../coreai-copy-shared/validators/oraculo-torriani.md`) — regras, clichês, craft, Sugarman ≥15.

## Output
As peças do otimização de funil (CRO), validadas. Listar o que foi gerado e a ordem de uso no funil.

## Regras
1. Seguir as etapas do workflow de referência, sem pular input obrigatório.
2. Toda peça passa pelos 2 validadores.
3. Zero invenção fora do briefing/contexto. PT-BR, acentuação completa, sem emoji, sem travessão.
