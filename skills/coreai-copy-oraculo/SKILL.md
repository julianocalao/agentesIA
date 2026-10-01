---
name: copy-oraculo
description: "Valida uma copy existente nas 2 camadas: filtro Anti-IA (5 dimensões) e Oráculo Torriani."
when-to-use: >
  Quando o usuário quiser validar/auditar uma copy já escrita, checar se passa no anti-IA
  e no oráculo, ou disser "valida essa copy", "roda o oráculo", "audita essa copy",
  "passa no anti-ia", ou /copy:oraculo.
argument-hint: "[caminho ou texto da copy a validar]"
allowed-tools: "Read, Write, Bash, Glob, Grep"
user-invocable: true
---

# Copy: Oráculo — Validação Imperial

Valida uma copy existente. Não escreve, julga. Nota 10 ou refaz, sem meio-termo.

## PASSO 1 — Receber a copy
Pegar a copy de `$ARGUMENTS` (caminho de arquivo ou texto colado). Se vazio, pedir.

## PASSO 2 — (Opcional) Contexto do cliente
Se a validação depende de voz/posicionamento, leia `../coreai-shared/contextos-contract.md`,
resolva o negócio ativo e use o `contexto.md` consolidado dele.

## PASSO 3 — Camada 0: Filtro Anti-IA
Aplicar `../coreai-copy-shared/validators/filtro-anti-ia.md`. As 5 dimensões precisam de nota 10
cada. Qualquer <10 = REPROVADO. Se reprovar, NÃO avança pro oráculo: devolve a lista
de violações.

## PASSO 4 — Camada 1: Oráculo Torriani
Só se passou na camada 0. Aplicar `../coreai-copy-shared/validators/oraculo-torriani.md`:
- Regras invioláveis (RU) + clichês (CL) → veto instantâneo.
- Craft (RC-01..RC-10).
- 5 critérios master (10/10 cada).
- Sugarman: mínimo 15 dos 30 triggers, com os 7 essenciais.

## Output
Veredito claro:
```
ANTI-IA: {PASS/REPROVADO} — {dimensões e notas}
ORÁCULO: {APROVADO 10/10 / REPROVADO}
{Se reprovado: lista de violações + como corrigir cada uma}
```

## Regras
1. Reprovou no anti-IA, nem roda o oráculo.
2. 10/10 ou refaz. 9 não passa.
3. Cada violação vem com exemplo concreto e correção. PT-BR, sem emoji, sem travessão.
