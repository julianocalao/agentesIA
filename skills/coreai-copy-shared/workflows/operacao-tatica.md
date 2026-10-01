# Workflow: Operação Tática

```yaml
workflow:
  name: operacao-tatica
  description: "Pipeline rápido de copy — público quente, Mapa do Domínio existente"
  estimated_time: "1-3 horas"
  complexity: media
  mode: express
  counterpart: operacao-completa

use_cases:
  - "Oferta pra público quente (já comprou ou já conhece)"
  - "Produto que já tem Mapa do Domínio salvo"
  - "Campanha rápida — promoção, oferta especial, upsell"
  - "Nova campanha de produto existente"
  - "Derivar novas peças de uma Copy Mestre existente"
```

---

## Visão Geral

A Operação Tática é o modo rápido. Só funciona quando já existe base construída (Mapa do Domínio, e idealmente Copy Mestre + Arsenais). Pula toda a construção e vai direto pro que precisa.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    OPERAÇÃO TÁTICA — MODO RÁPIDO                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PRÉ-REQUISITO          OPÇÕES DE ENTRADA                              │
│                                                                         │
│  Mapa do Domínio ──┬──▶ OFERTA (se nova oferta)                       │
│  (já existe)       │                                                    │
│                    ├──▶ COPY MESTRE (se já tem oferta)                 │
│  Copy Mestre ──────┤                                                    │
│  (se existe)       ├──▶ ARSENAIS (se já tem Copy Mestre)              │
│                    │                                                    │
│  Arsenais ─────────┴──▶ DERIVADOS (direto pra peça final)             │
│  (se existem)                                                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔒 CONDIÇÃO DE ENTRADA

```yaml
condicao_entrada:
  obrigatorio:
    - mapa_dominio_existe: true
      verificar: "<raiz>/businesses/<slug>/outputs/copy/{produto}/mapa-dominio/"
      se_nao_existe: "REDIRECIONAR para Operação Completa"

  recomendado:
    - publico_quente: true
      descricao: "Público que já te conhece, já comprou, ou já consumiu conteúdo"

  veto:
    - "SE mapa_dominio não existe → VETO: Não é possível Operação Tática sem base"
    - "SE público é frio E não tem Copy Mestre → REDIRECIONAR: Use Operação Completa"
```

---

## Triagem Rápida

```yaml
triagem:
  trigger: "Copy Chief identifica que Mapa do Domínio existe"
  elicit: true

  perguntas:
    - id: "o_que_precisa"
      pergunta: "O que você precisa criar?"
      opcoes:
        - "1. Nova oferta pra produto existente → Etapa 6 (Oferta Hormozi)"
        - "2. Copy Mestre (carta-mãe) → Etapa 7 (precisa ter oferta)"
        - "3. Headlines e ângulos novos → Etapa 8 (precisa ter Copy Mestre)"
        - "4. Peça específica (sales page, email, ad, etc.) → Etapa 9 (Derivados)"
      obrigatorio: true

    - id: "contexto"
      pergunta: "Me dá o contexto rápido — pra quem, pra quê, qual urgência?"
      tipo: "texto_livre"
      obrigatorio: true

  roteamento:
    "1": { entrada: "etapa_6", carrega: ["mapa-dominio", "big-idea", "narrativa"] }
    "2": { entrada: "etapa_7", carrega: ["mapa-dominio", "oferta", "big-idea", "narrativa"] }
    "3": { entrada: "etapa_8", carrega: ["copy-mestre", "big-idea"] }
    "4": { entrada: "etapa_9", carrega: ["copy-mestre", "arsenais", "oferta"] }
```

---

## Execução por Ponto de Entrada

### Entrada pela Etapa 6 — Nova Oferta

```yaml
entrada_oferta:
  pre_carga:
    - "Carregar Mapa do Domínio existente"
    - "Carregar Big Idea (se existir)"
    - "Carregar Narrativa (se existir)"
  fluxo: "Oferta → Copy Mestre → Arsenais → Derivados"
  agent: "@alex-hormozi"

  checkpoint:
    gate: "Oferta criada com estrutura Hormozi completa"
    criteria:
      - "Oferta tem valor stack definido"
      - "Preço e garantia documentados"
      - "Mapa do Domínio foi carregado e referenciado"
    veto_conditions:
      - "SE Mapa do Domínio não carregou → HALT: base corrompida ou ausente"
      - "SE oferta não tem valor stack → BLOCK: oferta incompleta"
    human_review: true
    message: "Revisar oferta antes de avançar para Copy Mestre"
```

### Entrada pela Etapa 7 — Copy Mestre

```yaml
entrada_copy_mestre:
  pre_carga:
    - "Carregar Mapa do Domínio"
    - "Carregar Oferta existente"
    - "Carregar Big Idea + Narrativa (se existirem)"
  fluxo: "Copy Mestre → Arsenais → Derivados"
  agent: "@gary-halbert"
  veto: "SE oferta não existe → Criar oferta primeiro (Entrada Etapa 6)"

  checkpoint:
    gate: "Copy Mestre produzida com estrutura completa"
    criteria:
      - "Copy Mestre segue estrutura AIDA ou equivalente"
      - "Big Idea integrada na headline/lead"
      - "Mecanismo único presente e articulado"
      - "Oferta referenciada corretamente"
    veto_conditions:
      - "SE oferta não existe → VETO: Criar oferta primeiro (Etapa 6)"
      - "SE Copy Mestre não tem mecanismo → BLOCK: copy genérica sem diferenciação"
    human_review: true
    message: "Revisar Copy Mestre antes de gerar Arsenais"
```

### Entrada pela Etapa 8 — Arsenais

```yaml
entrada_arsenais:
  pre_carga:
    - "Carregar Copy Mestre"
    - "Carregar Big Idea"
  fluxo: "Arsenais → Derivados"
  agents: "@halbert + @bencivenga (headlines), @carlton + @koe (ângulos)"
  veto: "SE Copy Mestre não existe → Criar Copy Mestre primeiro (Entrada Etapa 7)"

  checkpoint:
    gate: "Arsenais gerados com volume e variedade suficientes"
    criteria:
      - "Mínimo 10 headlines geradas"
      - "Mínimo 5 ângulos de abordagem criados"
      - "Headlines derivam da Big Idea (não genéricas)"
      - "Ângulos cobrem diferentes personas/dores"
    veto_conditions:
      - "SE Copy Mestre não existe → VETO: Criar Copy Mestre primeiro (Etapa 7)"
      - "SE headlines < 5 → BLOCK: volume insuficiente para teste"
    human_review: false
    message: "Arsenais prontos — selecionar melhores para Derivados"
```

### Entrada pela Etapa 9 — Derivado Direto

```yaml
entrada_derivado:
  pre_carga:
    - "Carregar Copy Mestre"
    - "Carregar Arsenais (headlines + ângulos)"
    - "Carregar Oferta"
  fluxo: "Gerar peça específica"
  agent: "Copy Chief distribui pro executor ideal"

  tipos_derivado:
    - "Sales Page → @halbert ou @makepeace"
    - "Capture Page → @kennedy"
    - "VSL → @benson ou @ry-schwartz"
    - "Email Sequence → @chaperon ou @settle"
    - "Ads → @carlton ou @koe"
    - "Conteúdo Orgânico → @koe"
    - "Webinar → @kern ou @brunson"

  veto: "SE Copy Mestre não existe → ALERTA: Derivado sem base pode ser fraco. Sugerir criar Copy Mestre."

  checkpoint:
    gate: "Derivado finalizado e validado"
    criteria:
      - "Peça segue metodologia do agente executor"
      - "Copy Mestre e Arsenais foram referenciados"
      - "Formato adequado ao canal (email, page, ad, etc.)"
    veto_conditions:
      - "SE Copy Mestre não existe E derivado é high-stakes → BLOCK: criar Copy Mestre primeiro"
      - "SE peça não passou pelo Oráculo → BLOCK: validação obrigatória"
    human_review: true
    message: "Revisar derivado final antes de entrega"
```

---

## Validação

```yaml
validacao:
  regra: "Todo output da Operação Tática passa pela mesma validação da Completa"
  obrigatorio:
    - "Oráculo Torriani: 10/10"
    - "Sugarman Check: mín 15 triggers"
    - "Manual de Craft: regras de escrita"

  nota: |
    Operação Tática é RÁPIDA, não é RELAXADA.
    A validação é idêntica à Operação Completa.
    Corta tempo de construção, não corta qualidade.
```

---

## Comandos Rápidos

```yaml
comandos:
  - "*operacao-tatica → Iniciar modo rápido"
  - "*tatica-oferta → Entrada pela Etapa 6 (nova oferta)"
  - "*tatica-copy-mestre → Entrada pela Etapa 7"
  - "*tatica-arsenais → Entrada pela Etapa 8"
  - "*tatica-derivado {tipo} → Entrada pela Etapa 9 (peça específica)"
```

---

*"Rápido não é desleixado. É eficiente. A base já existe — usa ela."*
*— Pedro Valério*

## Quality Gates
- Premissa-core.md carregada antes de qualquer copy
- Diagnostico de awareness e sofisticacao completo antes de execucao
- Oraculo Torriani 10/10 obrigatorio antes de entrega
