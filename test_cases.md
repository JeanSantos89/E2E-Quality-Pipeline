**Descrição**
- Test Case seguindo a gramática e ordenação, segundo a linguagem Gherkin.



    **Funcionalidade: Login e Sessão**

**Cenário**: TC01 - Login válido
- Dado que o usuário esteja na página de login
- Quando preencher com dados válidos e clicar em login
- Então deve ser redirecionado para a página principal

**Cenário**: TC02 - Logout
- Dado que o usuário esteja logado
- Quando clicar em logout
- Então deve ser deslogado com sucesso



    **Funcionalidade: Funcionalidades da Página**

**Cenário**: TC03 - Funcionalidade de Filtro
- Dado que o usuário esteja logado
- Quando aplicar um filtro na lista de produtos
- Então os produtos devem ser reorganizados corretamente

**Cenário**: TC04 - Adicionar itens ao carrinho
- Dado que o usuário esteja logado
- Quando selecionar produtos e adicioná-los ao carrinho
- Então os itens devem aparecer no carrinho corretamente

**Cenário**: TC05 - Checkout
- Dado que o usuário tenha itens no carrinho
- Quando clicar em checkout e preencher os dados necessários
- Então o checkout deve ser concluído com os itens selecionados



    **Funcionalidade: Validação de Conteúdo**

**Cenário**: TC06 - Descrição dos produtos
- Dado que o usuário esteja logado
- Quando acessar a lista de produtos
- Então pelo menos um produto deve exibir a descrição preenchida
