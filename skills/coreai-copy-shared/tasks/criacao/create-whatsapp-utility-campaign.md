# Task: create-whatsapp-utility-campaign

```yaml
nome: create-whatsapp-utility-campaign
versao: "1.0.0"
tipo: task
categoria: criacao
squad: copy
executor_padrao: dan-kennedy (via copy-chief)
canal: WhatsApp Business API Oficial (Meta)
objetivo: Criar templates de mensagem categoria UTILITY novos, aprovaveis pela Meta, para qualquer cliente e qualquer oferta
criado_em: "2026-08-18"
origem: >
  Formaliza como task o metodo que ja existia como conhecimento: o banco de padroes
  (engenharia reversa dos 169 templates pre-aprovados da Meta) e o metodo de 6 passos
  da Parte 3 do swipe. Antes desta task, o saber existia mas nao havia comando invocavel.
```

---

## Ativos obrigatórios (ler ANTES de escrever qualquer template)

| Ativo | Path | O que dá |
|---|---|---|
| Banco de padrões | `../../data/banco-templates-utility-whatsapp.yaml` | Os 8 padrões estruturais (P1 a P8), a regra de ouro e o contexto econômico |
| Swipe completo | `../../swipe/templates-utility-whatsapp.md` | Os exemplos reais dos 169 da Meta + a PARTE 3 (método de 6 passos) + tabela de erros que reprovam |
| Workflow de sequência | `../../workflows/convite-reuniao-diagnostico.md` | Quando o pedido for uma régua/sequência completa, não templates avulsos |
| Exemplo aplicado | `[exemplo de cliente não empacotado]` | Output de referência de campanha real |

## Regra de ouro (inegociável)

Utility só é aprovado quando a mensagem se refere a uma TRANSAÇÃO QUE JÁ EXISTE.
O lead precisa ter praticado um ato real (formulário, palavra-chave, pedido, compra,
agendamento). Sem ato, é Marketing. Tentar disfarçar prospecção fria de Utility
derruba a conta do cliente. Esta task REPROVA qualquer pedido sem ato identificável.

---

## Inputs (o copy-chief coleta antes de despachar)

1. **Cliente** e voz (contexto.md das sources do gate e `negocios/<slug>/cerebro/areas/marketing/contexto/brand.yaml`, campo voice_dna)
2. **O ato real** que o lead praticou (a transação que o Utility notifica)
3. **Objetivo da mensagem** (confirmar, lembrar, destravar, reagendar, expirar, registrar, feedback, avisar)
4. **Dados reais disponíveis**: protocolo, datas, nomes de variável e exemplo real de cada uma
5. **Quantidade** de templates e se há sequência (se sim, considerar o workflow de convite)

## Passo a passo (o método de 6 passos, executado pelo Dan Kennedy)

1. **Ache o ato real.** Sem ato, devolver ao copy-chief com a recomendação Marketing.
2. **Escolha o padrão** no banco: P1 Confirmação · P2 Lembrete · P3 Status pendente · P4 Reagendamento · P5 Expiração · P6 Solicitação registrada · P7 Feedback · P8 Aviso.
3. **Escreva o estado, não a venda.** Fato com data e protocolo, zero adjetivo.
4. **Peça uma resposta, não uma decisão.** O template abre a janela de 24h; quem vende é a conversa que vem depois.
5. **Filtros:** nenhuma palavra da coluna "reprova" do swipe, prazos só se reais, zero travessão, zero emoji, botão com ação operacional ("Ver solicitação", "Confirmar dados"), variável nunca no começo nem no fim, nunca duas variáveis coladas, corpo até 1024 caracteres.
6. **Dados de submissão:** slug em snake_case (`{cliente}_{padrao}_{contexto}`), categoria UTILITY, idioma pt_BR, exemplo real por variável.

## Validação (obrigatória, nesta ordem)

1. `legacy/[integração externa não empacotada]` + `anti-ia-structural.mjs` (zero violações)
2. Cliente Torriani: oráculo 10/10. Outros clientes: fidelidade à voz do cliente.
3. Checklist Meta do swipe (tabela "Erros que derrubam a aprovação"): passar item a item.

## Output

Arquivo em `[exemplo de cliente não empacotado]`
no padrão do exemplo do Diego: um card por template com nome/slug, categoria, gatilho (o ato),
botões, corpo pronto pra colar na tela "Criar Template" da Meta, e as MENSAGENS DE RESPOSTA
de cada botão (o que a pessoa recebe ao clicar). Registrar a peça no portal do cliente quando houver.

## Veto conditions

```yaml
veto_conditions:
  - "Pedido sem ato real identificável → REPROVA (recomendar Marketing)"
  - "Adjetivo de venda no corpo → REPROVA e reescreve"
  - "Prazo não rastreável a política real → REMOVER"
  - "Travessão ou emoji → REPROVA (regra de marca)"
  - "Variável no começo/fim ou duas coladas → corrigir antes de entregar"
```
