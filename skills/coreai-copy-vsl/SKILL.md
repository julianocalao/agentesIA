---
name: copy-vsl
description: "Escreve scripts de VSL (video sales letter) que prendem e convertem, validados anti-IA + oráculo."
when-to-use: >
  Quando o usuário quiser VSL, video sales letter, script de vídeo de vendas, roteiro de VSL, ou disser "VSL", "video sales letter", "script de vídeo de vendas", ou /copy:vsl.
argument-hint: "[produto / oferta / contexto]"
allowed-tools: "Read, Write, Bash, Glob, Grep, Agent"
user-invocable: true
---

# Copy: Script de VSL (video sales letter)

Atalho direto pra script de VSL (video sales letter). Internamente despacha o copywriter especialista e valida.

## PASSO 1 — Contexto do cliente (ContextOS)

Leia `../coreai-shared/contextos-contract.md` antes de qualquer produção. Resolva o negócio ativo, rode o gate e só prossiga com READY. Sem contexto validado, bloqueie a redação e ofereça `coreai-contexto`.

## PASSO 2 — DNA permanente
Ler `../coreai-copy-shared/references/premissa-core.md` e `manual-craft.md`.

## PASSO 3 — Triagem mínima
Confirmar faixa de preço, temperatura do público e a oferta/contexto. Se faltar tese,
big idea ou mecanismo único, avisar que a copy sai genérica e sugerir diagnóstico.

## PASSO 4 — Despachar escritor
Despachar via Agent tool o especialista em script de VSL (video sales letter): **jon-benson**
(alternativa: stefan-georgi). Passar contexto do cliente + persona
(`../coreai-copy-shared/agents/jon-benson.md`). O escritor produz no estilo dele.

## PASSO 5 — Validação obrigatória
1. Filtro Anti-IA (`../coreai-copy-shared/validators/filtro-anti-ia.md`) — nota 10 em todas as 5 dimensões ou refaz.
2. Oráculo Torriani (`../coreai-copy-shared/validators/oraculo-torriani.md`) — regras invioláveis, clichês, craft, Sugarman ≥15.
Loop até passar (máx 3 iterações).

## Output
A peça de script de VSL (video sales letter), validada e pronta. Salvar e indicar o que foi gerado.

## Regras
1. Sempre carregar o cliente antes de escrever.
2. Nunca entregar sem passar nos 2 validadores.
3. Zero invenção fora do briefing/contexto. PT-BR, acentuação completa, sem emoji, sem travessão.
