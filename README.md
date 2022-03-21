# QA Base Automation
Base para automação de testes utilizando a linguagem Python com as tecnologias do Selenium WebDriver e UnitTest e coma estrutura organizacional MTC (Model-Test-Controller), uma adaptação do MVC.

## Sobre o projeto
Para exemplificar o funcionamento da base será automatizado a tela de login do site Netflix. O código está organizando em:
- <b>controller</b>
  - <b>format</b>: Contem a formatação do título do teste. Será utilizado apenas em test.
  - <b>log</b>: Contem a formatação das mensagem de log nível debug, info e error. Será utilizada em webdriver.
  - <b>webdriver</b>: A base do projeto, nela consta a classe Element que contém os principais atributos de um elemento web assim com as principais ações sobre eles: Find, Click e Set. Cada função da classe além de executar as ações retorna True ou False em relação ao sucesso da execução.
- <b>model</b>: Cada arquivo .py dentro de model representa uma página do sistema web. E para cada página, é importando a classe Element de webdriver e transformado os principais itens da tela em uma instância da classe.
- <b>test</b>: Onde os testes serão executados com UnitTest. O repositório de teste é bem livre para a criação de cenários. Para cada teste será necessário apenas declarar o driver em setUp, informar o título do teste com a função titleTest de format e importar a página que será testada em modelo.

## controller/

### format.py
Contem a função titleTest() recebendo testName. Recebendo o nome do teste, quando a função é chamada imprime o nome do teste de forma mais amigável no terminal. Essa função é chamado em test.

![image](https://user-images.githubusercontent.com/51168329/159273023-2880848c-d6b8-454a-b2db-f8fe98f56021.png)
![image](https://user-images.githubusercontent.com/51168329/159273892-50ac6a3b-3e70-4928-b1f6-55da4d154d3c.png)

### log.py

Importa a biblioteca de loggin e formata a mensagem de log. Nesse arquivo é criado as funções debug(), info() e error(). Cada função recebe a mensagem que será enviada como log. Essas funções são chamadas em webdriver.

![image](https://user-images.githubusercontent.com/51168329/159275122-7bc33c6c-985a-47f3-9abb-8c4772db31ce.png)

### webdriver.py

Em webdriver.py 
