---
name: copy-operacao-completa
description: "Pipeline completo de copy em 9 etapas: da ideia bruta ao arsenal de peças prontas pra campanha."
when-to-use: >
  Quando o usuário quiser construir uma campanha de copy do zero, o pacote completo,
  da estratégia às peças finais, ou disser "operação completa", "pipeline completo de copy",
  "monta a campanha toda", ou /copy:operacao-completa.
argument-hint: "[produto / ideia / contexto]"
allowed-tools: "Read, Write, Bash, Glob, Grep, Agent"
user-invocable: true
---

# Copy: Operação Completa — Pipeline de 9 Etapas

Pipeline máximo de construção de copy. Constrói tudo, da ideia bruta ao arsenal de
peças. Cada etapa alimenta a próxima. Nada avança sem o input da anterior.

## PASSO 1 — Contexto do cliente (ContextOS)

Leia `../coreai-shared/contextos-contract.md` antes de qualquer produção. Resolva o negócio ativo, rode o gate e só prossiga com READY. Sem contexto validado, bloqueie a redação e ofereça `coreai-contexto`.

## PASSO 2 — DNA permanente
Ler `../coreai-copy-shared/references/premissa-core.md` e `manual-craft.md`.

## PASSO 3 — As 9 etapas (não pular; veto se a anterior não entregou)
1. **Ideia** — clarear a ideia bruta. Verificar se já existe Mapa do Domínio.
2. **Mapa do Domínio** — tom, ICP, diferencial, narrativa do produto.
3. **Pesquisa + Tese + Big Idea** — mecanismo único, prova. (Eugene Schwartz / Dan Kennedy)
4. **Narrativa** — o arco da história de venda.
5. **Oferta** — value equation (Hormozi): valor, garantia, bônus, escassez.
6. **Copy Mestre (carta-mãe)** — a peça central. Despachar gary-halbert ou stefan-georgi.
7. **Arsenais** — banco de headlines + ângulos. Despachar gary-bencivenga.
8. **Derivados** — peças por canal (sales page, VSL, e-mail, ads) a partir da carta-mãe.
9. **Validação** — cada peça passa pelo PASSO 4.

VETO: se uma etapa não produziu o output obrigatório, não avançar. Big Idea sem prova volta pra Etapa 3.

## PASSO 4 — Validação (obrigatória em cada peça)
1. Filtro Anti-IA (`../coreai-copy-shared/validators/filtro-anti-ia.md`) — nota 10 em tudo ou refaz.
2. Oráculo Torriani (`../coreai-copy-shared/validators/oraculo-torriani.md`) — regras + clichês + craft + Sugarman ≥15.

## Output
Pacote da campanha: mapa, tese, big idea, narrativa, oferta, carta-mãe, arsenais e
derivados validados. Salvar organizadamente e listar o que foi gerado.

## Regras
1. Triagem (preço + temperatura) antes de começar.
2. Nada avança sem o input obrigatório da etapa anterior.
3. Toda peça final passa pelos 2 validadores.
4. Zero invenção fora do briefing/contexto. PT-BR, sem emoji, sem travessão.
