Teste 1 - WebScraping

Lógica do programa:
1. Obter o HTML do link fornecido
2. Fazer um parse com a biblioteca Beautiful Soup
3. Procurar pelo elemento que começa com o texto 'Padrão TISS - Versão'
4. Acessar o link do primeiro elemento abaixo do header e obter o HTML
5. No novo HTML, encontrar a tabela
6. Dentro do primeiro <tr> da tabela, obter a versão a partir do segundo <td>
7. Obter o link do PDF no terceiro <td> e fazer o download
