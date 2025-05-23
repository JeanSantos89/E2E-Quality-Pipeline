**🟢 Objetivo:** 

Projeto de automação de testes E2E para uma aplicação de e-commerce (https://www.saucedemo.com/), utilizando Python, Pytest e Playwright, com foco na garantia de qualidade, estabilidade e integração contínua. Os casos de teste são elaborados em Gherkin, estruturados no Xray para rastreabilidade completa e vinculados a User Stories e Bugs no Jira. A execução automatizada ocorre via GitHub Actions, permitindo a execução contínua dos testes e manutenção de um pipeline de qualidade. O projeto está em constante evolução, com a inclusão de novos cenários, identificação de bugs e melhorias no processo de integração e entrega contínua (CI/CD).

**✅ Ideia Principal:** 
- Automação E2E construída utilizando Python, Pytest e Playwright, cobrindo fluxos essenciais da aplicação de e-commerce https://www.saucedemo.com/.
- Casos de teste documentados em formato Gherkin no arquivo test_cases.md, organizados por funcionalidades (Login, Carrinho, Filtros, etc.).
- Relatórios de bugs encontrados, estruturados com detalhes (ID, descrição, ambiente, evidências) no diretório bug_reports/.
= Pipeline básico de execução via GitHub Actions já configurado para rodar os testes automaticamente.

**⚠️ Estou adaptando e incrementando:**

**Gestão completa via Jira:**

- ➡️ Criando Epics, User Stories, Bugs e rastreabilidade entre requisitos e testes.

**Estruturação dos testes no Xray:**

- ➡️ Migrando os casos de teste para o Xray, transformando-os em Test Cases formais.

- ➡️ Configurando Test Executions para controlar execuções manuais e automatizadas.

**Integração contínua:**

- ➡️ Ajustando o pipeline de CI/CD no GitHub Actions para:

- ➡️ Rodar testes automaticamente a cada push ou PR.

- ➡️ Preparar integração com o Xray via API, para automatizar a atualização dos resultados dos testes.

**⌛ Expansão contínua:**
- ➡️ Incrementando novos cenários de teste, novos fluxos críticos e realizando bug hunting para fortalecer a cobertura.

