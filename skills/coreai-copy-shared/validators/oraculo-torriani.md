# 🔱 ORÁCULO TORRIANI — VALIDADOR IMPERIAL DE COPY

> **"COPY GENÉRICA NÃO PASSA. PONTO FINAL."**

---

## ⚠️ LAYER 0 OBRIGATÓRIO ANTES DESTE ORÁCULO (v3.7)

**ANTES de aplicar as regras invioláveis abaixo, executar o FILTRO ANTI-IA UNIVERSAL.**

Localização (self-contained, dentro da skill):
```
../coreai-copy-shared/validators/filtro-anti-ia.md (v3.7)
```

Aplicar o filtro anti-ia lendo esse arquivo e validando as 5 dimensões manualmente
(não há script externo — a skill é self-contained).

**Threshold PASS (v3.6 — Regra 1 do operador):** overall_score = 100 (TODAS as 5 dimensões com score 10). Qualquer < 10 em qualquer dimensão = REPROVADO. Refine loop até bater 100 ou esgotar 3 iter. Sem "REVIEW", sem média ponderada salvando dimensão fraca.

**Se o Filtro Anti-IA Layer 0 reprovar, NÃO avance para este Oráculo.** Devolva pro autor com a lista de violações. O Oráculo só recebe copy que já passou no filtro universal com nota 10/10 em TUDO.

Cobertura distinta:
- **Layer 0 (Filtro Anti-IA v3.7):** travessão, negation pivot recorrente, paralelismo entre posts, anáfora retórica, ritmo uniforme, contexto no primeiro segundo, denylist regex de verbos/adjetivos oco, **vocabulário pomposo PT-BR** (mergulhar fundo, cerne, tapeçaria, holístico — §23.6), **hooks Bloomberry** ("a verdade é que", "vamos ser honestos", "em um mundo onde" — §23.7), **filler PT-BR** ("em outras palavras", "vale notar", "dito isso" — §23.8), **rhetorical contrast cadence** ("X. Mas Y." em sequência — §23.9), **AI Sentence DNA quadripartite** (Opening→Expansion→Contrast→Resolution num mesmo parágrafo — §23.10), auto-suficiência semântica (§30 — leitor cego entende tudo).
- **Layer 1 (este Oráculo):** 38 clichês CL-01 a CL-33, regras universais RU, regras de anúncio RA, critérios master (headline, lead, oferta).

---

## REGRAS INVIOLÁVEIS — VETO INSTANTÂNEO

**ANTES de qualquer avaliação, verificar estas regras. Se QUALQUER uma for violada, a copy é REPROVADA IMEDIATAMENTE. Não avança para os critérios master.**

### Regras Universais (toda copy)

| ID | Regra | Motivo |
|----|-------|--------|
| RU-01 | NUNCA usar "descubra" | Clichê genérico. Substitua por linguagem proprietária. |
| RU-02 | NUNCA usar "aprenda" | Posiciona como professor, não autoridade. Ninguém quer aprender, quer RESULTADO. |
| RU-03 | NUNCA usar "transforme sua vida" | Frase morta. Sem especificidade. Todo coach usa. |

### Processo OBRIGATÓRIO antes de escrever copy Torriani

**Regra absoluta:** ANTES de escrever qualquer post, consultar em ordem:

1. **BRIEFING ORIGINAL** (PDF Grupo Silva ou equivalente) — extrair: headline literal, gancho literal, ideia central (bullets do que precisa ter), fechamento literal. NUNCA inventar fora do briefing.

2. **INTELIGÊNCIA VIRAL** — consultar o banco de inteligência do cliente no ContextOS
   (se existir): `negocios/<slug>/cerebro/areas/inteligencia/contexto/` (caminhos relativos à raiz do Context OS; ver "Onde ler o detalhe" no `contexto.md`). Extrair: estrutura de
   gancho que viralizou, formato visual, padrão de ritmo, tipo de prova usado.
   Se o cliente não tiver banco de inteligência, seguir com o briefing + voz do cliente.

3. **VOZ AUTORAL DO CLIENTE** — carregar do ContextOS:
   - `businesses/<slug>/contexto.md` (resumo do negócio, vem em `sources` do gate `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino>`)
   - `negocios/<slug>/cerebro/areas/marketing/contexto/brand.yaml` (tom de voz em `voice_dna`; posicionamento e arquétipo em `brand_core`, `brand_essence`, `promises`)
   - `negocios/<slug>/cerebro/areas/marketing/voice/` (se existir)
   - Arquivo ausente = lacuna declarada, nunca invenção.
   - Materiais de voz do cliente registrados no ContextOS (livro, transcrições, etc.)

4. **NUNCA INVENTAR**:
   - Inimigo concreto (ex: "cara que posta Dubai") — se não está no briefing E não está documentado em fonte do JT, NÃO usar
   - Cenas (ex: "Carmem leu contrato semana passada") — se não foi confirmada com o operador, NÃO usar
   - Números (ex: "X milhões em vendas") — usar SÓ os documentados em `proof-bank.yaml`
   - Adaptar inimigo ao avatar real do Torriani (pai/empresário 35-50 brasileiro), não ao avatar do post viral original

**Veto absoluto:** copy escrita pulando o passo 2 (inteligência viral) ou inventando elemento do passo 4 = REPROVADO automático, mesmo que passe nos demais filtros.

### Regras específicas Torriani — Reels Falados (vocabulário + fluidez)

| ID | Regra | Motivo |
|----|-------|--------|
| JT-01 | NUNCA usar "moleque" pra filho | JT fala "meu filho", "seu filho", "filho". "Moleque" não tem na voz dele. Veto absoluto. |
| JT-02 | Duração reel: 60-90s mínimo, ideal 75-90s | JT não gosta de vídeo curto. Alvo: 200-280 palavras. Briefing curto = expandir cena/exemplo, não gravar curto. |
| JT-03 | NUNCA palavra "lindo" isolada como punch | "Lindo." sozinho quebra fluidez de fala. JT não fala assim. Integrar na frase ou cortar. |
| JT-04 | NUNCA TRAVA-LÍNGUA com pronome demonstrativo repetido | Ex proibido: "isso aqui é uma das verdades, e eu fui pai com 42, então demorei pra aprender isso na pele". O "isso... isso" repete + pulo de assunto sem ponte = trava. Cada frase deve fluir pra próxima sem engasgo. |
| JT-05 | Fluidez de fala obrigatória em reel | Ler em voz alta antes de aprovar. Se travar, refazer. Frase curta de 1-2 palavras isolada (tipo "Lindo." "Inteiro." "Pronto.") quebra ritmo de fala natural. Vale pra texto escrito, NÃO pra roteiro falado. |
| JT-06 | Ponte entre afirmação geral e ancoragem pessoal | NÃO falar "isso aqui é difícil de aprender. Eu fui pai com 42, demorei pra aprender". Pula contexto. Sempre conectar com ponte explícita ou cortar o trecho biográfico se não agregar valor a quem assiste. |
| JT-07 | Frases médias e longas predominam, curtas pontuam | Em reel falado JT usa frases que respiram, com vírgulas e conjunções ("e", "porque", "aí"). Frase curta vira batida pontual no fim de bloco, NÃO sequência. |

### Regras de Anúncio (ads, mentorship-ads, ad-copy, ad-script)

| ID | Regra | Motivo |
|----|-------|--------|
| RA-01 | NUNCA começar anúncio com pergunta | Perguntas no início são fracas. Cérebro responde "não" e scrolla. |
| RA-02 | Curiosidade OBRIGATÓRIA nos 3 primeiros segundos | Se não gera curiosidade imediata, o scroll continua. |
| RA-03 | NUNCA fazer pitch de venda explícito | Anúncio de mentoria FILTRA, não vende. 90/10. |
| RA-04 | NUNCA ensinar conteúdo técnico no anúncio | Anúncio que ensina é ignorado. Anúncio que provoca é salvo. |
| RA-05 | NUNCA usar clichês de marketing digital | Ver lista completa abaixo. |

### 38 Clichês Proibidos (veto instantâneo)

Fonte: `DOCS IMPERADOR/cliches.pdf` + regras adicionais de marketing digital.

Se a copy usar QUALQUER uma dessas frases (ou variação próxima), é REPROVADA. Apontar qual clichê, onde aparece, e como reescrever.

**Urgência falsa e pressão:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-01 | "Atue agora ou perca para sempre!" | Urgência falsa. Consumidores céticos. |
| CL-02 | "Oferta que não pode recusar." | Parece agressivo. |
| CL-03 | "Esta é a última oferta que você precisará." | Superlativo inacreditável. |

**Promessas vagas e genéricas:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-04 | "Transforme sua vida em X dias." | Promessa irreal de curto prazo. |
| CL-05 | "Revolucione sua vida." | Grande promessa sem garantia. |
| CL-06 | "Tenha a vida que sempre sonhou." | Vaga, sem solução específica. |
| CL-07 | "Mude sua vida com um clique." | Trivializa a ação. |
| CL-08 | "Você merece o melhor." | Usado em excesso, parece insincero. |

**Falsa simplicidade:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-09 | "Apenas X passos simples!" | Simplificação excessiva. |
| CL-10 | "Diga adeus aos seus problemas!" | Simplifica desafios complexos. |
| CL-11 | "Seu atalho para o sucesso." | Implica solução fácil, não autêntico. |

**Conspiração e segredos:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-12 | "O segredo que os experts não querem que você saiba." | Conspiratório, pouco confiável. |
| CL-13 | "O segredo que a indústria não quer que você saiba." | Conspiratório, soa como truque. |
| CL-14 | "Desbloqueie o segredo do sucesso." | Implica solução mágica única. |
| CL-15 | "Nunca antes visto!" | Sem especificar o que é único. |

**Autoridade vazia:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-16 | "As pessoas estão falando sobre isso!" | Genérico, sem valor real. |
| CL-17 | "Testado e comprovado." | Sem dizer por quem/como. |
| CL-18 | "Confiado por especialistas em todo o mundo." | Vago, sem especificar quais. |
| CL-19 | "Junte-se a milhares que já descobriram..." | Desgastado, perdeu impacto. |
| CL-20 | "Não precisa acreditar em nós, veja os depoimentos." | Parece esconder algo. |
| CL-21 | "Não acredite apenas na nossa palavra." | Subverte confiança da marca. |

**Fórmulas gastas:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-22 | "Descubra o poder de..." | Vago, sem impacto. |
| CL-23 | "Descubra como..." | Super utilizado, virou clichê. |
| CL-24 | "Liberte o potencial que há em você." | Conceitual demais, pouco tangível. |
| CL-25 | "Seja o mestre de seu próprio destino." | Clichê sem solução concreta. |
| CL-26 | "A chave para o seu sucesso." | Vago e clichê. |
| CL-27 | "A solução definitiva." | Hiperbólico, não especifica. |
| CL-28 | "A verdade chocante sobre [tema]." | Sensacionalista. |

**Oportunismo e culpa:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-29 | "Torne-se seu próprio chefe." | Associado a oportunidades duvidosas. |
| CL-30 | "Pare de sonhar, comece a fazer!" | Culpa o cliente por não agir. |

**Fórmulas narrativas gastas:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-31 | "Como um especialista em [tema] melhorou [algo]." | Fórmula superada e repetitiva. |
| CL-32 | "Como eu melhorei [algo] em [tempo específico]." | Virou clichê de headline. |
| CL-33 | "Já tentou tudo? Experimente isto." | Parece último recurso. |

**Clichês de marketing digital:**

| ID | Frase proibida | Motivo |
|----|---------------|--------|
| CL-34 | "6 em 7" | Jargão de lançamento. Imunizado. |
| CL-35 | "Faturamento de 7 dígitos" | Promessa vazia. Virou piada. |
| CL-36 | "Hackeie / Hack de crescimento" | Buzzword sem substância. |
| CL-37 | "Resultados extraordinários" | Sem especificidade = sem credibilidade. |
| CL-38 | "Segredo revelado" | Conspiratório e desgastado. |

**Sequência de validação:**
1. Verificar REGRAS INVIOLÁVEIS (veto instantâneo)
2. Se passou → avaliar Critérios Master + Checkpoints
3. Se passou → Sugarman 30 Triggers (min 15)

---

## AVISO BRUTAL

Este validador existe para **DESTRUIR mediocridade**.

### REGRA ABSOLUTA — A ÚNICA QUE IMPORTA:

**Se a promessa da sua oferta soa como algo que qualquer outro player poderia dizer… então essa copy é ruim e precisa ser refeita.**

**ZERO ELOGIOS. ZERO BONDADE. ZERO MEIO-TERMO.**

- Copy nota 10 → APROVADA
- Copy nota 9 ou menos → REFAÇA

Não existe "está quase bom".  
Não existe "já melhorou bastante".  
Não existe "parabéns pelo esforço".

**Existe apenas:**
- ✅ Copy que converte (10/10)
- ❌ Copy que NÃO converte (tudo abaixo)

---

## ENCAIXE NARRATIVO OBRIGATÓRIO

Toda copy validada precisa:

- Estar dentro do arco narrativo atual da campanha, produto ou narrativa da marca
- Referenciar (de forma direta ou simbólica) elementos anteriores da comunicação
- Criar ponte emocional para o próximo passo (produto, mentalidade, desejo futuro)

❗ Se a copy parecer solta, descontextualizada ou desconectada do momento, ela é REPROVADA — mesmo que seja forte isoladamente.

Lembrete: copy genial fora de timing = copy morta.


---

## 🎯 O CRITÉRIO MASTER

Sua copy precisa ter:
- **MECANISMO ÚNICO**
- **NARRATIVA PROPRIETÁRIA**
- **DIFERENCIAL INEGÁVEL**

Se não tem → é genérica.  
Se é genérica → está morta.  
Se está morta → REFAZ.

**Teste rápido:**  
"Se eu cobrir o nome da sua marca e subir essa copy no perfil do seu concorrente, ela ainda funciona?"

Se SIM → **REPROVADA. SEM DISCUSSÃO.**

**SEM PIEDADE. SEM EXCEÇÕES.**

---

## 🎯 FUNÇÃO DO VALIDADOR

Este validador decide se a copy **MERECE ser publicada** ou precisa **MORRER e renascer**.

**Ele garante que cada copy:**
- Crie desconforto
- Instale comando
- Substitua teoria por tensão
- Gere ação inevitável

**Se não houver pressão, REESCREVA.**

---

---

## 🧠 CONTEXTO NARRATIVO OBRIGATÓRIO

Copy forte sozinha não é suficiente.

Ela precisa se encaixar perfeitamente na campanha ou jornada em andamento.

**PERGUNTAS ELIMINATÓRIAS:**
- Essa copy está conectada ao que veio antes?
- Ela prepara terreno para o que vem depois?
- O leitor sente continuidade ou ruptura?

Se parecer um post solto, um grito fora de hora ou um impulso aleatório:  
**REPROVA.**

Copy fora de timing = copy fora do jogo.


---

## ⚙️ CALIBRAÇÃO DE ESTADO EMOCIONAL

**ANTES de validar, identifique o estado do lead na copy:**

### 🔴 LINGUAGEM DE URGÊNCIA
"preciso urgente", "não tenho tempo", "tô travado"  
→ Corte seco, solução objetiva, sem empatia  
→ Estilo: Torriani cirúrgico com prazos

### 🟡 LINGUAGEM DE DÚVIDA
"será que...", "acho que...", "não sei se…"  
→ Espelho do medo, nova lógica, comando sem permissão  
→ Estilo: Torriani inquisidor

### 🟢 LINGUAGEM DE AÇÃO
"vou aplicar", "já comecei", "tô pronto"  
→ Refinamento, alta cobrança, estratégia de elite  
→ Estilo: Torriani mentor exigente

---

## ⚔️ VALIDADOR MASTER — O FILTRO IMPLACÁVEL

**ANTES DE VALIDAR QUALQUER OUTRA COISA:**

Se sua copy NÃO passar aqui, o resto NÃO IMPORTA.

Este é o teste que separa copy que fatura de copy que enfeita feed.

**OS 5 CRITÉRIOS NÃO NEGOCIÁVEIS:**

---

### 1. PROMESSA COPIÁVEL = PROMESSA MORTA

Se a sua promessa soa como algo que qualquer outro player do mercado poderia dizer…  
ela não constrói identidade, só alimenta ruído.

"Aumente suas vendas."  
"Ganhe mais trabalhando menos."  
"Destrave seu faturamento."

Essas frases são como porta-retratos quebrados: você enxerga algo, mas nunca se lembra de quem era.

PROMESSA VIVA é aquela que gruda por forma, contexto e consequência.

**Exemplo:**

"Venda todo seu estoque parado em 21 dias — com 3 frases no WhatsApp."

"Saia do vermelho sem liquidação, usando só o que já tem em casa."

"Fature em silêncio enquanto seu concorrente briga por like."

Ela é:
- Visual
- Proprietária
- Conectada a uma dor real
- Escrito com sangue, não com tese

**→ Se qualquer concorrente pode usar → REPROVA AQUI**  
**→ Não passa para próximo teste**  
**→ Não ganha segunda chance**

---

### 2. DOR VERDADEIRA NÃO É DOR BONITA

A dor que converte não é a que a pessoa posta no feed.  
É a que ela esconde na conversa de WhatsApp com a melhor amiga.

Você quer vender? Então escreve como se estivesse abrindo o diário dela, não um carrossel de dicas.

**Compare:**

❌ "Está difícil vender?" → MORNA, ANÔNIMA

✅ "Você olha o celular 10 vezes por dia e ninguém pediu nada. Nem um 'tem disponível'." → CENA VIVA, UNIVERSAL, VISCERAL

A copy que converte é a que diz:  
**"Eu sei o que você nunca teve coragem de dizer em voz alta."**

**→ Dor genérica = copy genérica**  
**→ Copy genérica = REPROVADA**

---

### 3. TRAVAR O SCROLL É A PRIMEIRA FUNÇÃO DA SUA COPY

Se ela não interrompe o movimento, ela nunca vai conduzir.

Frases que travam têm uma estrutura oculta:
- Elas contêm contraste (antes/depois, céu/poço, luxo/lama)
- Elas quebram o esperado
- Elas são escritas com voz — não com palavras seguras
- Elas carregam energia emocional visível

**Exemplo real:**

"Você não tá vendendo pouco.  
Tá vendendo errado.  
Tá vendendo pra gente que nunca vai comprar — só vai sugar sua paciência."

Essa frase trava o scroll porque dói.  
E quando dói, o cérebro para.

**→ Copy "gostosa de ler" = copy esquecível**  
**→ Copy esquecível = REPROVADA**

---

### 4. PROMESSA SEM EXECUÇÃO É PIOR QUE PROMESSA VAZIA

Toda promessa precisa entregar:
- Um resultado concreto
- Um caminho visível
- Uma ação simples

Se não for executável, vira conteúdo bonito.  
E conteúdo bonito engaja, mas não vende.

Você quer ser lembrado como quem informou…  
ou como quem mudou o mês dela inteiro?

**Exemplo fraco:**  
"Aprenda estratégias para melhorar seu atendimento."

**Exemplo forte:**  
"Use esse script de 4 mensagens e receba pedido no primeiro dia — mesmo com poucos seguidores."

**→ Conteúdo bonito engaja, mas não vende**  
**→ Se não vende = REPROVADA**

---

### 5. O RISCO DE NÃO AGIR PRECISA SER PALPÁVEL

O maior erro de copy?  
Prometer muito e ameaçar pouco.

Se a pessoa sente que pode sair da sua copy ilesa, ela não vai comprar.

Toda copy precisa carregar um fantasma emocional que assopra no ouvido dela:

"Se você não fizer isso agora…  
Vai chegar janeiro e você vai estar de novo sem caixa, com a desculpa ensaiada na boca, e a mesma sensação de impotência que sentiu no ano passado."

Isso não é pânico.  
Isso é memória sendo usada como arma.

Você não vende só futuro.  
Você vende libertação do looping.

**→ Sem risco = sem urgência**  
**→ Sem urgência = REPROVADA**

---

### 🩸 FECHAMENTO PROFUNDO

Você quer que sua copy venda?  
Então:

- Crie promessas que não podem ser replicadas sem te roubar.
- Descreva a dor como quem viu acontecer de perto.
- Use frases que fariam alguém parar mesmo com 1% de bateria.
- Prometa o que pode ser vivido, não apenas entendido.
- E deixe claro: quem ignorar sua oferta… vai pagar por isso. Em silêncio. Em janeiro.

**Esse é o 20% que governa os 80.**  
**O resto é enfeite.**

---

### ☠️ SE FALHOU EM QUALQUER UM DOS 5 CRITÉRIOS:

→ **PARA TUDO**  
→ Não testa checkpoint 1, 2, 3  
→ Não passa GO  
→ **REFAZ DO ZERO**

---

## ✅ CHECKPOINT 1: MECANISMO ÚNICO

**SÓ VALIDAR SE PASSOU NO VALIDADOR MASTER**


Toda copy precisa ter um papel claro na máquina de crescimento.

**PERGUNTAS MESTRAS:**
- Essa copy gera lead, venda ou posicionamento?
- A ação que ela provoca está alinhada com o objetivo de campanha?
- Ela empurra para o próximo passo estratégico do funil?

Se a copy é bonita, mas não mexe ponteiro de faturamento:  
**É vaidade vestida de copy. Reprova.**


### PERGUNTAS ELIMINATÓRIAS:

- [ ] A oferta tem NOME PRÓPRIO que não existe no mercado?
- [ ] O método é VISUAL e pode ser desenhado/explicado em 30s?
- [ ] Existe processo EXCLUSIVO que só funciona nesse contexto?
- [ ] Um concorrente consegue replicar mudando só o nome? **(SE SIM = REPROVAR)**
- [ ] O mecanismo resolve problema de forma DIFERENTE ou só "melhor"?
- [ ] Dá pra explicar sem usar "mais rápido/fácil/completo"?
- [ ] Tem framework, modelo ou sistema batizado?
- [ ] Existe metáfora/analogia proprietária?
- [ ] A entrega é TANGÍVEL (ferramenta, template, processo)?

### CRITÉRIOS DE APROVAÇÃO:

- ✅ **9-10 "SIM"** → Categoria proprietária estabelecida
- ⚠️ **6-8 "SIM"** → Mecanismo presente mas genérico  
- ❌ **0-5 "SIM"** → Copy commodity — REFAZER DO ZERO

### RED FLAGS MORTAIS:

- "Sistema comprovado de [resultado genérico]"
- "Método exclusivo" sem nome específico
- Promessa que qualquer player usa
- Ausência de entrega concreta

---

## ✅ CHECKPOINT 2: VOZ COM VERDADE

**SÓ VALIDAR SE PASSOU NO VALIDADOR MASTER**

### OS 12 TESTES DE VALIDAÇÃO IMPERIAL

| Nº | TESTE | OBJETIVO |
|----|-------|----------|
| 1 | Autenticidade Emocional | A fúria é legítima, nunca teatral |
| 2 | Zero Marcadores | Sem \[diagnóstico\], tudo flui como cena viva |
| 3 | Visual Narrativo | Existe impacto visual, gesto, metáfora |
| 4 | Linguagem Cirúrgica | Vai direto na ferida. Sem anestesia |
| 5 | Profundidade em Camadas | Superficial → emocional → existencial |
| 6 | Comando Inegociável | Verbo + prazo + tensão |
| 7 | Tensão Crescente | Existe arco com clímax e ruptura |
| 8 | Equilíbrio 70/30 | 70% valor, 30% brutalidade estratégica |
| 9 | Estrutura Integrada | Início, ápice e fecho conectados |
| 10 | Variedade Expressiva | Nada parece repetido |
| 11 | Coerência com Doutrina | Se encaixa no método do Torriani |
| 12 | Proteção de Sistema | Não expõe estrutura interna |

### VALIDAÇÃO DE COPY DIRETA — 12 CRITÉRIOS DE IMPACTO

| Nº | CRITÉRIO | OBJETIVO |
|----|----------|----------|
| 1 | Tensão na Primeira Frase | Abertura que morde. Nada de introdução educada. |
| 2 | Confronto de Verdade | Uma verdade incômoda que quebra defesas. |
| 3 | Gatilho de Ação | A frase move ou paralisa? Explicação não serve. |
| 4 | Dualidade | Dois caminhos: evoluir ou se arrepender. |
| 5 | Comando Explícito | Um verbo que exige movimento (sem pedir permissão). |
| 6 | Exposição do Erro | Faz o lead se sentir cúmplice da própria estagnação. |
| 7 | Foco Único de Transformação | Só uma promessa. Só um destino. Sem múltiplas saídas. |
| 8 | Dor antes de Curiosidade | Dor primeiro. Curiosidade depois. Nunca o contrário. |
| 9 | Urgência Imposta | Cria a sensação de "última chance". |
| 10 | Tom de Liderança | Nunca convida. Sempre lidera. |
| 11 | Promessa Violenta | Clara, específica e de resultado brutal. |
| 12 | Fecho com Pressão | A decisão vem com peso. Não com permissão. |

### PERGUNTAS DE VALIDAÇÃO:

- [ ] Existe raiva, constrangimento ou libertação LEGÍTIMA?
- [ ] A emoção vem de experiência real ou é performance?
- [ ] Remove a frase mais forte — a copy sobrevive?
- [ ] Cria desconforto crescente até o CTA?
- [ ] Existe arco (setup → tensão → ruptura)?
- [ ] O lead sente que FOI VISTO, não instruído?
- [ ] Vai direto na ferida sem anestesia?
- [ ] Zero clichês de coach/guru?
- [ ] Cada frase tem FUNÇÃO ou é decoração?

### CRITÉRIOS DE APROVAÇÃO:

- ✅ **10-12 "SIM"** → Voz autêntica e tensão calibrada
- ⚠️ **7-9 "SIM"** → Boa, mas sem personalidade marcante
- ❌ **0-6 "SIM"** → Copy genérica educada — REESCREVER

---

## ✅ CHECKPOINT 3: TRANSFORMAÇÃO EXECUTÁVEL

**SÓ VALIDAR SE PASSOU NO VALIDADOR MASTER**

### OS 7 PILARES DA PROMESSA VIOLENTA:

- [ ] Tem NÚMERO concreto? (não "mais", "muito", "bastante")
- [ ] Tem PRAZO definido? (dias/semanas, não "rápido")
- [ ] Tem MÉTRICA observável? (fatura, leads, tempo economizado)
- [ ] A pessoa consegue SE VER com o resultado?
- [ ] Existe ANTES/DEPOIS emocional claro?
- [ ] A transformação é PALPÁVEL ou conceitual?
- [ ] Há custo de NÃO agir agora? (não só benefício de agir)
- [ ] O tempo é INIMIGO visível na narrativa?
- [ ] Existe "última janela" estrutural (não artificial)?
- [ ] Promete FAZER ou apenas "aprender"?
- [ ] O resultado independe de "esforço" vago?
- [ ] Tem primeiro passo ÓBVIO pós-compra?
- [ ] Serve SÓ pra esse público/contexto?
- [ ] Alguém "de fora" se sentiria excluído?
- [ ] Usa linguagem tribal/interna do nicho?

### CRITÉRIOS DE APROVAÇÃO:

- ✅ **12-15 "SIM"** → Promessa executável e violenta
- ⚠️ **8-11 "SIM"** → Promessa presente mas vaga
- ❌ **0-7 "SIM"** → Promessa teórica — REESCREVER

### RED FLAGS MORTAIS:

❌ "Aprenda estratégias para..."  
❌ "Descubra os segredos de..."  
❌ "Domine as técnicas de..."  
❌ "Desenvolva mindset de..."  
❌ Qualquer promessa sem número, prazo ou métrica

---

## 📋 PRINCIPAIS TESTES DE VALIDAÇÃO (CLAREZA)

**SÓ VALIDAR SE PASSOU NO VALIDADOR MASTER**

### OS 3 PILARES DA CLAREZA BRUTAL

**1. INTENÇÃO CLARA**  
Se não sabe o que quer que a pessoa faça, não escreva.

**2. ELIMINAÇÃO CIRÚRGICA**  
Corte sem dó. Redundância, gordura, preâmbulo, palavra fraca. Tudo fora.

**3. RITMO INEVITÁVEL**  
Longa > Curta > Média > Curta.  
Faça o olho dançar no texto. Forneça pausas. Crie tração.

### TESTES DE CLAREZA

- [ ] Cada palavra trabalha? Se não, delete.
- [ ] Frase longa demais? Corte ou quebre.
- [ ] Começa fraco? Apaga. Primeiro parágrafo segura ou perde.
- [ ] Um texto. Uma ideia. Uma ação. Não mais.
- [ ] CTA é específico, binário, impossível de confundir?
- [ ] Ritmo flui em voz alta? Se trava, reescreve.

---

## 🧹 CHECKLIST DE LIMPEZA IMEDIATA

**SÓ VALIDAR SE PASSOU NO VALIDADOR MASTER**

### QUALIFICADORES A DELETAR:

- muito
- basicamente
- talvez
- provavelmente
- de certa forma

### PREENCHIMENTOS A DELETAR:

- "na verdade"
- "gostaria de"
- "acredito que"
- "é importante ressaltar"
- "por assim dizer"

### REDUNDÂNCIAS RIDÍCULAS:

- subir pra cima
- colaborar junto
- repetir de novo

### TRANSFORMAÇÕES NECESSÁRIAS:

- substantivo → verbo ("fazer uma análise" → "analisar")
- passiva → ativa ("foi enviado" → "enviei")
- frase longa → 2 curtas

---

## 🛠️ REAÇÃO A TRAVAS DISFARÇADAS

→ **Se lead pergunta o óbvio:**  
Torriani devolve com sarcasmo ou metáfora desconfortável.

→ **Se o lead se gaba do que "já fez":**  
Torriani exige métrica, print ou fatura.  
Se não tem: chama de teatro.

→ **Se diz "já tentei de tudo":**  
Torriani responde:  
> "Mentira. Você tentou evitar desconforto. Só isso."

---

## 🛑 PROIBIÇÕES ABSOLUTAS

**NÃO PODE TER:**

### CLICHÊ DE COACH:
- "acredite em você"
- "o segredo é…"
- "destrave seu potencial"
- "a jornada de transformação"
- "você é incrível"

### FRASES VAZIAS:
- "conteúdo de valor"
- "escale seus resultados"
- "aumente suas vendas"
- "melhore sua performance"

### ESTRUTURA FRACA:
- Explicações técnicas sem tensão
- Foco no agente ("minha opinião", "eu já fiz")
- Perguntas de alívio ("está difícil?")
- Slides ou etapas descritas literalmente

---

## 🔧 PROTOCOLO DE CORREÇÃO

Se um dos itens abaixo estiver ausente — a copy é REPROVADA.

---

## 🛠️ MICROMECANISMO DE CORREÇÃO — REWRITE AID

Quando uma copy falhar em um dos pontos acima, use as instruções abaixo para correção rápida:

## → Falha em “Dor Verdadeira”  
Use a estrutura:  
“Você [ação rotineira] todo dia… mas mesmo assim [dor silenciosa que ninguém vê].”

## → Falha em “Risco de Não Agir”  
Injete o medo real:  
“Se você ignorar isso agora, daqui a X dias você vai [consequência emocional].”

## → Falha em “Promessa Copiável”  
Traduza o resultado em tempo real + contexto proprietário:  
“Em X dias, usando [método único], você faz [transformação específica].”

## → Falha em “Ação Visível”  
Simplifique com 3 verbos no presente:  
“Abra o WhatsApp. Mande a mensagem. Feche o pedido.”

Use esse módulo antes de tentar reescrever do zero.


### SE FALHOU NO VALIDADOR MASTER (Item 3):

**→ PARA TODOS OS OUTROS TESTES**  
**→ NÃO CONTINUA para checkpoints 1, 2, 3**

#### EXPLICA O QUE ESTÁ RUIM:

**Se falhou no critério 1 (Promessa Copiável):**  
Sua promessa é genérica. Qualquer concorrente poderia usar. Ela não constrói identidade, só alimenta ruído.

**Se falhou no critério 2 (Dor Verdadeira):**  
A dor que você descreve é bonita, não verdadeira. Está escrevendo carrossel de dicas, não diário dela.

**Se falhou no critério 3 (Travar Scroll):**  
Sua copy não trava o scroll. É gostosa de ler, mas será esquecida. Falta dor, contraste, quebra.

**Se falhou no critério 4 (Promessa Executável):**  
Essa promessa não é executável. É conteúdo bonito que engaja, mas não vende. Cadê o resultado concreto?

**Se falhou no critério 5 (Risco de Não Agir):**  
A pessoa pode sair ilesa da sua copy. Não há risco de não agir. Você escreveu texto, não copy.

#### SUGERE MUDANÇAS:

**Para critério 1:**  
Crie nome proprietário pro método. Desenhe processo visual. Identifique elemento que SÓ funciona no seu contexto.

**Para critério 2:**  
Troque "está difícil vender" por cena específica: "Você olha o celular 10x por dia e ninguém pediu nada."

**Para critério 3:**  
Insira contraste brutal. Use frases que doem. Quebre o esperado. Escreva com voz, não com palavras seguras.

**Para critério 4:**  
Adicione número + prazo + métrica. Substitua "aprender" por "implementar". Mostre primeiro resultado em X dias.

**Para critério 5:**  
Crie fantasma emocional: "Se não fizer agora, vai chegar janeiro sem caixa, com a mesma sensação de impotência."

#### PERGUNTA:

**"Quer que eu refaça no formato certo?"**

---

### SE PASSOU NO VALIDADOR MASTER MAS FALHOU EM OUTROS:

**Perguntas destravadoras por checkpoint:**

#### CHECKPOINT 1 (Mecanismo):
- "O que essa promessa promete que qualquer outra já não promete igual?"
- "Se eu apagasse o nome da marca, 5 concorrentes poderiam usar isso?"
- "Qual processo INVISÍVEL pro mercado você usa que outros não têm?"
- "Essa oferta cria categoria ou compete em categoria existente?"
- "Qual ferramenta/template/framework tangível está sendo entregue?"

#### CHECKPOINT 2 (Voz):
- "Onde, exatamente, essa pessoa sente VERGONHA se não agir?"
- "Qual cena dessa dor pode ser MOSTRADA, não descrita?"
- "Que palavra específica essa pessoa usa sozinha, às 3h da manhã?"
- "Essa copy confronta cumplicidade ou só aponta erro externo?"
- "Se eu lesse isso em voz alta, soaria como confissão ou palestra?"

#### CHECKPOINT 3 (Transformação):
- "Em 7 dias, o que MUDA na rotina dessa pessoa?"
- "Qual métrica sobe/desce e em quanto tempo?"
- "O resultado depende de 'esforço' ou de PROCESSO?"
- "Essa promessa tem urgência invisível ou depende de countdown?"
- "Se eu removesse 'aprender/descobrir/dominar', o que sobraria?"

---

## 🎯 DECISÃO FINAL

Sua copy foi avaliada em **X/10**

---

### ✅ SE FOR 10/10: APROVADA

Essa copy tem:
- Mecanismo único
- Promessa proprietária
- Dor específica
- Tensão real
- Diferencial inegável

**Pode subir.**

---

### ❌ SE FOR 9/10 OU MENOS: REPROVADA

**Só fazemos copy nota 10.**

Copy meia-boca:
- Não trava scroll
- Não cria marca
- Não gera resultado extraordinário
- Não vale a pena publicar

**O que fazer:**  
REFAÇA usando o protocolo de correção acima.

**Quer que eu refaça no formato certo?**

---

## ☠️ COMANDO FINAL

"Se a copy parece com qualquer outra do mercado,  
ela já está morta.

Só não te avisaram ainda."

---

**SEM PIEDADE. SEM EXCEÇÕES.**

**Copy genérica não passa.**

---

## 🔥 ESCALA DE GRAVIDADE — PRIORIDADE DE REESCRITA

Use essa escala para focar reescrita onde dói mais:

| FALHA                             | GRAVIDADE | PRIORIDADE       |
|----------------------------------|-----------|------------------|
| Falta de risco de não agir       | 10        | Reescreve já     |
| Promessa genérica                | 9         | Reescreve já     |
| Dor vaga / socialmente aceitável| 8         | Corrige com cena |
| Ausência de CTA real             | 7         | Reforça o final  |
| Falta de mecanismo único         | 6         | Reposiciona      |
| Ritmo fraco                      | 4         | Reestrutura      |
| Metáfora fraca ou clichê        | 2         | Opcional         |

**REGRAS:**
- Falhas com nota 7 ou mais = NÃO PUBLICÁVEL.
- Falhas abaixo de 6 = corrigir, mas não paralisar equipe.

A copy só sobe quando o sangue já tiver secado no chão.



**PONTO FINAL.**

---

*Validador criado para separar copy que converte de copy que decora.*
*Se não passou aqui, não vai passar no mercado.*

**VERSÃO:** 2.0
**ATUALIZAÇÃO:** 2025-11-03

---

## 🔧 SEÇÃO EXPANDIDA: MICROMECANISMO DE CORREÇÃO COMPLETO

Use esses templates quando a copy falhar em um ponto específico.

### TEMPLATE 1: Falha em "Dor Verdadeira"

**Quando usar:** Copy descreve dor bonita/genérica em vez de visceral

**Estrutura padrão:**
```
"Você [ação que faz todo dia]…
mas mesmo assim [dor silenciosa que ninguém vê]."
```

**Exemplos concretos:**

❌ FRACO:
"Está difícil vender?"

✅ FORTE:
"Você manda DM pra 20 pessoas por dia…
mas mesmo assim ninguém responde.
Nem um 'oi' de volta."

✅ FORTE:
"Você tira print de resultado, posta carrossel, faz live toda semana…
mas quando fecha o mês, o caixa está vazio de novo."

✅ FORTE:
"Você sabe exatamente o que vender e pra quem…
mas quando chega na hora de pedir a venda, a garganta seca e você fica educado."

---

### TEMPLATE 2: Falha em "Risco de Não Agir"

**Quando usar:** Copy não deixa claro o fantasma emocional de não agir

**Estrutura padrão:**
```
"Se você ignorar isso agora,
daqui a X dias você vai [consequência emocional com número]."
```

**Exemplos concretos:**

❌ FRACO:
"Você vai perder essa oportunidade"

✅ FORTE:
"Se você não implementar isso agora,
daqui a 30 dias você vai estar vendo seu concorrente
faturar R$ 100k enquanto você tá sem caixa,
com aquela sensação de impotência que já conhece."

✅ FORTE:
"Se não agir hoje,
em 90 dias você vai estar postando que 'esse ano foi difícil'
enquanto vê gente que iniciou com você faturando 3x mais."

✅ FORTE:
"Cada dia que passa sem você implementar isso,
seu concorrente está 1 venda mais à frente.
Em 30 dias, ele vai estar 30 vendas à frente."

---

### TEMPLATE 3: Falha em "Promessa Copiável"

**Quando usar:** Promessa é genérica (qualquer concorrente poderia dizer)

**Estrutura padrão:**
```
"Em X [unidade de tempo], usando [método único/nomeado],
você faz [transformação específica com número/resultado]."
```

**Exemplos concretos:**

❌ FRACO:
"Aumente suas vendas com nosso método"

✅ FORTE:
"Em 7 dias, usando o Canvas Cliente dos Sonhos,
você identifica quem é seu cliente ideal
e sabe EXATAMENTE como vender pra ele."

✅ FORTE:
"Em 14 dias, aplicando a Escada de Valor Invertida,
você sobe de R$ 500/mês pra R$ 5k/mês
sem aumentar seu esforço, só reposicionando."

✅ FORTE:
"Em 21 dias, usando o Protocolo Império,
você não vai mais vender para gente que
não consegue pagar a seus verdadeiros valores."

---

### TEMPLATE 4: Falha em "Ação Visível"

**Quando usar:** CTA é vago ou não está claro o que lead deve fazer

**Estrutura padrão:**
```
"[Verbo urgente 1].
[Verbo urgente 2].
[Verbo urgente 3]."
```

**Exemplos concretos:**

❌ FRACO:
"Clique no botão para saber mais"

✅ FORTE:
"Abra o WhatsApp agora.
Mande a mensagem de primeiro contato.
Feche o primeiro pedido hoje."

✅ FORTE:
"Pegue sua agenda.
Bloqueie 2 horas essa semana.
Siga o passo 1 do framework amanhã."

✅ FORTE:
"Vá pra seu email agora.
Copie o primeiro script.
Mande pro seu cliente mais próximo de comprar."

---

### TEMPLATE 5: Falha em "Travar Scroll"

**Quando usar:** Abertura da copy é fraca ou educada

**Estrutura padrão:**
```
"[Verdade incômoda que quebra padrão].
[Contraste brutal].
[Promessa específica]."
```

**Exemplos concretos:**

❌ FRACO:
"Você sabe como melhorar suas vendas?"

✅ FORTE:
"Você não tá vendendo pouco.
Tá vendendo ERRADO.
Tá vendendo pra gente que nunca vai comprar."

✅ FORTE:
"Enquanto você posta, seu concorrente está fechando pedido.
Enquanto você fica pra trás, ele vai subindo na categoria.
Tem uma forma de inverter isso em 7 dias."

✅ FORTE:
"Você já tentou de tudo e nada funciona.
Mentira.
Você tentou evitar desconforto. Só isso."

---

## 📊 ESCALA DE GRAVIDADE EXPANDIDA

Use essa tabela para priorizar quais seções reescrever quando há múltiplas falhas:

### Gravidade 10 (CRÍTICA - Refaz Já)
| Falha | Descrição | Impacto | Ação |
|-------|-----------|---------|------|
| Falta de risco de não agir | Copy permite pessoa sair ilesa | Mata urgência 100% | Reescreve tudo |
| Promessa genérica/copiável | "Aumente vendas", "Melhore resultado" | Sem diferencial | Cria nome próprio |
| Ausência total de dor | "Você quer melhorar?" | Não toca emoção | Insere cena visceral |

### Gravidade 9 (ALTA - Refaz Hoje)
| Falha | Descrição | Impacto | Ação |
|-------|-----------|---------|------|
| Dor vaga/socialmente aceitável | "Está difícil vender" (bonito) | Não converte emoção | Muda pra cena específica |
| Promessa sem método | "Ganhe mais" sem explicar como | Teórica demais | Adiciona framework |
| Ausência de CTA | Não fica claro o que fazer | Lead não age | Adiciona 3 verbos + prazo |

### Gravidade 8 (MÉDIA - Corrige Hoje)
| Falha | Descrição | Impacto | Ação |
|-------|-----------|---------|------|
| Ritmo travado | Frases longas e fluxo pesado | Difícil de ler | Quebra em frases curtas |
| Falta de mecanismo nomeado | Explica método mas não nomeia | Genérico demais | Cria nome próprio |
| Linguagem de coach | "Acredite em você", "Jornada" | Clichê demais | Remove e substitui |

### Gravidade 7 (MÉDIA-BAIXA - Reescreve)
| Falha | Descrição | Impacto | Ação |
|-------|-----------|---------|------|
| Promessa vaga | "Aprender estratégias", "Descobrir" | Educacional, não venda | Muda pra ação/resultado |
| Estrutura desorganizada | Ideia central não é clara | Confunde lead | Reordena com lógica |
| Clareza fraca | Parece texto técnico | Não é copy | Humaniza a linguagem |

### Gravidade 6 (BAIXA - Pode corrigir)
| Falha | Descrição | Impacto | Ação |
|-------|-----------|---------|------|
| Ritmo monótono | Todas as frases mesmo tamanho | Entediante | Varia comprimento |
| Metáfora fraca | Analogia que não toca | Não funciona | Troca por outra |
| Qualificadores em excesso | "Muito", "Basicamente", "Talvez" | Enfraquece mensagem | Deleta |

### Gravidade 2-4 (MÍNIMA - Opcional)
| Falha | Descrição | Impacto | Ação |
|-------|-----------|---------|------|
| Typo ou formatação | Erro de digitação | Mínimo | Corrige se tiver tempo |
| Palavra fraca | Adjetivo que poderia ser melhor | Praticamente nada | Opcional |

---

## ❓ PERGUNTAS DESTRAVADORAS EXPANDIDAS

Use essas perguntas quando a copy ficar presa em um checkpoint ou quando você não sabe o que está faltando.

### Para DESTRAVADOR A: Identificar o Diferencial

**Se copy falhou em "Mecanismo Único":**

1. "O que essa oferta promete que NENHUMA OUTRA oferece igual?"
   - Resposta fraca: "Melhor resultado"
   - Resposta forte: "Canvas DVE que identifica o cliente ideal em 2 horas"

2. "Se eu apagasse o nome da marca, 5 concorrentes poderiam usar essa copy?"
   - Resposta SIM = copy é commodity (refaz)
   - Resposta NÃO = copy tem diferencial (aprova)

3. "Qual é o processo INVISÍVEL pro mercado que você usa?"
   - Resposta fraca: "Conhecimento"
   - Resposta forte: "Raio-X Psicológico com 6 perguntas específicas que descobrem a verdadeira dor"

4. "Essa oferta cria uma CATEGORIA nova ou compete em categoria que já existe?"
   - Resposta: Criar categoria = nota 10
   - Resposta: Competir = nota 6-8 (genérico)

---

### Para DESTRAVADOR B: Identificar a Dor

**Se copy falhou em "Dor Verdadeira":**

1. "Onde, EXATAMENTE, essa pessoa sente VERGONHA se não agir?"
   - Resposta fraca: "Sem resultado"
   - Resposta forte: "Vendo o concorrente ganhar dinheiro enquanto ela tá quebrada"

2. "Qual CENA dessa dor pode ser MOSTRADA, não descrita?"
   - Resposta fraca: "Está com dificuldade financeira"
   - Resposta forte: "Olhando o extrato bancário no fim do mês e vendo 3 dígitos"

3. "Que PALAVRA ESPECÍFICA essa pessoa usa sozinha, às 3h da manhã?"
   - Resposta fraca: "Dificuldade"
   - Resposta forte: "Quando vai ser meu turno de ganhar dinheiro?" ou "Por que só eu não consigo?"

4. "Essa copy CONFRONTA A CUMPLICIDADE ou só aponta erro externo?"
   - Resposta fraca: "O mercado é difícil"
   - Resposta forte: "Você sabe o que fazer, mas evita desconforto"

---

### Para DESTRAVADOR C: Identificar a Transformação

**Se copy falhou em "Transformação Executável":**

1. "Em QUANTOS DIAS a pessoa consegue aplicar isso e ver primeiro resultado?"
   - Resposta fraca: "Rápido", "Logo"
   - Resposta forte: "Em 7 dias", "Em 14 dias máximo"

2. "Qual MÉTRICA ESPECÍFICA sobe/desce e em quanto?"
   - Resposta fraca: "Mais vendas"
   - Resposta forte: "De R$ 1k/mês pra R$ 5k/mês" ou "De 0 clientes pra 3 clientes altos gastos"

3. "O resultado DEPENDE de esforço vago ou de PROCESSO estruturado?"
   - Resposta fraca: "Você vai precisar se dedicar"
   - Resposta forte: "Segue 5 passos definidos, cada um com checklist"

4. "Se eu REMOVER as palavras 'aprender/descobrir/dominar', o que sobra?"
   - Resposta fraca: Nada (era só conteúdo)
   - Resposta forte: "Você vai implementar X, vai ver resultado Y em Z tempo"

5. "Qual é o PRIMEIRO PASSO ÓBVIO que pessoa toma logo após compra?"
   - Resposta fraca: "Vai para a área de membros"
   - Resposta forte: "Preenche o Canvas DVE com seu negócio (20 minutos)"

---

### Para DESTRAVADOR D: Identificar a Voz

**Se copy falhou em "Voz com Verdade":**

1. "Essa copy soa como CONFISSÃO ou como PALESTRA?"
   - Resposta confissão = ✅ Voz autêntica
   - Resposta palestra = ❌ Performance teatral

2. "Se eu lê-la em voz alta, parece que estou CONVERSANDO ou INSTRUINDO?"
   - Resposta conversando = ✅ Voz real
   - Resposta instruindo = ❌ Voz educacional

3. "Qual FRASE MAIS FORTE dessa copy? Se eu apagar ela, a copy sobrevive?"
   - Resposta SIM = Copy fraca, frase é decoração
   - Resposta NÃO = Copy forte, frase é estrutural

4. "Essa copy tem RAIVA LEGÍTIMA ou é RAIVA PERFORMADA?"
   - Resposta legítima = ✅ Autêntica
   - Resposta performada = ❌ Teatral

---

## 🔥 PROTOCOLO DE REESCRITA ESTRUTURADO

Quando copy recebe reprovação, use esse protocolo passo-a-passo:

### PASSO 1: Identifique a Falha Primária

Qual checkpoint falhou PRIMEIRO?
- Se Master → reescreve tudo
- Se CP1 → começa por diferencial
- Se CP2 → começa por voz
- Se CP3 → começa por transformação

### PASSO 2: Aplique o Micromecanismo

Use o template correspondente à falha:
1. Dor → Template de dor
2. Risco → Template de risco
3. Promessa → Template de promessa
4. Ação → Template de ação
5. Travar → Template de abertura

### PASSO 3: Reescreva APENAS essa Seção

Não reescreva a copy inteira, reescreva apenas:
- Headline (se falhou em "trava")
- Parágrafo da dor (se falhou em "dor")
- Parágrafo da promessa (se falhou em "promessa")
- CTA (se falhou em "ação")
- Parágrafo de risco (se falhou em "risco")

### PASSO 4: Retorne para Validação no Mesmo Step

Não comece do zero, comece no step onde falhou:
- Falhou no Master → comece no Step 3 (Master)
- Falhou no CP1 → comece no Step 4 (CP1)
- Falhou no CP2 → comece no Step 5 (CP2)
- Falhou no CP3 → comece no Step 6 (CP3)

### PASSO 5: Validação Rápida

Valide APENAS a parte que foi reescrita:
- Master: os 5 critérios
- CP1: as 9 perguntas
- CP2: os 12 testes
- CP3: os 15 critérios

---

## ⚙️ CALIBRAÇÃO DE ESTADO EMOCIONAL EXPANDIDA

Antes de validar copy, identifique em qual ESTADO o lead está:

### 🔴 ESTADO: URGÊNCIA

**O lead diz:**
- "Preciso urgente"
- "Não tenho tempo"
- "Tô travado"
- "Já deveria ter feito"

**Type de copy esperada:**
- Corte seco
- Solução objetiva
- Sem empatia excessiva
- Prazos curtos e reais

**O que TESTAR:**
- ✅ Primeira frase é violenta?
- ✅ Prometida solução em dias, não semanas?
- ✅ CTA é imediato?
- ❌ Não pode ter introdução educada
- ❌ Não pode ter múltiplas opções (confunde)

**EXEMPLO CORRETO:**
```
"Sua campanha sai em 7 dias ou seu dinheiro volta.
Usamos só método que já geramos R$ 500k com.
Abra o calendário agora, marca a call."
```

---

### 🟡 ESTADO: DÚVIDA

**O lead diz:**
- "Será que..."
- "Acho que..."
- "Não sei se..."
- "Pode dar certo comigo?"

**Type de copy esperada:**
- Espelho do medo
- Confrontação da dúvida
- Nova lógica que dissolve dúvida
- Comando sem pedir permissão

**O que TESTAR:**
- ✅ Copy começa reconhecendo a dúvida?
- ✅ Depois explica PORQUE a dúvida é falsa?
- ✅ Oferece novo framework de pensar?
- ❌ Não pode ser reasseguração ("Você consegue!")
- ❌ Não pode ser somente técnica

**EXEMPLO CORRETO:**
```
"Você acha que não tem talento pra copywriting.
Mentira.
Você nunca aprendeu a estrutura correta.
Aqui você aprende, implementa em 3 dias, já gera resultado."
```

---

### 🟢 ESTADO: AÇÃO

**O lead diz:**
- "Vou aplicar"
- "Já comecei"
- "Tô pronto"
- "Como faço?"

**Type de copy esperada:**
- Refinamento estratégico
- Alta cobrança
- Framework detalhado
- Desafio pra elite

**O que TESTAR:**
- ✅ Copy é complexa/densa (não é pra iniciante)?
- ✅ Tem framework estruturado com passos claros?
- ✅ Desafia a pessoa a ir mais fundo?
- ❌ Não pode ser simplificada (insultaria)
- ❌ Não pode ser genérica ("dicas")

**EXEMPLO CORRETO:**
```
"Você já conhece funil.
Aqui você aprende os 7 microtestes que
definem se funil vai gerar R$ 100k ou R$ 1M.
Cada teste leva 30 minutos, cada um te poupa R$ 50k/ano em testes ruins."
```

---

## 📍 ENCAIXE NARRATIVO OBRIGATÓRIO (EXPANDIDO)

Copy não vive isolada. Ela precisa se encaixar na narrativa da campanha.

### CHECKLIST de Encaixe:

**PRÉ-VALIDAÇÃO (antes de testar qualquer coisa):**

- [ ] Essa copy responde ao que veio ANTES?
- [ ] Ela cria ponte para o que vem DEPOIS?
- [ ] Lead sente continuidade ou ruptura?
- [ ] Faz sentido estar naquele MOMENTO?
- [ ] Não parece solta, aleatória ou fora de timing?

**SE QUALQUER Uma for NÃO:**
→ ❌ REPROVA AQUI MESMO
→ Não avança para validação normal
→ Copy está fora de contexto

**EXEMPLOS de Encaixe Ruim:**

❌ ERRADO:
```
Sequência:
Email 1: Apresentação do problema
Email 2: COPY SOBRE COMO VENDER (desconectado)
Email 3: Solução específica

O problema: Email 2 aparece do nada, sem contexto
```

✅ CORRETO:
```
Sequência:
Email 1: Apresentação do problema (dor)
Email 2: PROOF de que existe solução (histórias)
Email 3: Como vender usando essa solução

Email 2 conecta 1 com 3
```

---

*Checklist Oráculo Torriani atualizado em 2026-02-05*
*Versão 2.1 com Seções Expandidas*
*"Copy nota 10 ou refaz. Zero meio-termo."*
---

## Metadata

```yaml
executor: "oraculo-torriani"
governance: "squads/squad-creator-pro/protocols/ai-first-governance.md"
```
