**Title:** Interação de filtro

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
Quando um usuário seleciona a flecha em filtro, não apresenta as opções.

**Steps to Reproduce:**
1. Abrir o navegador (https://www.saucedemo.com/)
2. Digitar login e senha válidos.
3. Clicar na flecha em filtros.
4. Observar o erro:
```
NULL
```
**Expected Result:**  
Ao selecionar a flecha em filtro, apresentar as opções.

**Actual Result:**  
Ao selecionar a flecha em filtro, não apresenta as opções.

**Attachments:**
- Screenshot do problema de interação[bug_report-2.png](playwright_tests\bugs_images\bug_report-2.png)

**Workaround (if any):**  
Selecionar filtro na parte central.