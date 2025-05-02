**Title:** Descrição de erro de login

**ID:** BUG-001

**Reported By:** Jeanderson Alves dos Santos

**Date:** 01/05/2025

**Environment:**
- **Operating System:** Windows 11 
- **Browser:** Chrome 130.0.6723.92
- **Application Version:** 24H2

**Severity:** Baixa  
**Priority:** P3 (Baixo)

**Description:**  
Quando um usuário adiciona credenciais incorretas, mensagem de erro não está correta.

**Steps to Reproduce:**
1. Abrir o navegador (https://www.saucedemo.com/)
2. Digitar login e senha válidos.
3. Clicar no botão na flecha para baixo em filtros.
4. Observar a mensagem de erro:
```
Epic sadface: Username and password do not match any user in this service.
```
**Expected Result:**  
Ao inserir credenciais inválidas e clicar no botão de login, o erro deveria usar inglês correto.

**Actual Result:**  
A página apresenta a afirmação de forma incorreta "Epic sadface: ".

**Attachments:**
- Screenshot do erro de digitação![bug_report-1.png](C:\Users\Study\Documents\qa-tech-challenge\playwright_tests\bugs_images\bug_report-1.png)

**Workaround (if any):**  
Nenhum.