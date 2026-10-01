---
name: copy-carta-vendas
description: "Escreve cartas de venda com estratégia obrigatória e validação Oráculo desde a escrita."
when-to-use: >
  Quando o usuário quiser uma carta de venda, sales letter, carta-mãe, copy longa de
  conversão, ou disser "carta de venda", "escreve uma carta", "sales letter", ou /copy:carta-vendas.
argument-hint: "[produto / oferta / contexto]"
allowed-tools: "Read, Write, Bash, Glob, Grep, Agent"
user-invocable: true
---

# Copy: Carta de Vendas (workflow obrigatório)

Cartas de venda seguem 4 estágios obrigatórios, com critérios do Oráculo aplicados
desde a escrita. Copy sem estratégia é commodity, não passa.

## PASSO 1 — Contexto do cliente (ContextOS)

Leia `../coreai-shared/contextos-contract.md` antes de qualquer produção. Resolva o negócio ativo, rode o gate e só prossiga com READY. Sem contexto validado, bloqueie a redação e ofereça `coreai-contexto`.

## PASSO 2 — DNA permanente
Ler `../coreai-copy-shared/references/premissa-core.md` e `manual-craft.md`.

## PASSO 3 — Os 4 estágios
1. **Estratégia** (veto se faltar): diagnóstico completo, big idea, funnel thesis,
   brief pro escritor. Sem isso, NÃO escrever.
2. **Escrita**: despachar gary-halbert (storytelling/emocional) ou stefan-georgi
   (RMBC/resposta direta). Promessa não copiável, mecanismo único, prova em toda afirmação.
3. **Validação Oráculo** (veto se faltar): não publicar sem passar.
4. **Entrega**: carta final + relatório de validação.

## PASSO 4 — Despachar escritor
Despachar o copywriter via Agent tool com: contexto do cliente, persona
(`../coreai-copy-shared/agents/{escritor}.md`), brief estratégico do estágio 1.

## PASSO 5 — Validação obrigatória (zero exceção)
1. Filtro Anti-IA (`../coreai-copy-shared/validators/filtro-anti-ia.md`) — nota 10 ou refaz.
2. Oráculo Torriani (`../coreai-copy-shared/validators/oraculo-torriani.md`) — regras, clichês, craft, Sugarman ≥15.

## Output
Carta de vendas completa e validada.

## Regras
1. Sem estágio 1 (estratégia) → não escrever.
2. Sem estágio 3 (validação) → não publicar.
3. Zero invenção fora do briefing. PT-BR, sem emoji, sem travessão.
