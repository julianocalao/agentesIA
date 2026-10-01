---
name: coreai-setup
description: Setup guiado CoreAI de ambiente, skills globais, ContextOS, conectores, Gemini e Meta. Verifica cada etapa com evidência.
---
# CoreAI:Setup

Esta skill pode trabalhar antes do ContextOS, justamente para criá-lo. Não produzir conteúdo comercial nesta etapa. Resolva scripts e referências relativamente a este arquivo.

## Regra de experiência do aluno

O aluno entrega o README ao Claude/Codex. Execute você os comandos locais usando suas ferramentas; não transforme as referências técnicas em uma lista de comandos para o aluno copiar. Peça apenas login, permissões e decisões que dependem do titular. Primeiro deixe o ambiente funcionando e instale as skills. ContextOS e conectores são etapas seguintes, com orientação por conversa. Se não houver acesso local, explique a limitação antes de executar.

## Condução

Identifique sistema operacional, Claude Code ou Codex, pasta do kit e configuração existente. Execute `scripts/doctor.py` para diagnóstico local. Não imprimir segredos. Conduza uma etapa por vez: ação, resultado esperado, conferência e recuperação. Retome do ponto pendente; não recrie contas ou bases já existentes.

1. Leia `references/ambiente.md`: runtime, dependências, instalação seletiva e descoberta das skills.
2. Liste o catálogo real com `scripts/install.py --source <skills> --list`. Instale somente nomes presentes, no destino solicitado (`--target claude`, `codex` ou `both`). Conflito bloqueia sem sobrescrever. Verifique `--status` e descoberta numa nova sessão. `--global-root` é apenas para testes isolados.
3. Se a skill `coreai-contextos` estiver instalada, o contexto é dela (padrão cérebro: CoreAI:ContextOS:Instalar e Criar). Senão, leia e execute `../coreai-contexto/SKILL.md`: inicialização, empresa ativa, entrevista com fontes e consolidação revisada. Pasta/template vazio não é contexto pronto. Confira com o gate compartilhado.
4. Leia `references/connectors-setup.md`: Drive no ambiente escolhido, leitura de documento conhecido, alternativa por exportação e Gemini. Conector do chat não implica ferramenta no terminal.
5. Leia `references/meta-setup.md`: aplicativo, portfólio, System User, ativos, permissões, token privado e conferência. Login e autorização são realizados pelo titular; guie sem pedir segredos no chat.
6. Faça ensaio local da etapa disponível. Acesso a conta externa precisa de verificação própria; esta skill não publica conteúdo nem ativa campanhas como teste de setup.

Registre cada capacidade como CONCLUÍDA COM EVIDÊNCIA, PENDENTE ou NÃO NECESSÁRIA. Inclua caminho do cliente, resultado do gate, descoberta das skills e testes realmente realizados. Presença de programa/chave não prova autenticação. Não invente comandos MCP nem declare tudo pronto sem testar. Dados do cliente ficam no ContextOS; credenciais ficam no mecanismo privado do executor, nunca em skills ou contexto.

A aula do aluno deve ser disponibilizada no Workshop Times de IA na área de membros. As referências locais são instruções técnicas para você executar, não material de comandos para o aluno.
