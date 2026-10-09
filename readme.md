**🟢 Objetivo:** 

Projeto de automação de testes E2E para uma aplicação de e-commerce (https://www.saucedemo.com/), utilizando Python, Pytest e Playwright, com foco na garantia de qualidade, estabilidade e integração contínua. Os casos de teste são elaborados em Gherkin, estruturados no Xray para rastreabilidade completa e vinculados a User Stories e Bugs no Jira. A execução automatizada ocorre via GitHub Actions, permitindo a execução contínua dos testes e manutenção de um pipeline de qualidade. O projeto está em constante evolução, com a inclusão de novos cenários, identificação de bugs e melhorias no processo de integração e entrega contínua (CI/CD).

**✅ Ideia Principal:** 
- Automação E2E construída utilizando Python, Pytest e Playwright, cobrindo fluxos essenciais da aplicação de e-commerce https://www.saucedemo.com/.
- Casos de teste documentados em formato Gherkin no arquivo test_cases.md, organizados por funcionalidades (Login, Carrinho, Filtros, etc.).
- Relatórios de bugs encontrados, estruturados com detalhes (ID, descrição, ambiente, evidências) no diretório bug_reports/.
= Pipeline básico de execução via GitHub Actions já configurado para rodar os testes automaticamente.

**🔍 Gate de qualidade dos testes (`assert-quality-audit`):**

O gate `e2e-ui-tests` prova que os testes rodam e passam. Mas passar não é a mesma
coisa que provar algo: um `def test_*` sem nenhum `assert`, `pytest.fail` ou `raise`
no corpo passa sempre, mesmo que a funcionalidade esteja quebrada - é um "verde
mentiroso". O mesmo vale pra uma asserção tautológica, tipo `assert True` ou
`assert x == x`, que nunca falha.

O job `assert-quality-audit` roda `scripts/audit_test_quality.py`, um script que usa
só a lib `ast` da stdlib (sem instalar nada, sem browser) pra escanear
`playwright_tests/test_*.py` e falhar o CI se achar:
- uma função de teste sem nenhuma verificação própria e sem chamar um helper que já
  verifica por dentro (este repo verifica com `pytest.fail()`/`raise`, não com
  `assert` cru - o script reconhece as duas formas como prova válida);
- `assert True`, `assert False` literal, ou `assert X == X` com os dois lados
  idênticos.

É um gate independente do `e2e-ui-tests`: não precisa de Playwright instalado, roda
em segundos, e pega um tipo de problema que a suíte passando não pega sozinha.
