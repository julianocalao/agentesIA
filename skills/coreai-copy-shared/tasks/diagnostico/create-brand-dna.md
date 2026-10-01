# Create Brand DNA — Mapa do Dominio

```yaml
task_id: create-brand-dna
version: 3.0
framework: copy-framework-v2
category: diagnostico
complexity: medium
estimated_time: 20-60min
agent_owner: copy-chief
requires_research: false

output:
  file: "<raiz>/businesses/<slug>/outputs/copy/brand-dna.md"  # gate READY antes de gravar
  format: markdown
  load: AUTO_ON_CLIENT

tags: [marca, brand, tom-de-voz, icp, posicionamento, diagnostico, mapa-dominio]
```

---

## Purpose

Construir o Mapa do Dominio completo de uma marca/cliente. Este arquivo e carregado AUTOMATICAMENTE toda vez que qualquer task de criacao rodar para esse cliente. Elimina repeticao de contexto e garante consistencia em toda copy produzida.

> "Quanto mais contexto o sistema tem sobre a marca, melhor a copy. O Mapa do Dominio e a fundacao de tudo."

---

## When to Use

```yaml
USE quando:
  - Novo cliente entra no sistema
  - Primeira vez criando copy para alguem
  - Cliente quer padronizar tom e comunicacao
  - Informacoes estao espalhadas e precisam ser centralizadas

NAO USE quando:
  - Cliente ja tem brand-dna.md criado (use *update-brand-dna)
  - So precisa de uma copy rapida sem contexto de marca
```

---

## Como Funciona

O Mapa do Dominio tem 11 blocos. O usuario NAO precisa preencher todos — preenche o que tiver. Quanto mais contexto, melhor a copy.

**Regra de atrito zero:** Se o usuario manda informacoes soltas ("sou mentor de negocios, ajudo donos de agencia a escalar"), ja comece a montar o mapa. Pergunte so o que faltar para ter o minimo viavel.

### Niveis de Preenchimento

```yaml
nivel_1_minimo:
  blocos: [1, 3, 4]
  descricao: "Quem sou + Diferencial + Cliente Ideal — suficiente para copy basica"
  tempo: "10-15 min"

nivel_2_recomendado:
  blocos: [1, 2, 3, 4, 5, 6, 7]
  descricao: "Mapa completo — copy de alta qualidade"
  tempo: "20-30 min"

nivel_3_completo:
  blocos: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  descricao: "Mapa completo com argumentacao e narrativa — copy premium"
  tempo: "40-60 min"

nivel_4_campanha:
  blocos: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  descricao: "Mapa completo + vilao + emocao + big idea — copy de campanha premium"
  tempo: "60-90 min"
```

---

## Protocolo de Conducao

**REGRA CRITICA:** Conduzir pergunta a pergunta, bloco a bloco. NAO enviar tudo de uma vez.

```
1. Comecar pelo Bloco 1 (Quem sou eu)
2. Validar resposta: "Perfeito, anotado: [resumo]"
3. Avancar para proximo bloco
4. Se usuario ja deu contexto, preencher automaticamente e confirmar
5. Parar nos 3 blocos obrigatorios se usuario quiser (nivel 1)
6. Oferecer expandir: "Quer aprofundar mais?"
```

---

## Elicitacao por Bloco

### Bloco 1: QUEM SOU EU (obrigatorio)

```elicit
- Qual seu nome e nome da marca?
- O que voce faz em 1 frase?
- Qual sua historia de origem?
  - ANTES: como estava, o que sentia, o que tentava
  - DESCOBERTA: ponto de virada, o que mudou
  - DEPOIS: onde esta hoje, o que conquistou
- Quais suas credenciais? (anos de experiencia, certificacoes, formacoes)
- Qual seu maior resultado pessoal?
- Por que VOCE e a pessoa certa pra resolver esse problema?
  - Ha quanto tempo trabalha com isso?
  - Quantas pessoas ja ajudou?
  - Voce ja esteve na situacao do seu cliente?
```

### Bloco 2: O QUE EU FACO (opcional)

```elicit
- Quais sao seus produtos/servicos? (listar todos)
- Para cada produto:
  - Nome
  - Formato (mentoria, curso, consultoria, servico, produto fisico)
  - Faixa de preco (low/mid/high/premium)
  - Entrega (online, presencial, hibrido)
  - Duracao (semanas, meses, acesso vitalicio)
  - Resultado principal que entrega
  - Bonus/extras inclusos
  - Garantia oferecida
- Qual e seu produto principal (carro-chefe)?
- Tem escada de valor? (produto de entrada → premium)
```

### Bloco 3: MEU DIFERENCIAL (obrigatorio)

```elicit
DESTINO (a grande oportunidade):
- Qual DESTINO voce leva seu cliente? (transformacao principal)
- Frase de Trono — sua promessa mais poderosa em 1 frase:
  Formato: "[RESULTADO] em [PRAZO], mesmo que [OBJECAO], sem [OBJECAO]"
  Exemplo: "Faturar 100k/mes vendendo mentorias em 90 dias, mesmo sem grande audiencia, sem lancamentos desgastantes"

METODO (seu veiculo):
- Tem um metodo/framework/sistema com nome proprio? Qual?
- Quantos pilares/etapas tem?
- Para cada pilar:
  - Nome
  - O que e (1 frase)
  - Por que existe (qual problema resolve)
  - Como funciona (processo resumido)
  - Mecanismos/estrategias especificas desse pilar
- POR QUE seu metodo e diferente do que o mercado faz?
  - "A maioria faz: [X]. Eu faco: [Y]."
  - "Resultado da maioria: [X]. Meu resultado: [Y]."

MECANISMO UNICO:
- Qual a PARTE MAIS CRITICA do seu metodo? (se tirar, nao funciona)
- Essa parte e diferente de como os outros fazem? Como?
- Por que funciona melhor? (logica/ciencia por tras)
- Tem nome proprio?

BENEFICIOS:
- Quando alguem aplica seu metodo, o que ganha?
  - Financeiros: quanto pode faturar? economia? ROI?
  - Tempo/liberdade: trabalha menos? mais tempo livre? automatizacao?
  - Emocionais/status: como se sente? como e visto?

PROPOSTA DE VALOR:
- Preencher: "O [METODO]: Para [QUEM]. Proporciona [O QUE]. Em [PRAZO]. Mesmo que [OBJECAO]. Sem [OBJECAO]. Atraves do [MECANISMO]."

BIG IDEA:
- Qual a grande ideia por tras da sua marca?
- Se eu cobrir seu nome e colocar sua promessa no perfil do concorrente, ela ainda funciona?
  (se sim, precisa diferenciar mais)
```

### Bloco 4: MEU CLIENTE IDEAL (obrigatorio)

```elicit
PERFIL:
- Quem e seu cliente ideal? (perfil em 1-2 frases)
- Dados demograficos: idade, genero, profissao, renda, localizacao

PONTO A — SITUACAO ATUAL:
- Qual a maior dor/frustracao dele?
- O que ele ja tentou que nao funcionou?
- Qual a solucao COMUM que ele usa hoje? (o que o mercado oferece e nao resolve)
- Crencas limitantes:
  - Sobre o PROBLEMA: "Ele acredita que..." (ex: "meu nicho e saturado")
  - Sobre a SOLUCAO: "Ele acredita que..." (ex: "so lancamento funciona")
- Como ele se sente? (emocoes dominantes)
- Que palavras/frases ele usa pra descrever o problema? (linguagem exata)

PONTO B — SITUACAO DESEJADA:
- Qual o resultado tangivel? (com numeros se possivel)
- Como ele se sente?
- O que muda no dia a dia dele?

MUDANCA DE CRENCA:
- O que ele PRECISA acreditar para comprar de voce?
  - Sobre o problema: de "[crenca antiga]" para "[nova crenca]"
  - Sobre a solucao: de "[crenca antiga]" para "[nova crenca]"

ONE BELIEF (crenca central):
- Qual a UNICA COISA que ele precisa acreditar para que TODAS as objecoes se tornem irrelevantes?
  "Se eu puder fazer ele acreditar que [OPORTUNIDADE] e a chave para [DESEJO] e so e alcancavel atraves de [MEU METODO], todas as objecoes se tornam irrelevantes."

OBJECOES:
- O que impede ele de comprar? (listar top 3-5)
- Para cada objecao: como quebrar?

NIVEL DE CONSCIENCIA (Schwartz):
  [ ] Unaware — nao sabe que tem problema
  [ ] Problem Aware — sabe do problema, nao da solucao
  [ ] Solution Aware — sabe que existem solucoes, nao conhece a sua
  [ ] Product Aware — conhece seu produto, ainda nao comprou
  [ ] Most Aware — ja te conhece, so precisa de oferta

NAO VENDO PARA: [desqualificadores]
```

### Bloco 5: TOM E VOZ (opcional)

```elicit
- Se sua marca fosse uma pessoa, como ela seria?
- Qual tom predominante? (escolha 1-3)
  [ ] Provocador / Desafiador
  [ ] Inspirador / Motivacional
  [ ] Direto / Sem rodeios
  [ ] Sarcastico / Ironico
  [ ] Premium / Sofisticado
  [ ] Casual / Acessivel
  [ ] Indignado / Revolucionario
  [ ] Vulneravel / Autentico
  [ ] Tecnico / Especialista
  [ ] Storyteller / Narrativo
- Tem algum criador/marca que admira como referencia de comunicacao?
- Usa linguagem tecnica ou simplificada?
- Primeira pessoa ("eu") ou terceira pessoa ("a marca")?
- Usa girias/regionalismos? Quais?
- Palavras que a marca SEMPRE usa? (bordoes, expressoes proprias)
- Palavras que a marca NUNCA usa? (proibidas alem dos cliches do Oraculo)
```

### Bloco 6: PROVAS (opcional)

```elicit
NUMEROS:
- Quantos clientes/alunos ja atendeu?
- Faturamento gerado para clientes?
- Anos no mercado?
- Outros numeros relevantes?

CASES DE SUCESSO (Ponto A → Ponto B):
- Case 1: [nome] estava [situacao]. Aplicou [metodo]. Em [tempo] alcancou [resultado].
- Case 2: [idem]
- Case 3: [idem]
(Minimo 3, ideal 5)

DEPOIMENTOS: frases exatas de clientes
MIDIA: aparicoes em podcasts, TV, portais, revistas
PREMIOS/RECONHECIMENTOS: [lista]
PARCERIAS: [lista]
```

### Bloco 7: INIMIGOS (opcional)

```elicit
- O que voce COMBATE no seu mercado?
- Quem sao os "viloes"? (gurus, metodos ruins, industria, mentalidade)
- O que te indigna no seu nicho?
- Que conselhos comuns voce DISCORDA?
- O que o mercado faz que voce se recusa a fazer?
- Qual e a "mentira" que o mercado conta?
- Qual a solucao COMUM que nao funciona? E por que nao funciona?
```

### Bloco 8: NARRATIVA E ARGUMENTACAO (opcional)

```elicit
NARRATIVA:
- Qual e o momento atual da sua marca?
  [ ] Lancamento — estou comecando / reposicionando
  [ ] Crescimento — estou escalando / expandindo
  [ ] Autoridade — ja sou referencia, estou consolidando
  [ ] Legado — estou construindo algo maior que eu
- Qual crenca principal voce quer instalar no publico?
- Qual e a transformacao que sua marca representa?
- Se pudesse resumir sua mensagem em 1 frase para o mundo, qual seria?
- Tema central recorrente na comunicacao? (liberdade, imperio, clareza, verdade, etc.)

ARGUMENTACAO (como muda a crenca do cliente — 3 pilares):
Para cada pilar do seu metodo, qual a mudanca de crenca que ele gera?

- Pilar 1: [nome]
  - Crenca antiga: "[o que acreditam hoje]"
  - Nova crenca: "[o que precisam acreditar]"
  - Evidencia: [dados, casos, logica que prova]

- Pilar 2: [nome]
  - Crenca antiga: "[o que acreditam hoje]"
  - Nova crenca: "[o que precisam acreditar]"
  - Evidencia: [dados, casos, logica que prova]

- Pilar 3: [nome]
  - Crenca antiga: "[o que acreditam hoje]"
  - Nova crenca: "[o que precisam acreditar]"
  - Evidencia: [dados, casos, logica que prova]
```

### Bloco 9: VILAO DA CAMPANHA (opcional)

```elicit
VILAO/INIMIGO:
- Quem ou o que e o vilao desta campanha?
  - E um contraponto ao senso comum?
  - E quem esta causando os problemas para a sua audiencia?
  - Exemplos: Bancos, Industria farmaceutica, Conteudo generico, Promessas de ganhos faceis, Lancamentos, Gurus falsos
- O que o vilao faz que prejudica seu publico?
- Como seu metodo/produto combate esse vilao?
- Qual a narrativa de "nos vs eles"?
```

### Bloco 10: EMOCAO PREDOMINANTE (opcional)

```elicit
EMOCAO DA CAMPANHA:
- Qual a emocao predominante que vai permear TODA a copy?
  - Deriva de GANANCIA ou de MEDO?
  - E um receio (medo de perder) ou um beneficio (desejo de ganhar)?
- Tipo de campanha:
  - Focada em PROMESSA? (resultado que vai levar a pessoa)
  - Derivada de uma PREVISAO? (algo que pode evitar/acontecer)
  - Focada em um METODO? (foco no beneficio do metodo)
- Regra: toda copy vai estar alinhada com essa emocao. Se disse "isso pode acabar com sua familia", ao longo de TODA copy precisa defender isso.
```

### Bloco 11: BIG IDEA ESTRUTURADA (opcional)

```elicit
BIG IDEA:
- Big Idea = Emocao + 1 (ou 2) Nudges
- Qual Nudge vai usar?
  - Escassez
  - Urgencia
  - Segredo
  - Oportunidade
  - Exclusividade (Metodo)
  - Inclusao (Convite)
- Regra do Um — a Big Idea PRECISA ser:
  - Unica (unique)
  - Ultra-Especifica (ultraspecific)
  - Util (useful)
  - Urgente (urgent)
  - Como uma Pilula Magica
  - Explicada em uma frase simples que todos entendam
- Estrutura da promessa:
  [Gatilho] + [Big Idea: Desejo + Resultado] + Objecao + Quebra de Objecoes
- Regra de ouro: "Pequenos beneficios que as pessoas acreditam valem muito mais do que grandes beneficios que elas nao acreditam"
```

---

## Execucao

### Step 1: Coletar Informacoes

Conduzir pergunta a pergunta, bloco a bloco. Se o usuario ja forneceu contexto, absorver e organizar nos blocos. Confirmar cada bloco antes de avancar.

**Regra:** Comecar com os 3 blocos obrigatorios (Quem sou, Diferencial, Cliente Ideal). Depois oferecer expandir.

### Step 2: Montar o Mapa do Dominio

Preencher o template abaixo com as informacoes coletadas.

### Step 3: Validar com o Usuario

Apresentar o mapa montado e perguntar:
- "Isso representa bem sua marca?"
- "Quer ajustar alguma coisa?"
- "Quer aprofundar algum bloco?"

### Step 4: Salvar

Salvar em `<raiz>/businesses/<slug>/outputs/copy/brand-dna.md` (rodar antes `../coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <esse caminho>` e exigir READY)

---

## Output Format

```markdown
# Mapa do Dominio: [NOME DA MARCA]

> [Frase de Trono — promessa central em 1 linha]

**Atualizado em:** [data]
**Versao:** 1.0
**Nivel:** [1-minimo / 2-recomendado / 3-completo / 4-campanha]

---

## 1. QUEM SOU EU

**Nome:** [nome pessoal]
**Marca:** [nome da marca]
**O que faco:** [1 frase]

**Minha Historia:**
- ANTES: [como estava, o que sentia]
- DESCOBERTA: [ponto de virada]
- DEPOIS: [onde esta hoje, o que conquistou]

**Credenciais:** [lista]
**Maior resultado pessoal:** [frase]
**Por que eu:** [por que sou a pessoa certa]

---

## 2. O QUE EU FACO

### Produto Principal
- **Nome:** [nome]
- **Formato:** [tipo]
- **Preco:** [faixa]
- **Duracao:** [tempo]
- **Resultado:** [transformacao]
- **Garantia:** [tipo]
- **Bonus:** [lista]

### Outros Produtos
- [produto 2]: [formato] — [resultado] — [preco]
- [produto 3]: [formato] — [resultado] — [preco]

### Escada de Valor
[entrada] → [intermediario] → [premium]

---

## 3. MEU DIFERENCIAL

### Destino (Grande Oportunidade)
**Frase de Trono:** "[RESULTADO] em [PRAZO], mesmo que [OBJECAO], sem [OBJECAO]"

### Metodo
**Nome:** [nome do metodo]
**Pilares:**
1. **[Pilar 1]:** [o que e] — resolve [problema]
   - Mecanismos: [estrategias/taticas especificas]
2. **[Pilar 2]:** [o que e] — resolve [problema]
   - Mecanismos: [estrategias/taticas especificas]
3. **[Pilar 3]:** [o que e] — resolve [problema]
   - Mecanismos: [estrategias/taticas especificas]

**Por que e diferente:**
- A maioria faz: [X] → Resultado: [ruim]
- Eu faco: [Y] → Resultado: [bom]

### Mecanismo Unico
**Nome:** [nome]
**O que e:** [explicacao]
**Por que funciona:** [logica]

### Beneficios
- Primarios: [top 3]
- Secundarios: [lista]

### Proposta de Valor
"O [METODO]: Para [QUEM]. Proporciona [O QUE]. Em [PRAZO]. Mesmo que [OBJECAO]. Sem [OBJECAO]. Atraves do [MECANISMO]."

### Big Idea
[frase]

---

## 4. MEU CLIENTE IDEAL

**Perfil:** [descricao em 1-2 frases]
**Demografia:** [idade, genero, profissao, renda]

### Ponto A (Situacao Atual)
- **Dor principal:** [dor]
- **Ja tentou:** [o que falhou]
- **Solucao comum do mercado:** [o que usa hoje e nao resolve]
- **Crencas limitantes:**
  - Sobre o problema: "[crenca]"
  - Sobre a solucao: "[crenca]"
- **Emocoes dominantes:** [emocoes]
- **Linguagem exata:** "[frases que usa]"

### Ponto B (Situacao Desejada)
- **Resultado tangivel:** [resultado com numeros]
- **Como se sente:** [emocoes]
- **O que muda:** [mudanca concreta]

### Mudanca de Crenca
- Problema: de "[antiga]" para "[nova]"
- Solucao: de "[antiga]" para "[nova]"

### One Belief
"Se eu puder fazer ele acreditar que [OPORTUNIDADE] e a chave para [DESEJO] e so e alcancavel atraves de [MEU METODO], todas as objecoes se tornam irrelevantes."

### Objecoes
1. [objecao] → Quebra: [como]
2. [objecao] → Quebra: [como]
3. [objecao] → Quebra: [como]

**Nivel de Consciencia:** [nivel Schwartz]
**NAO vendo para:** [desqualificadores]

---

## 5. TOM E VOZ

**Personalidade da marca:** [se fosse uma pessoa, como seria]
**Tom predominante:** [1-3 opcoes]
**Referencia de comunicacao:** [criador/marca admirada]
**Linguagem:** [tecnica / simplificada / mista]
**Pessoa:** [primeira / terceira]
**Bordoes/expressoes proprias:** [lista]
**Palavras PROIBIDAS (alem do Oraculo):** [lista]

---

## 6. PROVAS

**Numeros:**
- [X] clientes/alunos atendidos
- [X] anos no mercado
- [X] faturamento gerado para clientes

**Cases de Sucesso (Ponto A → Ponto B):**
1. **[nome]:** estava [situacao]. Aplicou [metodo]. Em [tempo] alcancou [resultado].
2. **[nome]:** estava [situacao]. Aplicou [metodo]. Em [tempo] alcancou [resultado].
3. **[nome]:** estava [situacao]. Aplicou [metodo]. Em [tempo] alcancou [resultado].

**Depoimentos Marcantes:**
> "[frase exata do cliente]" — [nome]

**Midia/Reconhecimento:** [lista]

---

## 7. INIMIGOS

**O que combatemos:** [causa/movimento]
**Viloes do mercado:** [gurus, metodos, mentalidades]
**Mentira que o mercado conta:** "[frase]"
**Solucao comum que nao funciona:** [o que o mercado faz e por que falha]
**O que nos recusamos a fazer:** [lista]
**Conselhos que discordamos:** [lista]

---

## 8. NARRATIVA E ARGUMENTACAO

**Momento atual:** [lancamento / crescimento / autoridade / legado]
**Crenca central a instalar:** [crenca]
**Transformacao que representamos:** [frase]
**Mensagem para o mundo:** [1 frase]
**Tema recorrente:** [palavra/conceito]

### Argumentacao (3 Pilares)

**Pilar 1: [nome]**
- Crenca antiga: "[o que acreditam hoje]"
- Nova crenca: "[o que precisam acreditar]"
- Evidencia: [dados, casos, logica]

**Pilar 2: [nome]**
- Crenca antiga: "[o que acreditam hoje]"
- Nova crenca: "[o que precisam acreditar]"
- Evidencia: [dados, casos, logica]

**Pilar 3: [nome]**
- Crenca antiga: "[o que acreditam hoje]"
- Nova crenca: "[o que precisam acreditar]"
- Evidencia: [dados, casos, logica]

---

*Mapa do Dominio gerado via Squad Copywriters — Task create-brand-dna v3.0*
*Este arquivo e carregado automaticamente em toda copy para este cliente.*
```

---

## Integracao com o Sistema

```yaml
carregamento:
  quando: "Toda vez que uma task de criacao rodar para o cliente"
  como: "O Copy Chief verifica se existe <raiz>/businesses/<slug>/outputs/copy/brand-dna.md"
  se_existe: "Carrega ANTES de iniciar a task (junto com premissa-core.md)"
  se_nao_existe: "Sugere criar com *brand-dna antes de produzir copy"
  obrigatorio: false
  recomendado: true

nota: "O Oraculo NAO usa o Mapa do Dominio — ele valida a copy pura (regras, checklist, Sugarman). O contexto da marca e responsabilidade do Copy Chief e das tasks de criacao."

atualizacao:
  comando: "*update-brand-dna"
  quando: "Cliente muda posicionamento, lanca produto novo, etc."
  como: "Edita blocos especificos sem recriar tudo"
```

---

## Related

- `data/premissa-core.md` — Premissa obrigatoria (posicionamento premium geral)
- `tasks/diagnostico/diagnose-avatar.md` — Diagnostico profundo de avatar
- `tasks/estrategia/create-unique-mechanism.md` — Criacao de mecanismo unico
- `tasks/estrategia/create-offer.md` — Estruturacao de oferta
- `checklists/oraculo-torriani.md` — Validador (usa Mapa do Dominio como referencia)

---

*Task Version: 3.0*
*"Quanto mais contexto, melhor a copy. O Mapa do Dominio e a fundacao."*

## Executor

```yaml
executor:
  primary: juliano-torriani
  secondary: copy-chief
  rationale: "Juliano Torriani como criador do framework de Mapa do Dominio e posicionamento premium, com Copy Chief apoiando na conducao e organizacao"
```

## Pre-Conditions

```yaml
pre_conditions:
  - Cliente/marca identificado (nome e contexto basico)
  - Acesso ao dono da marca ou informacoes detalhadas sobre o negocio
  - Minimo 3 blocos obrigatorios respondidos (Quem sou, Diferencial, Cliente Ideal)
  - Destino validado pelo gate (<raiz>/businesses/<slug>/outputs/copy/)
```

## Output Example

```markdown
# Mapa do Dominio: Acelerador Digital

> "Fature 100k/mes com sua agencia em 90 dias usando o Metodo Triangulo, mesmo sem grande equipe, sem lancamentos desgastantes."

**Atualizado em:** 2026-03-15
**Versao:** 1.0
**Nivel:** 2-recomendado

## 1. QUEM SOU EU
**Nome:** Ricardo Mendes
**Marca:** Acelerador Digital
**O que faco:** Ajudo donos de agencia a sair do operacional e escalar com processo.
**Credenciais:** 12 anos em marketing digital, 340+ agencias atendidas, ex-dono de agencia que faturava 500k/mes.

## 3. MEU DIFERENCIAL
**Metodo:** Metodo Triangulo (Processo, Pessoas, Performance)
**Mecanismo Unico:** Sprint de Delegacao — sistema de 14 dias para o dono sair de 80% das entregas.
**Por que e diferente:** A maioria ensina a contratar mais. Eu ensino a criar processo antes de contratar.

## 4. MEU CLIENTE IDEAL
**Perfil:** Dono de agencia digital, 28-45 anos, fatura 30-80k/mes, preso no operacional.
**Dor principal:** "Trabalho 60h/semana e o lucro nao reflete o esforco."
**Nivel de Consciencia:** Solution-Aware (Level 3)
**NAO vendo para:** Freelancers, agencias com menos de 5 clientes.
```

## Veto Conditions
- Brand DNA sem diferenciacao clara do mercado
- Tom de voz generico sem personalidade definida
- Ignorar ICP (Ideal Customer Profile) na definicao
