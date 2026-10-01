# Pré-escrita Torriani — Pipeline de Consulta OBRIGATÓRIO

> **Severidade: NON-NEGOTIABLE**
> **Quando aplica:** ANTES de escrever qualquer copy/post/roteiro pro Torriani. Nunca depois.
> **Veto:** Pular esse pipeline = REPROVADO automático, independente da qualidade do texto.

---

## Por que essa regra existe

Inteligência viral não pode ser checada DEPOIS da escrita. Ela tem que MOLDAR a escrita. Consultar só na validação já chegou tarde — você vai querer salvar o texto que escreveu em vez de reescrever do zero.

A regra: **antes da primeira palavra, já saber que padrão viralizou e que padrão morreu pra esse tipo de mensagem**.

---

## Pipeline (4 passos em ordem)

### Passo 1 — Briefing original
Ler PDF/documento original do briefing (Grupo Silva ou outro). Extrair LITERAL:
- Headline (manter)
- Gancho (manter literal como primeira frase do reel)
- Ideia central com bullets do que precisa ter
- Fechamento (manter literal como última frase do reel)

Anotar tudo que está no briefing. Tudo que NÃO está no briefing = não inventar.

### Passo 2 — Consultar inteligência viral (OBRIGATÓRIO)

Antes de escrever, ler em ordem:

**Banco de inteligência viral do cliente (se existir no ContextOS):**
- `negocios/<slug>/cerebro/areas/inteligencia/contexto/` (posts/carrosséis que viralizaram,
  análise de padrões, rankings, benchmarks de referências do nicho).

Se o cliente não tiver banco de inteligência montado, seguir com o briefing e a voz
do cliente (passo 3). Os swipe files em `../coreai-copy-shared/swipe/` também servem de referência.

**O que extrair de cada post viral relevante ao tema atual:**
- Estrutura do hook (1a linha)
- Quantidade de linhas
- Onde fica o clímax
- Padrão de fechamento (assinatura / soco verbal / pergunta retórica)
- Número ou cicatriz específica que ancora
- Inimigo nomeado (categoria, comportamento, geração)
- Vocabulário assinatura
- Recursos retóricos (caixa alta, reticências, palavrão se cabe)

**Anti-transposição:** identificar o que NÃO copiar (idiossincrasias de Antonio/Nigro que não cabem no registro Imperial JT). Lista em `analise-padroes.md` seção 11.

### Passo 3 — Voz autoral do cliente
Carregar a voz do cliente do ContextOS:
- `businesses/<slug>/contexto.md` (resumo do negócio, vem em `sources` do gate `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>`)
- `negocios/<slug>/cerebro/areas/marketing/contexto/brand.yaml` (tom de voz em `voice_dna`; posicionamento e arquétipo em `brand_core`, `brand_essence`, `promises`)
- `negocios/<slug>/cerebro/areas/marketing/voice/` (se existir)
- Caminhos relativos à raiz do Context OS; arquivo ausente = lacuna declarada, nunca invenção.
- Materiais de voz registrados no ContextOS (livro, transcrições, system prompt do clone, etc.)

Identificar quais cenas/casos reais do cliente podem ancorar este conteúdo.

### Passo 4 — Cruzamento (síntese pré-escrita)
Antes de digitar a primeira palavra, responder por escrito (mentalmente ou em scratch):

1. **Briefing:** Headline X. Gancho X. Fechamento X. Ideia central tem 4 bullets X.
2. **Inteligência:** Posts virais sobre tema similar usam hook tipo Y, ritmo Z, fecham com W. Anti-transposição: não usar A, B, C.
3. **Ancoragem JT:** Vou usar caso real X (ex: Carmem cozinha café, projeto provedor Ravi, modelo Ferrari 6-8h). NÃO vou inventar B, C, D.
4. **Riscos identificados antes de escrever:** essa peça pode cair em armadilha X (ex: jargão de outra tribo, frase obscura sem contexto, autoelogio sem inimigo, palavra que não soa JT).

Só então escrever.

---

## Checklist pré-escrita (executar SEMPRE)

- [ ] Li o briefing original literal (headline, gancho, ideia central, fechamento)?
- [ ] Identifiquei 2-3 posts virais de Antonio/Nigro sobre tema similar?
- [ ] Extraí padrão de hook + padrão de fechamento que funcionou?
- [ ] Listei o que NÃO copiar (idiossincrasias incompatíveis com voz Imperial)?
- [ ] Defini que cenas/casos reais do JT vou ancorar (zero inventado)?
- [ ] Cruzei briefing + inteligência + voz JT em síntese clara antes de escrever?
- [ ] Avatar do JT confirmado (pai/empresário 35-50 brasileiro), não avatar do post viral original?

**Se qualquer item não checou, parar. Não escrever.**

---

## Anti-padrão comum (erros já cometidos)

1. **Inventar inimigo concreto pra dar imagem:** ex "cara que posta foto em Dubai". Se não está no briefing E não está em transcrição do JT, NÃO usar. Adaptar ao avatar real.

2. **Inventar cena (ex "Carmem leu contrato semana passada"):** se não foi confirmada pelo operador, NÃO usar. Pedir cena real ou tirar a ancoragem.

3. **Frase obscura sem contexto:** ex "esposa e amante na mesma mulher" sem ponte explicativa. Se a frase não se sustenta sozinha pra leitor cego, refazer.

4. **Pulo de assunto sem ponte:** ex "Antes dela eu tinha o coração guardado a sete chaves, porque perdi meu pai aos 16". O "porque" vincula coisas que não estão explicitamente conectadas. Refazer.

5. **Trazer adjetivo do dicionário IA:** ex "homem sólido". Típico de pensamento metafônico de IA. Trocar por descrição concreta (ex "homem que escolheu alguém").

6. **Pular consulta de inteligência e escrever direto:** todo o resto do pipeline cai por terra se passo 2 é pulado.

7. **Vocabulário proibido em copy Torriani (vai dando bordão):**
   - "vida solo" — JT fala "vida de solteiro" ou "vida sozinho"
   - "glamourizando" / "glamouriza" — palavra de outra tribo, JT não usa
   - "Dubai" como símbolo — outro avatar, não cabe no público JT (pai/empresário 35-50 BR)
   - "homem sólido" — adjetivo metafônico genérico, sem cena
   - Atualizar essa lista conforme aprender mais com o operador.

8. **Bordão "homem de verdade":** JT gosta de usar "homem de verdade" como assinatura recorrente. Em vez de adjetivo abstrato como oposto de "instável" / "frouxo" / "fraco", usar "homem de verdade". Ex: "Homem instável busca liberdade na solidão. Homem de verdade constrói liberdade no casamento."

---

## Onde grava aprendizados novos

Toda vez que o operador reprovar copy por algo não previsto, atualizar:
- Anti-padrão acima
- Regras JT-XX em `oraculo-torriani.md`
- Esse pipeline se for erro de processo

Versionar como `pre-escrita-torriani.md v2.0` etc.
