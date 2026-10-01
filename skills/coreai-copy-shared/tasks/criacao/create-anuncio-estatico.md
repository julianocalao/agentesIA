# Create Anúncio Estático, Padrão Torriani (4 blocos)

```yaml
task_id: create-anuncio-estatico
version: 2.0
framework: copy-framework-v2
category: paid_media
complexity: intermediate
estimated_time: 20-40min
agent_owner: copy-chief
executor: john-carlton
alternative_executor: gary-halbert
requires_research: false

theoretical_foundation:
  - John Carlton, Simple Writing System (hooks, copy conversacional)
  - Gary Halbert, abertura visceral e afirmação contraintuitiva
  - Meta Advantage+ / Andromeda, criativo como sinal de segmentação
  - Padrão Torriani, Anúncio Estático de 4 blocos (INSTRUÇÃO v2.0)

dependencies:
  instrucao_canonica: data/anuncios-estaticos/INSTRUCAO-LLM-anuncio-estatico.md
  template: templates/anuncio-estatico.md
  framework: frameworks/torriani/anuncios-mentoria.md
  checklist: checklists/oraculo-torriani.md
  headline_bank: swipe/headlines/_index.yaml
  data: negocios/<slug>/cerebro/empresa/contexto/evidencias/  # provas por cliente (relativo a <raiz>; ausente = lacuna)

tags: [anuncio, estatico, meta, instagram, facebook, imagem, feed, story]

pre_conditions:
  - "Premissa-core.md carregada"
  - "Cliente carregado (perfil, ICP, voice, positioning, products)"
  - "Faixa de preço confirmada"
  - "Temperatura do público confirmada (frio / morno / quente)"
  - "Nível de consciência (awareness) confirmado"
  - "Destino confirmado: diagnóstico ou aplicação"
  - "Proof-bank disponível (todo número sai dele)"
  - "swipe/headlines/_index.yaml acessível (headline bank canônico)"

veto_conditions:
  - "VETO RA-01: Headline começa com pergunta -> REWRITE"
  - "VETO RA-02: Sem curiosidade nos 3 primeiros segundos -> REWRITE"
  - "VETO RA-03: Pitch de venda explícito -> REWRITE"
  - "VETO RA-04: Ensina conteúdo técnico -> REWRITE"
  - "VETO RA-05: Usa clichê de marketing digital (CL-01 a CL-38) -> REWRITE"
  - "VETO RH-01: Headline com ponto (são duas frases) -> REWRITE"
  - "VETO RH-02: Corpo com mais de 1 ponto por frase longa (texto picado) -> REWRITE"
  - "VETO RH-03: Headline em forma de pergunta -> REWRITE"
  - "VETO RH-04: Headline inventada, sem fórmula clonada declarada -> REWRITE"
  - "VETO BANK-01: Fórmula declarada sem citar o id da headline do _index.yaml -> REWRITE"
  - "VETO BANK-02: Clone de tier B ou C sem a declaração obrigatória de tier -> REWRITE"
  - "VETO: Headline acima de 15 palavras -> REWRITE"
  - "VETO: Corpo acima de 45 palavras -> REWRITE"
  - "VETO: Transição acima de 20 palavras -> REWRITE"
  - "VETO: Transição continua argumentando em vez de só convidar -> REWRITE"
  - "VETO: Peça não nomeia nenhuma coisa concreta e reconhecível -> REWRITE"
  - "VETO: Número que não existe no proof-bank -> BLOCK"
  - "VETO: Preço da oferta aparece na peça -> BLOCK"
  - "VETO: Palavra da lista de banidos na copy -> REWRITE"
  - "VETO: Palavra em inglês na copy -> REWRITE"
  - "VETO: CTA genérico tipo 'saiba mais' -> REWRITE"
  - "VETO: Emoji ou travessão na peça -> REWRITE"
```

---

## Task Anatomy

| Campo | Valor |
|-------|-------|
| Fonte de verdade | `data/anuncios-estaticos/INSTRUCAO-LLM-anuncio-estatico.md` (v2.0) |
| Executor padrão | john-carlton |
| Executor alternativo | gary-halbert |
| Validadores | filtro anti-IA (`validate-anti-ia.sh`) + oráculo Torriani (`oraculo-precheck.sh`) |
| Banco de headlines | `swipe/headlines/_index.yaml` (244 headlines, tiers A/B/C) |
| Entregável | Arquivo markdown com lote de peças numeradas por eixo |

---

## Purpose

Criar anúncios estáticos no padrão Torriani de **4 blocos**: HEADLINE, CORPO, TRANSIÇÃO e CTA, mais o ÂNGULO como rótulo interno.

Cada bloco tem função única e limite de palavras. Cada anúncio tem que ser entendido na leitura, sem a pessoa precisar deduzir nada. O anúncio não vende, ele para o scroll e filtra.

Este é o formato oficial de todo anúncio para imagem estática (feed 1080x1080 e story 1080x1920).

---

## Executor

**John Carlton** (`agents/tier-2-executores/john-carlton.md`) escreve por padrão. Simple Writing System, hooks, copy conversacional e agressiva.

**Gary Halbert** (`agents/tier-2-executores/gary-halbert.md`) é a alternativa quando o ângulo pede abertura mais visceral.

**Copy Chief** faz a triagem antes e o roteamento. **Oráculo Torriani** valida no fim.

---

## O ERRO MAIS CARO

Escrever a copy direto, sem carregar a persona de um copywriter real e sem clonar estrutura validada de swipe.

O texto sai com fingerprint de máquina: negation pivot repetido, tríade mecânica, paralelismo simétrico, headline picada em duas frases. Passa em leitura rápida e falha no ouvido.

**Se você não consegue dizer qual copywriter escreveu e qual fórmula foi clonada, a peça está reprovada.**

---

## Estrutura obrigatória (4 blocos)

Carregar `templates/anuncio-estatico.md` antes de escrever. Formato:

```
ÂNGULO:     {CONCEITO EM CAIXA ALTA, rótulo interno, não vai na arte}
HEADLINE:   {frase única, ZERO ponto, até 15 palavras}
CORPO:      {confirma a headline e entrega o benefício concreto, até 45 palavras}
TRANSIÇÃO:  {só o convite, até 20 palavras}
CTA:        {o clique}
```

| Bloco | Limite | Função | Erro comum |
|-------|--------|--------|------------|
| ÂNGULO | caixa alta, sem limite | Conceito-mãe. Rótulo interno, não vai na arte | Confundir com headline |
| HEADLINE | até 15 palavras | Parar o scroll com uma afirmação | Virar duas frases com ponto |
| CORPO | até 45 palavras | Provar a headline e entregar o benefício com coisa concreta | Repetir o que a headline já disse |
| TRANSIÇÃO | até 20 palavras | Convidar. Só isso. | Continuar argumentando |
| CTA | curto | O clique, 1ª pessoa do desejo | Ser vago ("saiba mais") |

---

## A REGRA QUE MAIS SE VIOLA

**A TRANSIÇÃO NÃO CONTINUA EXPLICANDO.**

O argumento acaba no CORPO. Se o benefício é forte, ele pertence ao corpo. A transição só faz a ponte para o convite.

| Errado (mais argumento) | Certo (convite) |
|---|---|
| "Reduzi 5 pessoas do time e a receita ficou de pé porque o atendimento não dependia mais de gente." | "Eu posso te mostrar como ter esse mesmo atendimento no seu negócio." |
| "Margem sobe de dois lados: menos custo fixo por tarefa e trabalho com mais qualidade." | "Eu posso te mostrar como aumentar sua margem de lucro usando IA." |
| "Quem usou IA não trabalha mais horas. Ele entrega com mais profundidade, mais qualidade e mais rápido, e é aprovado na hora. Isso eu instalo na sua empresa." | "Eu instalo isso na sua empresa, e não estou falando de ChatGPT nem de Claude." |

Teste rápido: se a transição pode ser lida como "mais um argumento", ela está errada.

---

## Regras de headline (veto absoluto)

**RH-01 · HEADLINE NUNCA TEM PONTO.** É frase única. Se tem ponto, são duas frases e não é headline.

| Errado | Certo |
|--------|-------|
| Sua empresa cresceu até o tamanho da sua agenda. Parou ali. | Sua empresa cresceu até o tamanho da sua agenda e parou ali |
| Hoje 80% do meu tempo é estratégia. O resto roda sozinho. | Hoje 80% do meu tempo é estratégia porque o resto roda instalado |
| Equipe, agência, automação, ChatGPT. Nada tirou você da operação. | Equipe, agência, automação e ChatGPT: nada tirou você da operação |

Corrija com vírgula, dois pontos, "e", "porque", ou reescreva menor.

**RH-02** · Corpo: no máximo 1 ponto por frase longa. Evite texto picado.
**RH-03** · Headline nunca abre com pergunta. Sempre afirmação contraintuitiva.
**RH-04** · Headline sai de estrutura validada de swipe, nunca inventada. Declare qual fórmula clonou e de qual headline do banco veio a estrutura.

---

## Fórmulas de headline (clone uma, declare qual)

| Nome | Estrutura |
|------|-----------|
| `how_to` | Como [RESULTADO] em [TEMPO] mesmo que [OBJEÇÃO] |
| `attention_avatar` | Atenção [AVATAR ESPECÍFICO]: [PROMESSA ESPECÍFICA] |
| `who_else` | Quem mais quer [BENEFÍCIO] (evitar em público empresário, soa a comunidade) |
| `secret_of` | O segredo de [RESULTADO INVEJÁVEL] |
| `warning` | Aviso: não [AÇÃO] antes de ler isto |
| `they_laughed` | [SITUAÇÃO HUMILDE]... mas quando [RESULTADO SURPREENDENTE] |
| `give_me` | Me dê [TEMPO CURTO] e eu te dou [RESULTADO GRANDE] |
| `amazing` | [COISA] que [BENEFÍCIO ESPECÍFICO] |
| `formula_resultado` | [RESULTADO ESPECÍFICO] em [TEMPO] ou [GARANTIA] |
| `se_voce` | Se você [PROBLEMA], aqui está [SOLUÇÃO] |

**Nunca escreva o nome da fórmula dentro da headline.** Erro real cometido: "Amazing: uma pessoa passa a produzir como dez". "Amazing" é o rótulo interno, não é palavra de copy em português.

---

## Conexão com o headline bank (`swipe/headlines/_index.yaml`)

O `_index.yaml` é o índice canônico de headlines do squad: 244 entradas classificadas por tier.

| Tier | Qtd | O que é | `clonavel_como_campea` |
|------|-----|---------|------------------------|
| A | 24 | Campeã comprovada: autor real, campanha específica, resultado documentado | `true` |
| B | 56 | Autor real, sem prova de resultado | `false` |
| C | 164 | Template ou estrutura, sem autor identificado | `false` |

**Regra de citação obrigatória (BANK-01 e BANK-02).** Ao declarar a fórmula clonada, o executor também precisa citar:

1. O `id` da headline do `_index.yaml` que serviu de estrutura (ex: `hl_halbert_001`)
2. O tier dessa headline (A, B ou C)

Se a estrutura veio de **tier B ou C**, é obrigatório escrever na peça, com essas palavras:

```
estrutura de template, não campeã comprovada
```

Clonar de tier A é o padrão. Tier B e C só quando não houver estrutura A que sirva ao ângulo.

Formato da declaração no rodapé de cada peça:

```
`{formula_clonada}` · fonte: `{id_headline}` (tier {A|B|C})
```

Exemplo tier A:
```
`they_laughed` · fonte: `hl_conroy_001` (tier A)
```

Exemplo tier C:
```
`se_voce` · fonte: `hl_b2_curiosity_003` (tier C, estrutura de template, não campeã comprovada)
```

---

## Guardrails (qualquer violação reprova a peça)

### Proibições absolutas

```
ZERO travessão. Use vírgula, ponto, parênteses ou dois pontos.
ZERO emoji.
ZERO palavra em inglês na copy.
Português brasileiro com acentuação completa.
```

### Palavras e expressões banidas

| Banido | Por quê |
|--------|---------|
| descubra, aprenda, transforme sua vida | Clichê de IA e de coach |
| desbloqueie, eleve, jornada, mergulhe, revolucione | Idem |
| mindset, próximo nível, acredite em você | Clichê de coach |
| "o segredo é" | Dispara o validador de clichê |
| briefing | A pessoa não sabe o que é. Use "4 horas suas" |
| quem mais quer | Linguagem de comunidade. Empresário é prático |
| instalo isso aí dentro | Reprovado pelo cliente. Use "na sua operação" ou "no seu negócio" |
| grátis, gratuito, sem custo | A consultoria é gratuita, mas isso não se diz na peça |

Universais do oráculo: nunca "descubra" (RU-01), "aprenda" (RU-02), "transforme sua vida" (RU-03).

### Regras de anúncio (veto instantâneo)

| ID | Regra | Motivo |
|----|-------|--------|
| RA-01 | NUNCA começar com pergunta | Cérebro responde "não" e scrolla |
| RA-02 | Curiosidade nos 3 primeiros segundos | Sem curiosidade imediata, o scroll continua |
| RA-03 | NUNCA pitch de venda explícito | Anúncio filtra, não vende |
| RA-04 | NUNCA ensinar conteúdo técnico | Anúncio que ensina é ignorado |
| RA-05 | NUNCA clichê de marketing digital | Ver CL-01 a CL-38 no oráculo |

### Padrões estruturais a evitar (cheiro de IA)

- **Negation pivot** repetido ("não é X, é Y"): no máximo 2 por lote de 15
- **Tríade mecânica**: "Sem A. Sem B. Sem C."
- **Staccato**: 3 ou mais frases curtas empilhadas com ponto
- **Paralelismo simétrico** entre frases consecutivas
- **Repetição de abertura**: mais de 4 headlines começando com a mesma palavra num lote de 30

### Números

Todo número vem do proof-bank do cliente. **Nada inventado.** Preço da oferta nunca aparece na peça.

---

## Concretude obrigatória

Cada peça precisa nomear pelo menos uma coisa reconhecível.

| Prefira | Em vez de |
|---------|-----------|
| o agente que responde seu cliente no WhatsApp | infraestrutura de atendimento |
| o CRM que eu entrego pronto | camada de inteligência comercial |
| o relatório que chega no seu celular às 7 | visibilidade operacional |
| o post e a copy saindo toda semana | máquina de conteúdo |

**Teste:** se a pessoa lê headline e corpo e não sabe o que está sendo vendido, reprove e reescreva.

---

## Destino: diagnóstico ou aplicação

| Destino | Quando usar | Transição | CTA |
|---------|-------------|-----------|-----|
| **Diagnóstico** | Dor, desejo, inimigo, contraste, margem | convida para a consultoria | "Clica abaixo e agenda a sua consultoria" |
| **Aplicação** | Oferta direta | convida a preencher formulário | "Preencher o formulário" · "Quero saber mais" |

O diagnóstico é gratuito, mas isso não é dito na peça.

### Padrões de transição · DIAGNÓSTICO

Varie. Não repita o mesmo em peças vizinhas.

1. "Eu posso te mostrar como ter isso instalado no seu negócio com uma consultoria de IA."
2. "Na consultoria eu abro [COISA CONCRETA] e mostro como fica com os seus números."
3. "Eu posso te mostrar como ter [BENEFÍCIO] no seu negócio."
4. "Eu instalo isso na sua operação, e a consultoria começa mostrando onde."
5. "Isso cabe na sua empresa também, e a consultoria mostra exatamente como."
6. "Em 90 dias isso está rodando aí, e a consultoria é onde a gente começa."
7. "Eu instalo isso no seu negócio." (curta, usar com moderação)

### Padrões de transição · APLICAÇÃO

1. "São de 3 a 5 instalações ao mesmo tempo, preenche o formulário e a gente vê se o seu negócio entra agora."
2. "Preenche o formulário e eu te mostro como isso fica no seu negócio."
3. "Se quiser ver como isso funciona no seu caso, preenche o formulário abaixo."

---

## Eixos psicológicos

Cubra pelo menos 3 eixos distintos por lote. Variação cosmética não conta como diversidade: o Meta detecta e limita a distribuição.

| Eixo | Prefixo | O que ativa | Exemplo de ângulo |
|------|---------|-------------|-------------------|
| **dor** | `DR-n` | O problema que ele vive e não resolveu | CEGUEIRA OPERACIONAL |
| **desejo** | `DS-n` | O estado final que ele quer | O RESUMO DAS 7 DA MANHÃ |
| **inimigo** | `IN-n` | O culpado externo nomeado | A AGÊNCIA QUE VENDE RELATÓRIO |
| **contraste** | `CT-n` | Dois caminhos, um certo e um errado | DOIS EMPRESÁRIOS, UM USOU IA |
| **margem / prova** | `MG-n` | O número ou case que sustenta | OS 20.400 QUE PARARAM DE SAIR |
| **oferta direta** | `OD-n` | A oferta nomeada, entendível na leitura | A OFERTA NOMEADA |

**No eixo dor:** a peça não pode só descrever o problema e parar. Tem que apontar a solução e convidar.
**No eixo desejo:** não é "sistema rodando". É concreto: o resumo no WhatsApp, o relatório sem pedir, a leitura do CRM.
**No eixo inimigo:** o inimigo precisa estar NOMEADO, sem ambiguidade.
**No eixo contraste:** empresário não quer "ter sistema". Quer ganhar. Fale de vender mais, ganhar concorrência, entregar melhor.

---

## Workflow

### FASE 1: Triagem (obrigatória)

Confirmar antes de escrever:

1. **Cliente**: carregar perfil, ICP, voice, positioning, products
2. **Faixa de preço**: define o nível de prova necessário
3. **Temperatura**: frio, morno ou quente
4. **Awareness**: em qual nível de consciência o prospect está
5. **Destino**: diagnóstico ou aplicação

Se faltar tese, big idea ou mecanismo único, avisar que a copy sai genérica e sugerir diagnóstico antes.

### FASE 2: Carregar contexto

- `data/anuncios-estaticos/INSTRUCAO-LLM-anuncio-estatico.md` (fonte de verdade)
- `templates/anuncio-estatico.md` (formato)
- `checklists/oraculo-torriani.md` (RA-01 a RA-05, RH-01 a RH-04, RU-01 a RU-03, CL-01 a CL-38)
- `swipe/headlines/_index.yaml` (banco de headlines com tier)
- Proof-bank do cliente (todo número sai daqui)
- Voice profile do cliente

### FASE 3: Definir ângulos

Um ângulo por peça, em caixa alta. Cubra no mínimo 3 eixos distintos.

### FASE 4: Selecionar estruturas no headline bank

Para cada peça, escolher a headline do `_index.yaml` que vai servir de estrutura. Priorizar tier A. Anotar `id` e tier antes de escrever.

### FASE 5: Escrever (via john-carlton)

Despachar o executor com contexto do cliente, persona e as estruturas selecionadas. Ordem de escrita: headline, corpo, transição, CTA.

Declarar em cada peça a fórmula clonada, o `id` da headline fonte e o tier.

Agrupar por temperatura de público ou por sub-oferta.

### FASE 6: Conferir limites

Contar palavras, não estimar. Headline acima de 15, corpo acima de 45 ou transição acima de 20 volta para reescrita.

### FASE 7: Checklist pré-entrega (15 itens)

```
[ ] Nenhuma headline tem ponto
[ ] Nenhuma headline começa com pergunta
[ ] Nenhuma headline passa de 15 palavras (CONTE, não estime)
[ ] Nenhum corpo passa de 45 palavras
[ ] Nenhuma transição passa de 20 palavras
[ ] Zero travessão no texto inteiro
[ ] Zero emoji
[ ] Zero palavra em inglês na copy
[ ] Nenhuma palavra da lista de banidos
[ ] Cada peça nomeia coisa concreta
[ ] A transição só convida, não argumenta
[ ] Todo número rastreado ao proof-bank
[ ] Preço não aparece
[ ] Fórmula declarada em cada peça, com id do `_index.yaml` e tier (tier B ou C traz a declaração de template)
[ ] No máximo 4 headlines abrindo com a mesma palavra
```

### FASE 8: Validação obrigatória

1. **Filtro Anti-IA**: `bash ../conteudo/scripts/validate-anti-ia.sh <arquivo>` mais crítico LLM 5 dimensões, nota 10 em todas
2. **Oráculo Torriani**: `bash copy/scripts/oraculo-precheck.sh <arquivo>`, regras invioláveis e craft Sugarman

Anti-IA precisa passar limpo. Oráculo precisa dar auto-reprova falso. Loop de correção: no máximo 3 iterações.

### FASE 9: Entrega

Arquivo markdown com cabeçalho declarando o formato, os anúncios numerados e rodapé de conformidade.

Cabeçalho padrão:

```markdown
**Cliente:** {slug} · **Produto:** {produto} · **Destino:** {destino}
**Formato:** Anúncio Estático 4 blocos (Ângulo interno + Headline ≤15 + Corpo ≤45 + Transição ≤20 + CTA)
**Conformidade:** headlines ≤15 palavras, corpos ≤45, transições ≤20 · PT-BR, acentuação completa, zero emoji, zero travessão
**Data:** {AAAA-MM-DD}
```

Rodapé padrão:

```markdown
## Conformidade
- Headlines: todas ≤15 palavras, frase única, zero ponto. Corpos: ≤45. Transições: ≤20.
- Fórmula clonada declarada em cada peça, com id do `swipe/headlines/_index.yaml` e tier.
- Prova vinda do proof-bank/positioning do {cliente}. Nada inventado.
- PT-BR, acentuação completa, zero emoji, zero travessão.
- Padrão: `data/anuncios-estaticos/INSTRUCAO-LLM-anuncio-estatico.md` (v2.0).
```

---

## Formato de saída

```markdown
### {ID} · {eixo}
**ÂNGULO:** {CONCEITO EM CAIXA ALTA}
**HEADLINE:** {frase única, zero ponto}
**CORPO:** {benefício concreto, até 45 palavras}
**TRANSIÇÃO:** {só o convite, até 20 palavras}
**CTA:** {o clique}
`{formula_clonada}` · fonte: `{id_headline}` (tier {A|B|C})
```

Nomenclatura por eixo: `DR-n` dor · `DS-n` desejo · `IN-n` inimigo · `CT-n` contraste · `MG-n` margem · `OD-n` oferta direta

---

## Exemplos aprovados

Estes passaram por validação e aprovação do cliente. Use como referência de ritmo e concretude.

### Exemplo 1 · DOR

```
ÂNGULO: CEGUEIRA OPERACIONAL
HEADLINE: Você precisa perguntar pra três pessoas o que aconteceu na sua própria empresa
CORPO: Os assistentes de IA mandam o resumo pronto no seu WhatsApp toda manhã, com as vendas de ontem, as oportunidades do CRM e o status de cada atendimento.
TRANSIÇÃO: Eu posso te mostrar como ter isso instalado no seu negócio com uma consultoria de IA.
CTA: Clica abaixo e agenda a sua consultoria
FÓRMULA: secret_of
```

Por que funciona: a headline nomeia a dor sem explicar demais. O corpo entrega o benefício com três coisas concretas. A transição só convida.

### Exemplo 2 · DESEJO

```
ÂNGULO: CRM QUE SE LÊ SOZINHO
HEADLINE: O resumo de tudo que aconteceu no seu CRM, todo dia no seu WhatsApp
CORPO: As oportunidades quentes, os leads quase fechando, os que estão parados e os que morrem hoje, tudo separado e enviado pra você sem ninguém do seu time precisar olhar. O assistente já varreu o CRM de madrugada.
TRANSIÇÃO: Na consultoria eu abro esse painel e mostro como ele fica com os seus números.
CTA: Agenda a sua consultoria de IA
FÓRMULA: secret_of
```

Por que funciona: o corpo detalha o que ele recebe, item por item, e fecha com o motivo (o assistente varreu de madrugada). A transição usa o padrão 2, que é mais específico.

### Exemplo 3 · INIMIGO

```
ÂNGULO: A AGÊNCIA QUE VENDE RELATÓRIO
HEADLINE: A agência te cobra 10 mil por mês e entrega um relatório que ninguém lê
CORPO: Enquanto isso o WhatsApp fica sem resposta, o CRM fica vazio e a proposta atrasa três dias. Os assistentes de IA fazem o contrário: respondem na hora, alimentam o CRM sozinhos e deixam a proposta pronta antes da reunião acabar.
TRANSIÇÃO: Eu posso te mostrar como ter esses assistentes trabalhando no seu negócio.
CTA: Clica abaixo e agenda a sua consultoria de IA
FÓRMULA: attention_avatar
```

Por que funciona: inimigo nomeado com número na headline. O corpo mostra o dano e a alternativa lado a lado.

### Exemplo 4 · CONTRASTE

```
ÂNGULO: DOIS EMPRESÁRIOS, UM USOU IA
HEADLINE: Dois empresários começaram juntos, um usou IA e hoje ganha 80% das concorrências que entra
CORPO: O outro continua entregando o mesmo material, no mesmo prazo, disputando por preço. Quem usa IA não trabalha mais horas: entrega com mais profundidade, mais qualidade e mais rápido, e é aprovado na hora.
TRANSIÇÃO: Eu instalo isso na sua empresa, e não estou falando de ChatGPT nem de Claude.
CTA: Clica abaixo e agenda a consultoria, eu te mostro como ter isso no seu negócio
FÓRMULA: they_laughed
```

Por que funciona: o contraste é sobre GANHAR, não sobre ter sistema. A transição derruba a objeção do ChatGPT em cinco palavras.

### Exemplo 5 · MARGEM

```
ÂNGULO: NEGÓCIO SE MEDE PELA MARGEM
HEADLINE: Empresário de verdade sabe que negócio bom se mede pela margem de lucro
CORPO: E é exatamente nela que os assistentes de IA mexem, sem você tocar no preço nem cortar entrega. Menos custo fixo por tarefa e trabalho com mais qualidade, profundidade e velocidade, que é o que faz você cobrar melhor.
TRANSIÇÃO: Eu posso te mostrar como aumentar sua margem de lucro usando IA no seu negócio.
CTA: Clica abaixo e agenda a sua consultoria individual
FÓRMULA: secret_of
```

Por que funciona: o eixo margem fala da métrica que o empresário já usa pra medir o próprio negócio. O corpo explica de onde a margem sai, dos dois lados.

### Exemplo 6 · OFERTA DIRETA (destino aplicação)

```
ÂNGULO: A OFERTA NOMEADA
HEADLINE: Consultoria individual de IA onde eu instalo os assistentes dentro do seu negócio
CORPO: Não é curso, não é aula, não é ferramenta pra você configurar. Você recebe CRM montado, atendimento no WhatsApp respondendo na hora e assistentes escrevendo seu conteúdo, tudo rodando em 90 dias.
TRANSIÇÃO: São de 3 a 5 instalações ao mesmo tempo, preenche o formulário e a gente vê se o seu negócio entra agora.
CTA: Quero saber mais
FÓRMULA: attention_avatar
```

Por que funciona: a oferta é entendível na leitura, com o que entra e o prazo. A transição usa escassez real e manda pro formulário.

---

## Exemplos reprovados (e por quê)

### Reprovado por headline com ponto

```
HEADLINE: Sua empresa cresceu até o tamanho da sua agenda. Parou ali.
```
Duas frases. Viola RH-01. Correção: "Sua empresa cresceu até o tamanho da sua agenda e parou ali"

### Reprovado por não se explicar

```
HEADLINE: Hoje 80% do meu tempo é estratégia porque o resto roda instalado
```
"Roda instalado" não diz nada para quem lê de fora. O que roda? Instalado onde? Falta concretude. Correção: nomear o que roda (o atendimento no WhatsApp, o CRM, o conteúdo).

### Reprovado por transição redundante

```
HEADLINE: O agente que atende meu cliente hoje vai atender o seu cliente também
CORPO: Mesma lógica de resposta, mesma velocidade, mesmo padrão, só treinado no que o seu negócio vende.
TRANSIÇÃO: Reduzi 5 pessoas do time e a receita ficou de pé porque o atendimento não dependia mais de gente.
```
A transição dá mais um argumento em cima de algo já fechado. Correção: "Eu posso te mostrar como ter esse mesmo atendimento no seu negócio."

### Reprovado por palavra em inglês

```
HEADLINE: Amazing: uma pessoa passa a produzir como dez dentro do seu negócio
```
"Amazing" é o nome interno da fórmula, não é copy. Correção: "Uma pessoa sozinha entregando o volume que hoje ocupa dez na sua empresa"

### Reprovado por linguagem de comunidade

```
HEADLINE: Quem mais quer parar de engordar a folha todo ano
```
Empresário é prático, não responde a linguagem de comunidade. Trocar por afirmação direta.

---

## Specs de arte

| Item | Valor |
|------|-------|
| Feed | 1080x1080 |
| Story | 1080x1920 |
| Texto na imagem | máximo 20% da área |
| Hierarquia visual | TAG → HEADLINE → CORPO → CTA → LOGO |

A **transição** normalmente não vai na arte. Ela vai no texto do post (primary text do Meta), junto com o CTA.

Design system ativo:

```
Fundo    radial-gradient #1a2444 → #0d1225 → #080c1a
Fonte    Inter 400/700/900
Accent   #F87171 coral
Ink      #FFFFFF · Body #CBD5E1 · Muted #94A3B8
```

---

## Volume (Meta Advantage+ / Andromeda)

- 8 a 15 criativos por conjunto de anúncio, cada um com ângulo distinto
- 8 a 20 criativos novos por mês
- Renovar 25 a 30% da biblioteca por mês
- Framework P.D.A. por criativo: Persona, Desejo, Awareness

---

## Handoff

| Situação | Próximo |
|----------|---------|
| Anúncio aprovado | @traffic (veiculação) ou squad criativos (arte) |
| Precisa de arte | Squad criativos, com a direção visual |
| Precisa de oferta antes | @alex-hormozi (grand slam offer) |
| Público indefinido | diagnose-avatar antes de escrever |

---

## Completion Criteria

- [ ] Cliente carregado e triagem feita (preço, temperatura, awareness, destino)
- [ ] INSTRUÇÃO v2.0 e template `anuncio-estatico.md` carregados
- [ ] `swipe/headlines/_index.yaml` consultado e estruturas selecionadas
- [ ] Mínimo 3 eixos psicológicos distintos cobertos
- [ ] Todas as headlines com 15 palavras ou menos, frase única, zero ponto
- [ ] Todos os corpos com 45 palavras ou menos
- [ ] Todas as transições com 20 palavras ou menos, só convite
- [ ] Nenhuma headline começa com pergunta
- [ ] Cada peça nomeia pelo menos uma coisa concreta
- [ ] Fórmula clonada declarada com id do `_index.yaml` e tier em cada peça
- [ ] Clones de tier B ou C trazem "estrutura de template, não campeã comprovada"
- [ ] Todo número rastreado ao proof-bank, preço ausente
- [ ] Checklist de 15 itens rodado
- [ ] Filtro Anti-IA 10/10 nas 5 dimensões
- [ ] Oráculo Torriani aprovado
- [ ] Zero emoji, zero travessão, zero palavra em inglês, acentuação completa
- [ ] Cabeçalho e rodapé de conformidade no arquivo
