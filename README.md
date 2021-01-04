Teste 1 - WebScraping

Lógica do programa:
1. Obter o HTML do link fornecido
2. Fazer um parse com a biblioteca Beautiful Soup
3. Procurar pelo elemento que começa com o texto 'Padrão TISS - Versão'
4. Acessar o link do primeiro elemento abaixo do header e obter o HTML
5. No novo HTML, encontrar a tabela
6. Iterar a tabela até achar a linha cuja primeira coluna possui o texto 'Componente Organizacional'
7. Da linha, extrair a versão da segunda coluna
8. Da linha, extrair o link da terceira coluna
9. Fazer o download
