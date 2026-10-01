# Referência técnica para o agente

Execute estes procedimentos com suas ferramentas. Não entregue comandos para o aluno copiar. O aluno apenas abre o aplicativo, concede acesso à pasta e conclui os logins necessários.

# Preparar o computador e instalar o kit

## 1. Escolher o ambiente
Abra Terminal no Mac ou PowerShell no Windows. Use Claude Code ou Codex com acesso à pasta local do kit. O chat comum não executa automaticamente scripts locais. Tenha a pasta agentesIA extraída num lugar permanente.

Confira Python 3.10+ com `python3 --version` (Windows: `py -3 --version`) e Node com `node --version` e `npm --version`. Se faltar, instale pelos sites [Python](https://www.python.org/downloads/) e [Node](https://nodejs.org/en/download), reabra o terminal e confira novamente. No Windows habilite Python no PATH no instalador.

Instale e entre no ambiente escolhido seguindo [Claude Code](https://code.claude.com/docs/en/quickstart) ou [Codex CLI](https://developers.openai.com/codex/cli). Confira `claude --version` ou `codex --version`, abra o programa, conclua o login no navegador e peça uma resposta simples. Erro de versão/modelo exige atualizar pelo método oficial de instalação antes de continuar.

## 2. Instalar as skills disponíveis
No terminal, entre na pasta agentesIA com `cd` seguido do caminho da sua pasta entre aspas. Execute:

```sh
python3 skills/coreai-setup/scripts/doctor.py
python3 skills/coreai-setup/scripts/install.py --source skills --list
python3 skills/coreai-setup/scripts/install.py --source skills --target both coreai-setup coreai-contexto coreai-criativos coreai-carousel-creator
python3 skills/coreai-setup/scripts/install.py --source skills --target both --status
```

No Windows substitua `python3` por `py -3`. Para um único ambiente, troque `both` por `claude` ou `codex`. O kit limpo contém essas quatro skills; não confundir com o catálogo antigo de 30.

Resultado esperado: links instalados sem conflitos e status correspondente. Abra nova sessão e procure `coreai-setup` e `coreai-contexto`. Peça para ler a skill e confirmar seu caminho. Link criado sozinho não comprova descoberta pelo aplicativo. Os links dependem de manter a pasta original no lugar. No Windows, erro de permissão de symlink pode exigir Modo de Desenvolvedor. Conflito com instalação antiga exige conferir o destino antes de substituir; não apagar todas as skills.

## 3. Dependências do ContextOS
Na raiz do kit:

```sh
python3 -m venv .venv
```

Ative no Mac/Linux com `source .venv/bin/activate`; no PowerShell com `.venv\Scripts\Activate.ps1`. Se a política local impedir a ativação, use diretamente `.venv\Scripts\python.exe` nos comandos seguintes.

```sh
python -m pip install -r skills/coreai-contexto/requirements.txt
python skills/coreai-contexto/scripts/contextos.py --help
```

Resultado esperado: ajuda com init, add-business e status. Erro de módulo yaml indica que o pip foi executado em outro Python; use `python -m pip` dentro do ambiente.

## 4. Iniciar a empresa
> Com a skill `coreai-contextos` instalada, use-a (padrão cérebro) em vez dos comandos abaixo, que criam o layout clássico.

Escolha um caminho absoluto para guardar seus dados, substitua `/CAMINHO/contextos` e `minha-empresa` abaixo pelos seus valores. No Windows use caminho como `C:/Users/SEU-USUARIO/contextos`.

```sh
python skills/coreai-contexto/scripts/contextos.py --root /CAMINHO/contextos init
python skills/coreai-contexto/scripts/contextos.py --root /CAMINHO/contextos add-business --business minha-empresa
python skills/coreai-contexto/scripts/contextos.py --root /CAMINHO/contextos set-active --business minha-empresa
python skills/coreai-contexto/scripts/contextos.py --root /CAMINHO/contextos status
```

Agora ative coreai-contexto e diga: “Minha base está em [caminho], o cliente é [slug]. Conduza a entrevista quick, guarde as fontes e apresente a síntese para minha revisão.” A skill explica importação das respostas e consolidação. Não preencher com dados inventados para passar no teste. Antes da revisão, contexto incompleto permanece bloqueado.

## 5. Preparar carrosséis
Para a skill incluída:

```sh
npm --prefix skills/coreai-carousel-creator ci
npm --prefix skills/coreai-carousel-creator exec -- playwright install chromium
```

Resultado esperado: dependências e navegador instalados. Depois de consolidar o ContextOS, peça à skill um carrossel de teste salvo dentro de `businesses/SEU-CLIENTE/outputs/`. Abra o HTML e a imagem gerada. Instalação do Chromium não comprova renderização.

## 6. O que separar antes da aula
Tenha acesso ao negócio, produto/oferta, público, documentos e referências de marca; conta do ambiente escolhido; Google/Drive; e, se for usar as integrações, projeto Gemini e acesso administrativo ao portfólio Meta e seus ativos. Não colocar senhas ou tokens na pasta do contexto.
