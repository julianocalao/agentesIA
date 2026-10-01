---
name: use
description: >
  Troca o business ativo do ContextOS deste pacote. Pergunta a raiz de
  contexto (não assume path fixo), lista businesses dentro dela e atualiza
  a seleção ativa via ../coreai-contexto/scripts/contextos.py. Acionar
  quando o usuário disser "trocar empresa", "use empresa X", "ativar
  business", ou /coreai:use.
---

# Use Business

Troca a empresa ativa dentro do ContextOS já existente. Não cria contexto novo:
se não houver nenhum, encaminhe para `coreai-contexto`.

## Passos

### 1. Resolver a raiz de contexto

Pergunte a raiz de contexto (`--root`) se não vier de uma sessão anterior. Nunca
assumir path fixo de máquina.

> **Padrão cérebro** (a raiz tem `negocios/<slug>/cerebro/`): a troca é por máquina e não toca no
> `config.json` versionado. Liste com `node "$ROOT/nucleo/motor/negocio-ativo.mjs" listar` e troque com
> `node "$ROOT/nucleo/motor/negocio-ativo.mjs" trocar <slug>`. Os passos abaixo valem só para o layout clássico
> (o `contextos.py` recusa `set-active` no padrão cérebro).

### 2. Listar businesses

```bash
python3 ../coreai-contexto/scripts/contextos.py --root "$ROOT" status
```

### 3. Apresentar e pedir escolha

Mostre numerado. Aceite número ou nome direto.

### 4. Atualizar a seleção ativa

```bash
python3 ../coreai-contexto/scripts/contextos.py --root "$ROOT" set-active --business "<slug>"
```

### 5. Confirmar

```
Business ativo: <slug>
Raiz: <ROOT>/businesses/<slug>/
```

## Edge cases

- Nenhuma raiz de contexto existente → sugerir `coreai-contexto`.
- Nome inválido → re-perguntar.
