# Workflow: Operação Completa

```yaml
workflow:
  name: operacao-completa
  description: "Pipeline completo de construção de copy — da ideia ao arsenal de peças"
  estimated_time: "8-16 horas (pode ser distribuído em sessões)"
  complexity: muito_alta
  mode: premium
  counterpart: operacao-tatica

use_cases:
  - "Produto novo para público frio"
  - "Oferta que precisa de argumentação completa"
  - "Campanha de alta complexidade (lançamento, high-ticket)"
  - "Público que não te conhece — precisa construir tudo do zero"
  - "Quando não existe Mapa do Domínio salvo"
```

---

## Visão Geral

A Operação Completa é o pipeline máximo de construção de copy. Constrói TUDO — da ideia bruta até o arsenal de peças prontas pra campanha. Cada etapa alimenta a próxima. Nada avança sem o input necessário.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    OPERAÇÃO COMPLETA — 9 ETAPAS                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ETAPA 1        ETAPA 2         ETAPA 3          ETAPA 4               │
│  IDEIA ──────▶ MAPA DO ──────▶ PESQUISA ──────▶ BIG IDEA              │
│               DOMÍNIO         + TESES            ◄──┘                  │
│                               + PROVAS        (volta se               │
│                                 🔒 GATE       tese fraca)             │
│                                                                         │
│  ETAPA 5        ETAPA 6         ETAPA 7          ETAPA 8               │
│  NARRATIVA ──▶ OFERTA ──────▶ COPY ──────────▶ ARSENAIS              │
│               (Hormozi)       MESTRE          ├─ Headlines             │
│                                               └─ Ângulos              │
│                                                                         │
│  ETAPA 9                                                                │
│  DERIVADOS ──▶ Sales page, VSL, emails, ads, conteúdo...              │
│  (campanha)                                                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Roteamento Automático (Copy Chief)

```yaml
roteamento:
  trigger: "Usuário pede pra criar copy de qualquer tipo"

  perguntas_triagem:
    - "Esse produto/oferta já tem Mapa do Domínio salvo?"
    - "O público já te conhece ou é público frio?"
    - "Você já tem tese e provas construídas?"

  regras:
    operacao_completa:
      condicoes:
        - mapa_dominio_existe: false
        - OR publico: "frio (não te conhece)"
      fluxo: "Todas as 9 etapas"

    operacao_tatica:
      condicoes:
        - mapa_dominio_existe: true
        - publico: "quente (já comprou ou já conhece)"
      fluxo: "Pula etapas 1-5, vai direto pra Oferta ou Derivados"

    modo_intermediario:
      condicoes:
        - mapa_dominio_existe: true
        - publico: "frio"
      fluxo: "Pula etapa 2 (já tem mapa), faz pesquisa + tese + big idea + narrativa"
```

---

## 🔒 VETO CONDITIONS GLOBAIS

```yaml
veto_conditions_globais:
  - "SE etapa anterior não completou output obrigatório → NÃO AVANÇAR"
  - "SE Mapa do Domínio não existe e modo = Completa → OBRIGATÓRIO criar"
  - "SE pesquisa não tem nenhuma prova → ALERTA: tese fraca, sugerir pesquisa adicional"
  - "SE Big Idea construída sem prova → ÚNICA EXCEÇÃO: pode voltar pra Etapa 3"
  - "SE Copy Mestre não existe → NÃO gerar derivados"
  - "SE derivado gerado → OBRIGATÓRIO passar por validação Oráculo (10/10)"
```

---

## ETAPA 1: IDEIA

**Objetivo:** Capturar o que o usuário quer vender — ainda sem estrutura.

```yaml
etapa_1:
  name: "Ideia"
  tipo: "Input do usuário"
  elicit: true

  perguntas:
    - id: "ideia_produto"
      pergunta: "O que você quer vender? (descreva a ideia, mesmo que não esteja estruturada)"
      tipo: "texto_livre"
      obrigatorio: true
      exemplo: "Quero vender um serviço de automação com IA para empresas"

    - id: "contexto_mercado"
      pergunta: "Pra quem é isso? Que tipo de pessoa/empresa se beneficia?"
      tipo: "texto_livre"
      obrigatorio: true
      exemplo: "Empresas de serviço que perdem tempo com processos manuais"

    - id: "tem_mapa_dominio"
      pergunta: "Você já tem um Mapa do Domínio salvo pra esse produto?"
      tipo: "sim_nao"
      obrigatorio: true
      se_sim: "Carregar mapa existente e avaliar se pula pra Etapa 3"
      se_nao: "Seguir para Etapa 2"

  output:
    - ideia_capturada: "Descrição da ideia do produto/serviço"
    - contexto_inicial: "Público-alvo preliminar"
    - decisao_fluxo: "Completa ou pular etapas"

  veto_conditions:
    - "SE ideia_produto == vazio → VETO: Não avançar sem saber o que vai vender"
    - "SE contexto_mercado == vazio → Perguntar: 'Pra quem é isso?'"

  salvar_em: "<raiz>/businesses/<slug>/outputs/copy/{produto}/"
```

---

## ETAPA 2: MAPA DO DOMÍNIO

**Objetivo:** Construir o documento-base do produto — público, diferencial, promessa. Persistente e reutilizável.

```yaml
etapa_2:
  name: "Mapa do Domínio"
  tipo: "Construção colaborativa"
  agent_sugerido: "@dan-kennedy + @juliano-torriani"
  task_existente: "tasks/diagnostico/create-brand-dna.md"
  persistente: true
  elicit: true

  componentes:
    - id: "publico"
      nome: "Público Completo"
      descricao: "Quem é o cliente ideal — demográfico, psicográfico, dores, desejos"
      obrigatorio: true

    - id: "diferencial"
      nome: "Diferencial"
      descricao: "O que torna essa oferta única no mercado"
      obrigatorio: true

    - id: "promessa"
      nome: "Promessa Central"
      descricao: "O que o cliente vai conseguir — resultado principal"
      obrigatorio: true

    - id: "por_que_comprar"
      nome: "Por que comprar"
      descricao: "Argumentos de porque o cliente deve comprar isso agora"
      obrigatorio: true

    - id: "awareness_level"
      nome: "Nível de Consciência"
      descricao: "Schwartz 5 Levels — onde o público está"
      agent: "@eugene-schwartz"
      obrigatorio: true

    - id: "sophistication_level"
      nome: "Sofisticação do Mercado"
      descricao: "Schwartz 5 Stages — maturidade do mercado"
      agent: "@eugene-schwartz"
      obrigatorio: true

  output:
    - mapa_dominio_completo: "Documento com todos os componentes preenchidos"

  veto_conditions:
    - "SE publico == vazio → VETO: Sem público definido, nada avança"
    - "SE promessa == vazio → VETO: Sem promessa, não tem copy"
    - "SE diferencial == vazio → ALERTA: Oferta sem diferencial é commodity"

  salvar_em: "<raiz>/businesses/<slug>/outputs/copy/{produto}/mapa-dominio/"

  nota: |
    Este documento é PERSISTENTE. Uma vez criado, fica salvo e pode ser reutilizado
    em qualquer campanha futura desse produto. O Copy Chief consulta antes de começar
    qualquer trabalho: "Já tem Mapa do Domínio pra esse produto?"
```

---

## ETAPA 3: PESQUISA + TESES + PROVAS

**Objetivo:** Pesquisar, construir tese e validar com provas. Gate obrigatório antes de avançar.

```yaml
etapa_3:
  name: "Pesquisa + Teses + Provas"
  tipo: "Pesquisa + Elicitação"
  agent_sugerido: "@todd-brown + @stefan-georgi + @david-ogilvy + @gary-bencivenga"
  elicit: true

  # ═══════════════════════════════════════════════════════════════
  # TASKS DISPONÍVEIS (usar conforme profundidade necessária)
  # ═══════════════════════════════════════════════════════════════
  tasks_disponiveis:
    copysearch:
      arquivo: "tasks/otimizacao/copysearch.md"
      agent: "@david-ogilvy"
      quando_usar: "Pesquisa profunda com anti-alucinação — fatos verificáveis, hierarquia de evidências (Gold/Silver/Bronze)"
      output: "Research Charter, Technical Fact Sheet (13+ fatos), Consumer Language Bank (50+ quotes), Competitive Intelligence Matrix, Strategic Brief"
      duracao: "4-8 horas"
      nota: "RECOMENDADO como ponto de partida — garante que toda pesquisa tem fonte verificável"

    rmbc_research:
      arquivo: "tasks/estrategia/rmbc-method.md"
      agent: "@stefan-georgi"
      quando_usar: "Entender o prospect em profundidade — dores, desejos, crenças, linguagem"
      output: "Research Document com 9 seções (avatar, dores, desejos, provas, concorrentes, key belief, insights, ângulos, objeções)"
      duracao: "3-4 horas"
      nota: "Responde: 'O que meu prospect precisa ACREDITAR para comprar?'"

    create_proof_stack:
      arquivo: "tasks/estrategia/create-proof-stack.md"
      agent: "@gary-bencivenga + @claude-hopkins"
      quando_usar: "Empilhar provas concretas — transformar evidências em arsenal persuasivo"
      output: "Proof Stack com 11 elementos em 4 tiers + guia de deploy por canal"
      duracao: "2-3 horas"
      nota: "Usar APÓS pesquisa (CopySearch ou RMBC) para organizar e fortalecer as provas encontradas"

  # ═══════════════════════════════════════════════════════════════
  # FLUXO RECOMENDADO
  # ═══════════════════════════════════════════════════════════════
  fluxo_recomendado: |
    MODO COMPLETO (pesquisa profunda):
    1. CopySearch (Ogilvy) → fatos verificáveis + linguagem do consumidor + concorrentes
    2. RMBC Research (Georgi) → prospect deep dive + key belief + ângulos
    3. Construir tese a partir dos outputs
    4. Create Proof Stack (Bencivenga) → empilhar provas nos 4 tiers
    5. Gate de provas → validar com usuário

    MODO RÁPIDO (já tem contexto):
    1. RMBC Research (Georgi) → prospect + ângulos
    2. Construir tese
    3. Gate de provas → validar com usuário

  fase_1_pesquisa:
    action: "Executar pesquisa usando tasks disponíveis"
    decisao: |
      Perguntar ao usuário:
      "Qual nível de profundidade de pesquisa você precisa?"
      1. Profunda (CopySearch + RMBC) — para produtos novos ou mercados desconhecidos
      2. Padrão (RMBC Research) — para mercados que você já conhece
      3. Já tenho pesquisa — pular direto para tese
    ferramentas:
      - "CopySearch (tasks/otimizacao/copysearch.md) → pesquisa anti-alucinação com fatos verificáveis"
      - "RMBC Research (tasks/estrategia/rmbc-method.md) → entender prospect + key belief + ângulos"
      - "WebSearch para dados e estatísticas complementares"
      - "Pesquisa de concorrentes"
      - "Estudos de caso do mercado"
    output: "Research Document + Consumer Language Bank + Competitive Matrix"

  fase_2_tese:
    action: "Construir tese a partir das pesquisas + Mapa do Domínio"
    descricao: |
      A tese é a crença central que o público precisa ter pra comprar.
      Ex: "IA pode fazer sua empresa produzir 10x mais"
      Ex: "Você não precisa de mais funcionários, precisa de sistemas"

      A tese DEVE ser construída a partir de:
      - Key Belief identificada no RMBC Research
      - Anchor Fact identificado no CopySearch
      - Gaps competitivos da Competitive Intelligence Matrix
    output: "Tese principal definida + sub-teses de suporte"

  fase_3_proof_stack:
    action: "Empilhar provas usando Create Proof Stack"
    task: "tasks/estrategia/create-proof-stack.md"
    agent: "@gary-bencivenga + @claude-hopkins"
    descricao: |
      Organizar todas as provas encontradas nos 4 tiers (Bencivenga):
      - Tier 1: Demonstração (demos, testemunhos, case studies)
      - Tier 2: Autoridade (experts, mídia, credenciais)
      - Tier 3: Lógica (reason why, especificidade, exposé)
      - Tier 4: Risco (garantia criativa, candor)
    output: "Proof Stack Document com inventário + guia de deploy"

  fase_4_gate_provas:
    type: "🔒 GATE OBRIGATÓRIO"
    elicit: true
    descricao: "Perguntas ao usuário para validar provas da tese"

    perguntas:
      - id: "prova_direta"
        pergunta: "Você tem alguma PROVA que confirma essa tese? (dados, resultados próprios, pesquisas publicadas)"
        tipo: "texto_livre"
        obrigatorio: false
        exemplo: "Nossos clientes aumentaram produtividade em 340% com automação IA"

      - id: "depoimento_fato"
        pergunta: "Tem algum DEPOIMENTO ou FATO que confirma a tese? (caso real, testemunho, resultado mensurável)"
        tipo: "texto_livre"
        obrigatorio: false
        exemplo: "Cliente X saiu de 5h/dia pra 45min no processo Y"

      - id: "tipo_prova"
        pergunta: "Como você pode PROVAR essa tese? Escolha todas que se aplicam:"
        tipo: "multipla_escolha"
        opcoes:
          - "1. Dados/estatísticas próprias (resultados reais)"
          - "2. Depoimentos de clientes (vídeo, texto, print)"
          - "3. Estudos/pesquisas de terceiros (Harvard, McKinsey, etc.)"
          - "4. Demonstração ao vivo (mostrar funcionando)"
          - "5. Comparação antes/depois (métricas concretas)"
          - "6. Autoridade/credenciais (certificações, experiência)"
          - "7. Lógica irrefutável (argumento que não tem como negar)"
          - "8. Não tenho provas ainda — preciso construir"
        obrigatorio: true

    veto_conditions:
      - "SE tipo_prova == '8' E prova_direta == vazio E depoimento_fato == vazio → ALERTA: Tese fraca. Sugerir pesquisa adicional ou ajuste de tese antes de avançar."
      - "SE nenhuma pergunta respondida → VETO: Não avançar sem mínimo de embasamento"
      - "SE Proof Stack tem 0 elementos Tier 1 (demonstração) → ALERTA: Provas fracas, considerar pesquisa adicional"

    output: "Dossiê de provas compilado — alimenta Big Idea e Copy Mestre"

  salvar_em: "<raiz>/businesses/<slug>/outputs/copy/{produto}/pesquisas/"
```

---

## ETAPA 4: BIG IDEA

**Objetivo:** Criar a Big Idea a partir da tese + provas. ÚNICA etapa que pode voltar pra Etapa 3.

```yaml
etapa_4:
  name: "Big Idea"
  tipo: "Construção estratégica"
  agent_principal: "@todd-brown"
  agents_suporte: ["@eugene-schwartz", "@stefan-georgi"]
  task_existente: "tasks/estrategia/create-big-idea.md"
  tasks_complementares:
    - "tasks/estrategia/create-unique-mechanism.md"

  # CHECKPOINT: Mostrar resumo da pesquisa antes de construir Big Idea
  checkpoint_entrada:
    action: "Apresentar insumos da Etapa 3 antes de construir Big Idea"
    mostrar:
      - "Tese principal: [resumo]"
      - "Key Belief (RMBC): [o que o prospect precisa acreditar]"
      - "Anchor Fact (CopySearch): [fato mais forte]"
      - "Gaps competitivos: [o que ninguém está fazendo]"
      - "Provas disponíveis: [resumo do Proof Stack por tier]"
    perguntar: "Esses insumos estão corretos? Quer ajustar antes de construir a Big Idea?"

  input_obrigatorio:
    - tese_principal: "Da Etapa 3"
    - dossie_provas: "Da Etapa 3 (Gate de Provas)"
    - mapa_dominio: "Da Etapa 2"

  componentes:
    - primary_promise: "Promessa principal — específica e mensurável"
    - unique_mechanism: "Mecanismo único NOMEADO — o 'como' que diferencia"
    - intellectual_interest: "O que torna isso intelectualmente interessante"
    - emotional_hook: "Gancho emocional que conecta com as dores/desejos"

  formula: "E-C (P-P+U-M) I-I (Todd Brown E5 Framework)"

  validacao:
    criterios:
      - "Big Idea é NÃO copiável por concorrente?"
      - "Mecanismo Único tem NOME próprio?"
      - "Promessa é ESPECÍFICA (com número ou prazo)?"
      - "Tem prova que sustenta a promessa?"

    se_falhar: |
      ÚNICA EXCEÇÃO ao fluxo unidirecional:
      Se Big Idea não passa nos critérios por falta de prova/tese,
      PODE voltar para Etapa 3 para reforçar pesquisa.
      Máximo 2 iterações. Se após 2 voltas ainda não passa →
      Ajustar tese ou escopo antes de continuar.

    max_iteracoes_volta: 2

  output:
    - big_idea_documento: "Big Idea completa com todos os componentes"
    - mecanismo_unico: "Nome e descrição do mecanismo"

  veto_conditions:
    - "SE mecanismo_unico não tem nome → VETO: Mecanismo sem nome é genérico"
    - "SE promessa é vaga → VETO: Precisa ser específica"
    - "SE iteracoes_volta > 2 → ESCALAR: Ajustar tese ou escopo"

  salvar_em: "<raiz>/businesses/<slug>/outputs/copy/{produto}/big-idea/"
```

---

## ETAPA 5: NARRATIVA

**Objetivo:** Construir a narrativa — como usar tudo em lives, vídeos, aulas.

```yaml
etapa_5:
  name: "Narrativa"
  tipo: "Construção de narrativa"
  agent_principal: "@gary-halbert"
  agents_suporte: ["@andre-chaperon", "@jon-benson"]

  # CHECKPOINT: Antes de começar, mostrar resumo ao usuário
  checkpoint_entrada:
    action: "Apresentar resumo das etapas anteriores antes de construir narrativa"
    mostrar:
      - "Big Idea (Etapa 4): [resumo em 1 frase]"
      - "Tese principal (Etapa 3): [resumo em 1 frase]"
      - "Mecanismo Único: [nome + descrição curta]"
      - "Provas mais fortes: [top 3 do Proof Stack]"
    perguntar: "Quer ajustar algo antes de construir a narrativa?"

  input_obrigatorio:
    - big_idea: "Da Etapa 4"
    - tese_validada: "Da Etapa 3"
    - mapa_dominio: "Da Etapa 2"
    - proof_stack: "Da Etapa 3 (provas organizadas por tier)"

  componentes:
    - arco_narrativo: |
        A história que conecta TUDO:
        - De onde o público está (dor/problema)
        - Pra onde vai (transformação/resultado)
        - Como chega lá (mecanismo único)

    - formatos_aplicacao:
        - live: "Como contar essa história numa live"
        - video: "Como usar num vídeo/VSL"
        - aula: "Como estruturar numa aula"
        - conteudo: "Como fragmentar em peças de conteúdo"
        - email: "Como serializar em sequência de emails"

    - tom_voz: "Como falar sobre isso — qual energia, qual registro"

    - storytelling_elements:
        - origem: "De onde veio essa descoberta/método"
        - conflito: "Qual obstáculo foi superado"
        - epifania: "O momento da virada"
        - prova: "O que prova que funciona"
        - chamada: "O que o público deve fazer"

  output:
    - narrativa_documento: "Narrativa completa com todos os formatos"
    - guia_tom_voz: "Como falar sobre isso em cada canal"

  veto_conditions:
    - "SE arco_narrativo não tem conflito → ALERTA: História sem conflito não engaja"
    - "SE formatos_aplicacao == vazio → VETO: Narrativa precisa ter pelo menos 1 formato"
    - "SE narrativa não usa provas do Proof Stack → ALERTA: Narrativa sem prova é ficção"

  salvar_em: "<raiz>/businesses/<slug>/outputs/copy/{produto}/narrativa/"
```

---

## ETAPA 6: OFERTA (Hormozi)

**Objetivo:** Construir a Grand Slam Offer usando tudo que foi construído até aqui.

```yaml
etapa_6:
  name: "Oferta — Grand Slam Offer"
  tipo: "Construção de oferta"
  agent_principal: "@alex-hormozi"
  agents_suporte: ["@dan-kennedy", "@juliano-torriani"]
  task_existente: "tasks/estrategia/create-offer.md"
  tasks_complementares:
    - "tasks/estrategia/evaluate-offer.md"

  # CHECKPOINT: Mostrar Big Idea e Narrativa antes de construir oferta
  checkpoint_entrada:
    action: "Apresentar resumo das etapas 4 e 5 antes de construir oferta"
    mostrar:
      - "Big Idea: [resumo em 1 frase]"
      - "Mecanismo Único: [nome + descrição]"
      - "Narrativa: [arco resumido]"
      - "Provas mais fortes: [top 3]"
    perguntar: "Quer ajustar algo antes de construir a Grand Slam Offer?"

  input_obrigatorio:
    - mapa_dominio: "Da Etapa 2"
    - tese_e_provas: "Da Etapa 3"
    - big_idea: "Da Etapa 4"
    - narrativa: "Da Etapa 5"

  componentes_hormozi:
    - value_equation:
        dream_outcome: "Resultado dos sonhos — O QUE o cliente consegue"
        perceived_likelihood: "Probabilidade percebida — PROVA que funciona"
        time_delay: "Tempo até resultado — QUANDO consegue"
        effort_sacrifice: "Esforço necessário — QUANTO custa em energia"

    - grand_slam_offer:
        core_offer: "O que está sendo vendido"
        bonuses: "Bônus que aumentam valor percebido"
        guarantees: "Garantias que eliminam risco"
        scarcity: "Escassez REAL (não fabricada)"
        urgency: "Urgência REAL (não fabricada)"
        naming: "Nome da oferta (Magic Naming Formula)"

    - pricing:
        strategy: "Preço baseado em valor, não em custo"
        justification: "10-100x o custo de entrega"

  output:
    - oferta_completa: "Grand Slam Offer documentada"
    - value_stack: "Stack de valor com preços"

  veto_conditions:
    - "SE value_equation não está preenchida → VETO: Oferta incompleta"
    - "SE escassez é fabricada → VETO: Hormozi não aprova escassez falsa"
    - "SE garantia é fraca (7 dias sem contexto) → ALERTA: Garantia que te assusta = garantia boa"
    - "SE preço baseado em custo → VETO: Cobrar baseado em valor"

  salvar_em: "<raiz>/businesses/<slug>/outputs/copy/{produto}/oferta/"
```

---

## ETAPA 7: COPY MESTRE

**Objetivo:** A carta-mãe. Toda argumentação, teses, provas, oferta numa carta de vendas longa. Base pra TUDO.

```yaml
etapa_7:
  name: "Copy Mestre — Carta-Mãe"
  tipo: "Construção de copy longo"
  agent_principal: "@gary-halbert"
  agents_suporte: ["@clayton-makepeace", "@parris-lampropoulos", "@david-deutsch"]
  task_referencia: "tasks/criacao/create-sales-page.md"
  nota_task: "A Copy Mestre usa a estrutura de sales page como base, mas é mais completa — inclui TODA argumentação"

  # CHECKPOINT: Antes de escrever, mostrar plano ao usuário
  checkpoint_entrada:
    action: "Apresentar estrutura da Copy Mestre ao usuário antes de escrever"
    mostrar:
      - "Headline candidata (da Big Idea)"
      - "Tipo de lead escolhido (story/problem/news/question)"
      - "Mecanismo Único: [nome]"
      - "Provas que serão usadas: [top 5 do Proof Stack]"
      - "Oferta: [resumo da Grand Slam Offer]"
    perguntar: "Aprova essa estrutura? Quer ajustar algo antes de escrever?"

  input_obrigatorio:
    - mapa_dominio: "Da Etapa 2"
    - proof_stack: "Da Etapa 3 (Proof Stack organizado por tier)"
    - big_idea: "Da Etapa 4"
    - narrativa: "Da Etapa 5"
    - oferta_completa: "Da Etapa 6"

  definicao: |
    A Copy Mestre é uma carta de vendas LONGA e COMPLETA que contém:
    - Toda a argumentação construída nas etapas anteriores
    - Todas as teses com suas provas
    - A narrativa completa (origem, conflito, epifania, prova)
    - A oferta estruturada (Grand Slam Offer)
    - Headlines, sub-headlines, bullets, CTAs

    É o DOCUMENTO-MÃE que alimenta todos os derivados.
    Se precisar de uma sales page → extrai da Copy Mestre.
    Se precisar de um email → fragmenta da Copy Mestre.
    Se precisar de um ad → puxa um ângulo da Copy Mestre.

  estrutura:
    - secao_1_headline: "Headline principal (extraída da Big Idea)"
    - secao_2_lead: "Abertura que captura atenção (história/dado chocante/pergunta)"
    - secao_3_problema: "Amplificação do problema (dor → agitação → consequência)"
    - secao_4_tese: "Apresentação da tese central com provas"
    - secao_5_mecanismo: "Mecanismo Único — o 'como' que diferencia"
    - secao_6_prova_social: "Depoimentos, cases, dados que provam (do Proof Stack Tier 1)"
    - secao_7_narrativa: "História completa (origem → conflito → epifania)"
    - secao_8_oferta: "Grand Slam Offer com value stack"
    - secao_9_garantia: "Garantia que remove risco (do Proof Stack Tier 4)"
    - secao_10_urgencia: "Urgência/escassez REAL"
    - secao_11_cta: "Chamada pra ação clara e direta"
    - secao_12_ps: "P.S. com reforço de urgência ou benefício"

  validacao:
    obrigatoria:
      - task: "tasks/otimizacao/sugarman-check.md"
        regra: "Mínimo 15 triggers presentes"
      - task: "tasks/otimizacao/audit-copy.md"
        regra: "Auditoria científica — score mínimo 75/100"
    obrigatoria_final:
      - task: "tasks/validacao/validate-copy-oraculo.md"
        regra: "10/10 ou refaz — sem exceção"

  output:
    - copy_mestre_documento: "Carta de vendas longa e completa"
    - indice_secoes: "Índice de seções pra facilitar extração"

  veto_conditions:
    - "SE oferta não está incluída → VETO: Copy Mestre sem oferta não é Copy Mestre"
    - "SE provas não estão incluídas → VETO: Argumentação sem prova é opinião"
    - "SE mecanismo não aparece → VETO: Sem mecanismo é commodity"
    - "SE Sugarman < 15 triggers → REFAZ seções fracas"
    - "SE Hopkins < 75/100 → REFAZ elementos que falharam"
    - "SE Oráculo < 10/10 → REFAZ"

  salvar_em: "<raiz>/businesses/<slug>/outputs/copy/{produto}/copy-mestre/"
```

---

## ETAPA 8: ARSENAIS

**Objetivo:** Gerar Banco de Headlines e Banco de Ângulos/Ganchos a partir de tudo construído.

```yaml
etapa_8:
  name: "Arsenais — Headlines + Ângulos"
  tipo: "Geração em massa"
  agents:
    headlines: "@gary-halbert + @parris-lampropoulos + @gary-bencivenga"
    angulos: "@john-carlton + @david-deutsch + @clayton-makepeace"
  tasks_existentes:
    headlines: "tasks/criacao/create-headlines.md"
    bullets: "tasks/criacao/create-bullets.md"

  # CHECKPOINT: Mostrar Copy Mestre aprovada antes de gerar arsenais
  checkpoint_entrada:
    action: "Confirmar que Copy Mestre passou validação antes de gerar arsenais"
    verificar:
      - "Sugarman Check ≥ 15 triggers"
      - "Hopkins Audit ≥ 75/100"
    se_nao_passou: "Voltar para Etapa 7 e corrigir"

  input_obrigatorio:
    - copy_mestre: "Da Etapa 7"
    - big_idea: "Da Etapa 4"
    - teses: "Da Etapa 3"
    - narrativa: "Da Etapa 5"

  arsenal_1_headlines:
    nome: "Banco de Headlines"
    descricao: |
      Coleção de headlines prontas pra uso em qualquer peça.
      Categorizadas por tipo e formato.

    categorias:
      - tipo: "Curiosidade"
        exemplo: "O método de 3 passos que fez a empresa X produzir 10x mais (sem contratar ninguém)"
      - tipo: "Benefício direto"
        exemplo: "Automatize 80% dos processos da sua empresa em 30 dias"
      - tipo: "Medo/Dor"
        exemplo: "Sua empresa está perdendo R$50k/mês com processos manuais (e você nem sabe)"
      - tipo: "Prova social"
        exemplo: "347 empresas já automatizaram com esse sistema — veja os resultados"
      - tipo: "Pergunta"
        exemplo: "E se você pudesse eliminar 80% do trabalho repetitivo da sua equipe?"
      - tipo: "Como/Tutorial"
        exemplo: "Como usar IA pra fazer sua equipe de 5 render como 20"
      - tipo: "Contraintuitivo"
        exemplo: "Por que contratar mais gente está MATANDO a produtividade da sua empresa"

    quantidade_minima: 30
    formato: "Headline + categoria + contexto de uso"

  arsenal_2_angulos:
    nome: "Banco de Ângulos e Ganchos"
    descricao: |
      Ângulos diferentes de abordagem pro mesmo produto.
      Cada ângulo é uma "lente" diferente sobre a mesma oferta.
      Usados pra ads, conteúdo orgânico, emails, hooks de vídeo.

    tipos_angulo:
      - tipo: "Ângulo de dor"
        descricao: "Foca na dor/problema que o produto resolve"
        exemplo: "Sua equipe gasta 4h/dia em tarefas que uma IA faz em 4 minutos"

      - tipo: "Ângulo de oportunidade"
        descricao: "Foca no ganho/oportunidade que o produto abre"
        exemplo: "Empresas que automatizam agora vão dominar nos próximos 3 anos"

      - tipo: "Ângulo de medo"
        descricao: "Foca no risco de não agir"
        exemplo: "Enquanto você faz manual, seu concorrente já automatizou"

      - tipo: "Ângulo de autoridade"
        descricao: "Foca em credenciais e provas"
        exemplo: "347 empresas, R$12M em resultados, 1 sistema"

      - tipo: "Ângulo de curiosidade"
        descricao: "Foca em gerar curiosidade sobre o método"
        exemplo: "O sistema de 3 camadas que CEOs estão implementando em silêncio"

      - tipo: "Ângulo de história"
        descricao: "Foca em contar uma história que conecta"
        exemplo: "Ele tinha 45 funcionários e operava como se tivesse 200..."

      - tipo: "Ângulo contraintuitivo"
        descricao: "Foca em desafiar uma crença comum"
        exemplo: "Pare de contratar. Comece a automatizar."

      - tipo: "Ângulo de transformação"
        descricao: "Foca no antes/depois"
        exemplo: "De 5h/dia pra 45min: a transformação da empresa X"

    quantidade_minima: 16
    formato: "Ângulo + tipo + headline + contexto de uso (ad/conteúdo/email/vídeo)"

  output:
    - banco_headlines: "30+ headlines categorizadas"
    - banco_angulos: "16+ ângulos com headlines e contexto"

  veto_conditions:
    - "SE headlines < 30 → ALERTA: Arsenal fraco, gerar mais"
    - "SE angulos < 8 → ALERTA: Pouca diversidade de abordagem"
    - "SE todos angulos do mesmo tipo → VETO: Precisa diversidade"

  salvar_em:
    headlines: "<raiz>/businesses/<slug>/outputs/copy/{produto}/arsenais/headlines/"
    angulos: "<raiz>/businesses/<slug>/outputs/copy/{produto}/arsenais/angulos/"
```

---

## ETAPA 9: DERIVADOS (Campanha)

**Objetivo:** Gerar peças de copy específicas a partir da Copy Mestre + Arsenais.

```yaml
etapa_9:
  name: "Derivados — Peças de Campanha"
  tipo: "Extração e adaptação"
  agent_principal: "@copy-chief (distribui pros executores)"

  input_obrigatorio:
    - copy_mestre: "Da Etapa 7"
    - banco_headlines: "Da Etapa 8"
    - banco_angulos: "Da Etapa 8"
    - oferta: "Da Etapa 6"

  derivados_possiveis:
    - tipo: "Sales Page"
      agent: "@gary-halbert ou @clayton-makepeace"
      task: "tasks/criacao/create-sales-page.md"
      extrai_de: "Copy Mestre (adaptado pra formato web)"

    - tipo: "Capture Page"
      agent: "@dan-kennedy"
      task: "tasks/criacao/create-capture-page.md"
      extrai_de: "Big Idea + 1 headline do banco"

    - tipo: "Landing Page"
      agent: "@dan-kennedy"
      task: "tasks/criacao/create-landing-page.md"
      extrai_de: "Big Idea + headline + CTA"

    - tipo: "VSL"
      agent: "@jon-benson"
      task: "tasks/criacao/create-vsl.md"
      extrai_de: "Narrativa + Copy Mestre (formato vídeo)"

    - tipo: "Sequência de Emails"
      agent: "@andre-chaperon ou @ben-settle"
      task: "tasks/criacao/create-email-sequence.md"
      extrai_de: "Narrativa fragmentada + ângulos do banco"

    - tipo: "Soap Opera Sequence"
      agent: "@andre-chaperon"
      task: "tasks/criacao/create-soap-opera-sequence.md"
      extrai_de: "Narrativa serializada em emails"

    - tipo: "Ads"
      agent: "@john-carlton ou @david-deutsch"
      task: "tasks/criacao/create-ad-copy.md"
      extrai_de: "Banco de ângulos + headlines"

    - tipo: "Ads para Mentoria/High-Ticket"
      agent: "@juliano-torriani"
      task: "tasks/criacao/create-mentorship-ads.md"
      extrai_de: "Banco de ângulos + framework Torriani 90/10"

    - tipo: "Conteúdo Orgânico"
      agent: "@dan-koe"
      task: "tasks/criacao/create-organic-content.md"
      extrai_de: "Teses + ângulos adaptados pra formato orgânico"

    - tipo: "Webinar Script"
      agent: "@russell-brunson"
      task: "tasks/vendas/create-webinar-script.md"
      extrai_de: "Narrativa + oferta completa"

    - tipo: "Upsell Page"
      agent: "@gary-bencivenga"
      task: "tasks/criacao/create-upsell-page.md"
      extrai_de: "Oferta + benefícios secundários"

    - tipo: "Downsell Page"
      agent: "@dan-kennedy"
      task: "tasks/criacao/create-downsell-page.md"
      extrai_de: "Oferta simplificada"

    - tipo: "Lead Magnet"
      agent: "@todd-brown"
      task: "tasks/criacao/create-lead-magnet.md"
      extrai_de: "Tese + mecanismo único (versão gratuita)"

    - tipo: "Headlines para campanha"
      task: "tasks/criacao/create-headlines.md"
      extrai_de: "Banco de Headlines (selecionar as melhores)"

    - tipo: "Bullets/Fascinations"
      agent: "@gary-bencivenga"
      task: "tasks/criacao/create-bullets.md"
      extrai_de: "Copy Mestre + Proof Stack"

  validacao_obrigatoria:
    - task: "tasks/validacao/validate-copy-oraculo.md"
      regra: "Todo derivado → Oráculo Torriani (10/10 ou refaz)"
    - task: "tasks/otimizacao/sugarman-check.md"
      regra: "Todo derivado → Sugarman Check (mín 15 triggers)"
    - task: "tasks/otimizacao/audit-copy.md"
      regra: "Todo derivado → Hopkins Audit (score mín 80/100)"
    - referencia: "data/manual-craft.md"
      regra: "Todo derivado → Manual de Craft (regras de escrita)"

  salvar_em: "<raiz>/businesses/<slug>/outputs/campanhas/{campanha}/{tipo-derivado}/"
```

---

## Persistência e Reuso

```yaml
persistencia:
  estrutura_pastas:
    <raiz>/businesses/<slug>/outputs/copy/{produto}/:  # gate READY antes de gravar
      mapa-dominio/:
        - "mapa-dominio.md (PERSISTENTE — reutilizável entre campanhas)"
      pesquisas/:
        - "teses.md"
        - "dossie-provas.md"
        - "pesquisas-internet.md"
      big-idea/:
        - "big-idea.md"
        - "mecanismo-unico.md"
      narrativa/:
        - "narrativa.md"
        - "guia-tom-voz.md"
      oferta/:
        - "grand-slam-offer.md"
        - "value-stack.md"
      copy-mestre/:
        - "copy-mestre.md (DOCUMENTO-MÃE)"
        - "indice-secoes.md"
      arsenais/:
        headlines/:
          - "banco-headlines.md"
        angulos/:
          - "banco-angulos.md"
      "{campanha}/":
        - "{tipo-derivado}/ (peças geradas)"

  consulta_automatica: |
    Quando o Copy Chief recebe um pedido de copy, SEMPRE verificar:
    1. Existe <raiz>/businesses/<slug>/outputs/copy/{produto}/mapa-dominio/ ?
    2. Se SIM → Carregar e oferecer Operação Tática
    3. Se NÃO → Iniciar Operação Completa

    Quando existe Mapa do Domínio + Copy Mestre:
    → Derivados podem ser gerados a qualquer momento sem repetir etapas 1-7
```

---

## Resumo de Agents por Etapa

| Etapa | Agent Principal | Agents Suporte | Task Referência |
|-------|----------------|----------------|-----------------|
| 1. Ideia | Copy Chief | — | — (elicitação) |
| 2. Mapa do Domínio | Kennedy + Torriani | Schwartz (awareness/sophistication) | `create-brand-dna.md` |
| 3. Pesquisa + Teses | Ogilvy + Georgi + Bencivenga | Todd Brown, Hopkins | `copysearch.md` + `rmbc-method.md` + `create-proof-stack.md` |
| 4. Big Idea | Todd Brown | Schwartz, Georgi | `create-big-idea.md` |
| 5. Narrativa | Halbert | Chaperon, Benson | — (construção guiada) |
| 6. Oferta | Hormozi | Kennedy, Torriani | `create-offer.md` |
| 7. Copy Mestre | Halbert | Makepeace, Lampropoulos, Deutsch | `create-sales-page.md` (base) |
| 8. Arsenais | Halbert + Bencivenga (headlines), Carlton + Deutsch (ângulos) | Lampropoulos | `create-headlines.md` + `create-bullets.md` |
| 9. Derivados | Copy Chief (distribui) | Todos os executores conforme tipo | 15 tasks em `tasks/criacao/` |

## Resumo de Tasks por Etapa

| Etapa | Tasks Disponíveis |
|-------|-------------------|
| 3. Pesquisa | `copysearch.md`, `rmbc-method.md`, `create-proof-stack.md` |
| 4. Big Idea | `create-big-idea.md`, `create-unique-mechanism.md` |
| 6. Oferta | `create-offer.md`, `evaluate-offer.md` |
| 7. Copy Mestre | `create-sales-page.md`, `sugarman-check.md`, `audit-copy.md` |
| 8. Arsenais | `create-headlines.md`, `create-bullets.md` |
| 9. Derivados | `create-sales-page.md`, `create-capture-page.md`, `create-vsl.md`, `create-email-sequence.md`, `create-ad-copy.md`, `create-mentorship-ads.md`, `create-organic-content.md`, `create-soap-opera-sequence.md`, `create-upsell-page.md`, `create-downsell-page.md`, `create-landing-page.md`, `create-lead-magnet.md`, `create-webinar-script.md` |

---

## Comandos Rápidos

```yaml
comandos:
  - "*operacao-completa → Iniciar pipeline completo (9 etapas)"
  - "*operacao-tatica → Iniciar modo rápido (público quente)"
  - "*mapa-dominio → Criar/consultar Mapa do Domínio"
  - "*copy-mestre → Ir direto pra construção da Copy Mestre (se tiver insumos)"
  - "*arsenais → Gerar headlines + ângulos (se tiver Copy Mestre)"
```

---

*"Impossibilitar caminhos. Cada etapa tem veto condition. Nada avança sem o necessário."*
*— Pedro Valério*

## Quality Gates
- Premissa-core.md carregada antes de qualquer copy
- Diagnostico de awareness e sofisticacao completo antes de execucao
- Oraculo Torriani 10/10 obrigatorio antes de entrega
