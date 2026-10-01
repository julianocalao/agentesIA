---
name: coreai-contexto
description: ContextOS original — bootstrap multiempresa, 30 templates, coleta quick/deep e enriquecimento com fontes. Inicializa contexto sem inventar dados.
---
# CoreAI:Contexto — ContextOS

> **Padrão cérebro:** se a raiz tiver `negocios/<slug>/cerebro/`, esta skill só faz `status`.
> Criar negócio, entrevistar, importar respostas e consolidar passam a ser da skill `coreai-contextos`
> (CoreAI:ContextOS:Criar, Perguntar, Status); o `contextos.py` recusa os outros comandos nessa raiz,
> porque recriaria em `businesses/<slug>/` o formato antigo (`context/`, `brand-dna/`, `evidence/`).
> Nesse padrão o `businesses/<slug>/contexto.md` é gerado a partir do cérebro, não pelo `consolidate`.

Use esta skill para construir e enriquecer ContextOS. Biblioteca fora do cliente; raiz explicitamente escolhida pelo usuário. Layout `<ROOT>/businesses/<slug>`. Nunca produzir `contexto.md` vazio ou com placeholders para liberar outros agentes.

Leia `references/context-create-method.md` integralmente para o método de seis fases, gates de 85%, entrevistas, propagação de marca, inteligência e validação cruzada. Leia `references/context-quick-method.md`, `references/context-deep-method.md` e `references/context-enrich-method.md` conforme a rota. Os 30 templates legítimos ContextOS e os bancos originais estão incluídos. As instruções de paths/comandos nesta entrada prevalecem sobre nomes históricos nos métodos.

## Execução local

Python 3.10+ e PyYAML (`requirements.txt`), instalar em ambiente virtual escolhido pelo usuário. Não instalar implicitamente. Script relativo à própria pasta da skill:

```sh
python scripts/contextos.py --root /CAMINHO/contextos init
python scripts/contextos.py --root /CAMINHO/contextos add-business --business empresa
python scripts/contextos.py --root /CAMINHO/contextos set-active --business empresa
python scripts/contextos.py --root /CAMINHO/contextos status
python scripts/contextos.py --root /CAMINHO/contextos questions --business empresa --mode quick
```

`init`/`add-business` preservam arquivos existentes; `set-active` é a mudança explícita de seleção. Configuração canônica é `config.json`, com schema original e `active_business`. Não criar outra configuração concorrente. Sem raiz, perguntar; múltiplas empresas sem seleção: perguntar. Não inferir pelo diretório de trabalho.

## Coleta real

Pergunte uma questão ou pequeno lote, em português, mantendo chaves YAML originais inglesas. Quick: 25 questões; deep: banco completo de nove fases. `questions --mode deep` retorna IDs, fase e estado answered; retomar pelas não respondidas. Aceitar pausar/pular sem inventar. Não é necessário terminar deep para contexto inicial; não alegar 85% sem contar campos reais excluindo metadata/defaults.

1. Salvar respostas, transcrição de áudio ou trecho documental real em `businesses/<slug>/sources/` com consentimento. Não colocar segredos.
2. Mapear apenas respostas sustentadas ao `id` retornado por questions. Preparar lista JSON:
   `[{"id":"context/company-profile.yaml::company_essence.trade_name","value":"Nome real","source":"sources/entrevista.md"}]`.
3. Executar `import-answers --business empresa --answers /caminho/respostas.json` com a mesma raiz. Números e listas devem ser JSON tipados. Conflitos são bloqueados, não sobrescritos.
4. Mostrar síntese, lacunas e fontes ao usuário. Após revisão explícita, `consolidate --business empresa --reviewed`. Exige nome, descrição, ICP e modelo de preço respondidos com fonte. Este mínimo de bootstrap não equivale ao gate de 85% do método completo.
5. Executar o gate de `../coreai-shared/scripts/gate.py` para o agente consumidor, com output dentro da empresa. Gate estrutural não certifica semântica.

## Método completo e enriquecimento

Seguir fases originais: empresa → fundador/credenciais → empresa/time → ICP/diagnóstico → marca/preço → síntese e cruzamentos. Deep estende stack e IA. Propagar marca e criar authority-story apenas com evidências, apresentando mudanças para revisão. Templates permanecem vazios até haver fonte.

Para enrich: website e dados públicos identificados, 3–5 páginas relevantes, URL/data/confiança por afirmação. Ferramenta web/Drive depende do ambiente e autorização; não há connector automático neste pacote. Importar transcrições fornecidas; não afirmar transcrição nativa de áudio. Registro em sources e inteligência da empresa, nunca em skills globais. Não executar os scripts shell históricos descritos nos métodos: usar bootstrap acima.

## Limites concretos

CLI implementa bootstrap, seleção, questionário retomável por respostas, importação tipada e consolidado rastreável. Entrevistas, síntese, propagação de marca, auditoria semântica e enriquecimento continuam workflows do agente, não automações Python. Atualizações que conflitam exigem revisão manual; CLI não oferece overwrite. Consulte README.md.
