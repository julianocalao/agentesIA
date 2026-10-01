---
name: copy-operacao-tatica
description: "Modo rápido de copy pra público quente e base existente: pula a estratégia e vai direto pra peça."
when-to-use: >
  Quando o usuário já tem mapa/oferta/carta-mãe e quer uma peça específica rápido,
  público quente, ou disser "operação tática", "copy rápida", "já tenho a base, só preciso da peça",
  ou /copy:operacao-tatica.
argument-hint: "[peça que quer / contexto existente]"
allowed-tools: "Read, Write, Bash, Glob, Grep, Agent"
user-invocable: true
---

# Copy: Operação Tática — Modo Rápido

Para quando já existe base estratégica (mapa, oferta, big idea). Pula etapas 1-5 e
entra direto no ponto certo. Público quente, entrega rápida.

## PASSO 1 — Contexto do cliente (ContextOS)

Leia `../coreai-shared/contextos-contract.md` antes de qualquer produção. Resolva o negócio ativo, rode o gate e só prossiga com READY. Sem contexto validado, bloqueie a redação e ofereça `coreai-contexto`.

## PASSO 2 — DNA permanente
Ler `../coreai-copy-shared/references/premissa-core.md` e `manual-craft.md`.

## PASSO 3 — Triagem rápida (ponto de entrada)
Perguntar o que já existe e o que quer:
1. Nova oferta pra produto existente → Etapa Oferta (value equation Hormozi).
2. Copy mestre (carta-mãe) → precisa de oferta. Despachar gary-halbert / stefan-georgi.
3. Headlines e ângulos novos → precisa de copy mestre. Despachar gary-bencivenga.
4. Peça específica (sales page, e-mail, ad) → precisa de copy mestre + arsenais.

VETO: se o input obrigatório não existe, criar primeiro (avisar e voltar uma etapa).

## PASSO 4 — Despachar escritor + escrever
Conforme a peça, despachar o copywriter certo (ver tabela na skill `copy`) com o contexto.

## PASSO 5 — Validação obrigatória
1. Filtro Anti-IA (`../coreai-copy-shared/validators/filtro-anti-ia.md`).
2. Oráculo Torriani (`../coreai-copy-shared/validators/oraculo-torriani.md`).

## Output
A peça pedida, validada. Indicar de onde partiu (qual base usou).

## Regras
1. Não escrever sem a base obrigatória do ponto de entrada.
2. Sempre validar nos 2 layers. PT-BR, sem emoji, sem travessão.
