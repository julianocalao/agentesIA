---
name: copy-ads
description: "Escreve anúncios de resposta direta com variações conceituais (framework P.D.A.), validados anti-IA + oráculo."
when-to-use: >
  Quando o usuário quiser anúncio, ads, criativo de tráfego, copy de anúncio, anúncio de Facebook/Instagram, ou disser "anúncio", "ads", "criativo de tráfego", "copy de anúncio", ou /copy:ads.
argument-hint: "[produto / oferta / contexto]"
allowed-tools: "Read, Write, Bash, Glob, Grep, Agent"
user-invocable: true
---

# Copy: Anúncios (resposta direta)

Atalho direto pra anúncios (resposta direta). Internamente despacha o copywriter especialista e valida.

## PASSO 1 — Contexto do cliente (ContextOS)

Leia `../coreai-shared/contextos-contract.md` antes de qualquer produção. Resolva o negócio ativo, rode o gate e só prossiga com READY. Sem contexto validado, bloqueie a redação e ofereça `coreai-contexto`.

## PASSO 2 — DNA permanente
Ler `../coreai-copy-shared/references/premissa-core.md` e `manual-craft.md`.

## PASSO 3 — Triagem mínima
Confirmar faixa de preço, temperatura do público e a oferta/contexto. Se faltar tese,
big idea ou mecanismo único, avisar que a copy sai genérica e sugerir diagnóstico.

## PASSO 4 — Formato obrigatório: Anúncio Estático
Todo anúncio segue o template `../coreai-copy-shared/templates/anuncio-estatico.md`. Carregue-o.
Cada anúncio tem 5 blocos, nesta ordem:
- **ÂNGULO** — nome do conceito em CAIXA ALTA (rótulo). Vários anúncios compartilham o mesmo ângulo.
- **HEADLINE** — até 10 palavras (máx 15). Choque/gancho que vai grande na arte. Nunca pergunta.
- **SUBHEADLINE** — até 20 palavras. O número/dado que dá lastro (faturamento, margem, prazo, prova).
- **PONTE** — explicação que gera desejo (a viragem: inimigo, reframe ou prova social).
- **CTA** — curto, 1ª pessoa do desejo ("Quero ver a conta", "Quero entender o modelo").

Respeitar os limites de palavras é obrigatório. Ver exemplos reais no template.

## PASSO 5 — Despachar escritor
Despachar via Agent tool o especialista em anúncios (resposta direta): **john-carlton**
(alternativa: gary-halbert). Passar contexto do cliente + persona
(`../coreai-copy-shared/agents/john-carlton.md`) + o template `anuncio-estatico.md`. O escritor
produz no estilo dele, dentro do formato de 5 blocos.

## PASSO 6 — Validação obrigatória
1. Filtro Anti-IA (`../coreai-copy-shared/validators/filtro-anti-ia.md`) — nota 10 em todas as 5 dimensões ou refaz.
2. Oráculo Torriani (`../coreai-copy-shared/validators/oraculo-torriani.md`) — regras invioláveis, clichês, craft, Sugarman ≥15.
Loop até passar (máx 3 iterações).

## Output
A peça de anúncios (resposta direta), validada e pronta. Salvar e indicar o que foi gerado.

## Regras
1. Sempre carregar o cliente antes de escrever.
2. Nunca entregar sem passar nos 2 validadores.
3. Zero invenção fora do briefing/contexto. PT-BR, acentuação completa, sem emoji, sem travessão.
