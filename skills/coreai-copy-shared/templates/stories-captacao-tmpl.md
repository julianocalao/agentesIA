# Template — Stories de Captação (Torriani)

> **Tipo:** template de copy (peça, não funil) · **Squad:** copy
> **Gatilho:** "stories de captação", "story único" (a peça), "stories de captação no formato do Torriani"
> **NÃO confundir com:** `workflows/funil-story-unico.md` (esse é o FUNIL macro: 48h silêncio →
> story → ManyChat → isca → reunião → venda). ESTE arquivo é só a PEÇA: como se escreve o story.
> **Task de execução:** `tasks/create-stories-captacao.md`
> **Template HTML de saída:** `templates/stories-captacao-html-tmpl.html`

---

## 1. O que é um Story de Captação

UM único story do Instagram (uma tela) que entrega uma mensagem completa e leva a pessoa a
mandar uma palavra-chave no Direct. Cada story é autossuficiente: a pessoa entende tudo numa
tela só. Trabalha-se um BANCO de variações (10 a 20), uma postada por dia/ciclo.

**Filosofia:** foco total numa mensagem = máxima conversão. Não é carrossel, não é sequência
narrativa, não é o funil inteiro. É a peça mínima e completa.

---

## 2. Estrutura canônica (3 blocos numa tela)

| Bloco | Função | Regra |
|-------|--------|-------|
| **ABERTURA** | Chamada magnética. Para o dedo. Promessa ou dor específica. | 1 a 2 linhas. A primeira coisa que a pessoa lê. Curiosidade ou benefício concreto. |
| **CONTEXTO** | A isca + o desejo + a prova. O que a pessoa recebe se responder. | 1 a 2 linhas. Conecta a abertura à isca (relatório, guia, diagnóstico, reunião). Número real quando houver. |
| **CTA** | A ação. Palavra-chave clara pro Direct. | 1 linha. Simples e memorável. Ex: 'Me manda "AGENTE" aqui'. |

### Esqueleto
```
[ABERTURA: promessa/dor específica, 1-2 linhas]

[CONTEXTO: a isca que resolve + prova/número, 1-2 linhas]

Me manda "[PALAVRA-CHAVE]" aqui
```

---

## 3. Os 5 tipos de abertura (alternar entre eles no banco)

1. **"Como [resultado] em [prazo]"** — ex: "Como colocar a IA pra trabalhar no seu negócio nos próximos 7 dias."
2. **Número/conta real** — ex: "R$450 mil por ano economizados trocando funcionário por agente de IA."
3. **Dor específica** — ex: "Como parar de perder venda por falta de follow-up."
4. **Caso real (estudo de caso)** — ex: "R$172 mil recuperados num ano segurando cliente com IA."
5. **Tese/urgência de mercado** — ex: "Em 18 meses, a IA vai separar quem fica de quem sai do mercado."

> Um bom banco mistura os 5 tipos. Não repetir o mesmo tipo em sequência.

---

## 4. Regras de escrita (voz Torriani)

- **Avatar Ferrari:** empresário que fatura 100k+/mês, tem time, é refém do negócio. Falar com ele.
- **Número específico vence adjetivo:** "R$172 mil", "12 segundos", "de 24 pra 48 clientes". Nunca "muito", "vários".
- **A isca tem que ser concreta:** relatório, guia, estudo de caso, diagnóstico, reunião. Algo que a pessoa "recebe".
- **Uma ideia por story.** Não empilhar.
- **Linguagem falada,** como quem manda áudio. Sem corporativês.
- **ZERO travessão. ZERO emoji no corpo.** (raio ⚡ só se for bordão de fechamento, e geralmente não entra no story curto).
- **CTA = 1 palavra-chave** em CAIXA ALTA, sempre a mesma no banco inteiro.
- **Sem clichê de guru** (ver `data/` cliches). Sem "segredo que ninguém te conta", "transforme sua vida", etc.

---

## 5. Exemplos-ouro (referência canônica — copiar o PADRÃO, não o conteúdo)

### Exemplo A — Recompensa "O Time Que Nunca Dorme" (palavra: AGENTE)
```
01 | ABERTURA: Como colocar a IA pra trabalhar no seu negócio nos próximos 7 dias.
     CONTEXTO: Montei um relatório com 30 estudos de caso de empresários brasileiros que já fizeram isso.
     CTA: Me manda "AGENTE" aqui

05 | ABERTURA: R$450 mil por ano economizados trocando funcionário por agente de IA.
     CONTEXTO: Fiz um relatório com a conta real e os 30 agentes que substituem um time de 5 pessoas.
     CTA: Me manda "AGENTE" aqui

14 | ABERTURA: Em 18 meses, a IA vai separar quem fica de quem sai do mercado.
     CONTEXTO: Fiz um relatório mostrando o que quem sai na frente já está instalando no negócio hoje.
     CTA: Me manda "AGENTE" aqui
```

### Exemplo B — "Board de Sucesso do Cliente" (palavra-chave própria)
```
01 | ABERTURA: Tenho um Board de IA com 6 especialistas que cuidam da retenção da tua base mensal.
     CONTEXTO: Tira renovação de 15% pra 40%, sem tu ter que virar atendente do próprio aluno.

05 | ABERTURA: Tenho um Detector de Churn de IA que avisa antes do cliente pedir pra sair.
     CONTEXTO: Faz parte de um Board com 6 especialistas que cuidam de toda a retenção da tua base.
```

> Arquivos originais (referência histórica do pacote de origem; não existem nesta instalação):
> - `outputs/copys/torriani/campanhas/funcionarios-ia-empresarios-mai26/mensagens-captacao-stories/`
> - `outputs/copys/torriani/campanhas/board-sucesso-cliente/stories/`

---

## 6. Quantidade e uso

- **Gerar 10 a 20 variações** por banco (default: 15).
- Postar **1 por dia ou a cada 2 dias**, alternando os tipos de abertura.
- Fundo de vídeo casual (palco, escritório, mesa, café).
- Quem responde a palavra-chave recebe a isca na DM e entra no fluxo de conversão.
- Marcar "usado" depois de postar (o HTML controla isso).

---

## 7. Validação obrigatória (toda peça)

1. **Filtro Anti-IA** (`scripts/anti-ia-validate.mjs`): exit 0 ou refaz.
2. **Oráculo Torriani** (`checklists/oraculo-torriani.md`): 10/10 ou refaz.
3. **Sugarman** (`checklists/sugarman-30-triggers.md`): mínimo 15 triggers no banco.

> Copy 10/10 ou refaz. Zero meio-termo.
