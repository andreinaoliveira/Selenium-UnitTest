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

## controller/format.py
Contem a função titleTest() recebendo testName. Recebendo o nome do teste, quando a função é chamada imprime o nome do teste de forma mais amigável no terminal. Essa função é chamado em test.

![image](https://user-images.githubusercontent.com/51168329/159273023-2880848c-d6b8-454a-b2db-f8fe98f56021.png)

Exemplo da impressão:

![image](https://user-images.githubusercontent.com/51168329/159273892-50ac6a3b-3e70-4928-b1f6-55da4d154d3c.png)

## controller/log.py

Importa a biblioteca de loggin e formata a mensagem de log. Nesse arquivo é criado as funções debug(), info() e error(). Cada função recebe a mensagem que será enviada como log. Essas funções são chamadas em webdriver.

![image](https://user-images.githubusercontent.com/51168329/159275122-7bc33c6c-985a-47f3-9abb-8c4772db31ce.png)

## controller/webdriver.py

Em webdriver.py é criada a classe Element com os seguintes atribuitos e importações:
- driver: recebe o webdriver que será criado apenas no teste.
- name: nome do elemento ex.: Botão Sign In. O nome será enviado apenas nos log's. 
- as_id/class/css/xpath/text: é a referência do elemento. É necessário atribuir valor a um dos itens para poder usar as funções da classe. 

Para cada referência (id, class, css, xpath e text) há uma função find_by_*referencia*(), click_by_*referencia*() e set_by_*referencia*(). 

A lógica da função para cada referência é a mesma, a diferença consta apenas quando o código tiver por exemplo "self.as_id" ou "By.ID" o temo "ID" deve ser substituído pela refereência correspondente a função, ou seja, find_by_xpath utilizada self.as_xpath e By.XPath.

As funções da classe ao serem chamadas (find, click e set), executará as ações e retornará [True] ou [False] de acordo com o sucesso ou não da atividade. Portanto, além de executar a ação você poderá comparar o resultado, por exemplo, checar se retornou True, ou seja, checar se a ação executado com sucesso.

![image](https://user-images.githubusercontent.com/51168329/159277405-fc66fc4e-0098-4929-94a4-8551d7d63e0b.png)

### Find By
1. A Função tenta localizar o elemento e envia um log informando essa tentativa
2. Não encontrando, imprime o log de erro e retorna Falso.
3. Encontrando, imprime log informando sucesso e retorna True

![image](https://user-images.githubusercontent.com/51168329/159278822-1b0475e5-5246-4c67-80b9-e97e671c6cc1.png)

### Click By
1. Chama find_by_*referencia*()
2. retorna Element._ click()
3. Função _ click() tenta clicar no elemento
4. Não conseguindo, imprime o log de erro e retorna Falso.
5. Conseguindo, imprime log informando sucesso e retorna True

![image](https://user-images.githubusercontent.com/51168329/159283809-18a0948c-e909-47ae-bb3c-aeceb5b192ad.png)


### Set By
1. Chama find_by_*referencia*()
2. retorna Element._ set()
3. Função _ set() tenta clicar no elemento
4. Não conseguindo, imprime o log de erro e retorna Falso.
5. Conseguindo, imprime log informando sucesso e retorna True

![image](https://user-images.githubusercontent.com/51168329/159286842-b4dd4133-43dd-4e0b-aa1b-3f6314261a41.png)

## model/login.py
## model/test_login.py
