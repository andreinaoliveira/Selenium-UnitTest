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

![image](https://user-images.githubusercontent.com/51168329/159277405-fc66fc4e-0098-4929-94a4-8551d7d63e0b.png)

Para cada referência (id, class, css, xpath e text) há uma função find_by_*referencia*(), click_by_*referencia*() e set_by_*referencia*(). 

A lógica da função para cada referência é a mesma, a diferença consta apenas quando o código tiver por exemplo "self.as_id" ou "By.ID" o temo "ID" deve ser substituído pela refereência correspondente a função, ou seja, find_by_xpath utilizada self.as_xpath e By.XPath.

As funções da classe ao serem chamadas (find, click e set), executará as ações e retornará [True] ou [False] de acordo com o sucesso ou não da atividade. Portanto, além de executar a ação você poderá comparar o resultado, por exemplo, checar se retornou True, ou seja, checar se a ação executado com sucesso.

<div align="center">
  <table>
    <tr>
      <td>
        <b>Find By</b>
      </td>
      <td>
        <b>Click By</b>
      </td>
      <td>
        <b>Set By</b>
      </td>
    </tr>
    <tr>
      <td>
        <ol>
          <li>A Função tenta localizar o elemento e envia um log informando essa tentativa</li>
          <li>Não encontrando, imprime o log de erro e retorna Falso.</li>
          <li>Encontrando, imprime log informando sucesso e retorna True</li>
        </ol>
      </td>
      <td>
        <ol>
          <li>Chama find_by_*referencia*()</li>
          <li>Não encontrando, imprime o log de erro e retorna Falso</li>
          <li>Função _ click() tenta clicar no elemento</li>
          <li>Não conseguindo, imprime o log de erro e retorna Falso</li>
          <li>Conseguindo, imprime log informando sucesso e retorna True</li>
        </ol>
      </td>
       <td>
         <ol>
          <li>Chama find_by_*referencia*()</li>
          <li>retorna Element._ set()</li>
          <li>Função _ set() tenta clicar no elemento</li>
          <li>Não conseguindo, imprime o log de erro e retorna Falso.</li>
          <li>Conseguindo, imprime log informando sucesso e retorna True</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://user-images.githubusercontent.com/51168329/159278822-1b0475e5-5246-4c67-80b9-e97e671c6cc1.png">
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/51168329/159283809-18a0948c-e909-47ae-bb3c-aeceb5b192ad.png">
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/51168329/159286842-b4dd4133-43dd-4e0b-aa1b-3f6314261a41.png">
      </td>
    </tr>
  </table>
</div>

## model/login.py
Modelo armazena todas as páginas de um sistema web em aquivos .py diferentes. O ideal é que os principais elementos de uma página sejam instanciandos nesse arquivo através da classe Element de controller/webdriver.

As funções da página é dividida em: 
- Check: Checa se está na página, checa se alguma mensagem de erro é apresentada etc.
- Click: realiza o clique em qualquer elemento da página.
- Set: Insere alguma informação na página.

<div align="center">
  <table>
    <tr>
      <td>
        <b>Check</b>
      </td>
      <td>
        <b>Click</b>
      </td>
      <td>
        <b>Set</b>
      </td>
    </tr>
    <tr>
      <td>
        <ol>
          <li>Instancia o elemento passando o driver e o nome do elemento.</li>
          <li>Atribuir o valor da referência.</li>
          <li>Retorna a função find que busca a referência informada.</li>
        </ol>
      </td>
      <td>
        <ol>
          <li>Instancia o elemento passando o driver e o nome do elemento.</li>
          <li>Atribuir o valor da referência.</li>
          <li>Retorna a função click que tentará clicar na referência informada.</li>
        </ol>
      </td>
       <td>
         <ol>
          <li>Instancia o elemento passando o driver e o nome do elemento.</li>
          <li>Atribuir o valor da referência.</li>
          <li>Retorna a função set que tentará inserir uma informação na referência informada.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://user-images.githubusercontent.com/51168329/159297467-fd7b499a-fc48-4e4a-8dee-44b0b3f2d542.png">
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/51168329/159297310-76b5d505-ba2c-4bbb-9f3a-b1ff1088c804.png">
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/51168329/159297180-eb92ee9f-3267-4868-9991-9acd5ff3d728.png">
      </td>
    </tr>
  </table>
</div>

## model/test_login.py
Onde os testes de fato irão ocorrer. Após controller ser escrito suportandos as instancias da página em model chega a hora de criar os casos de teste, para isso, será utilizado UnitTest.

### Imports
Como base para o teste, será importado:
- webdriver do próprio selenium
- format de controller
- página de model, no caso login
- unittest.

![image](https://user-images.githubusercontent.com/51168329/159299471-ca7f58d8-b85b-4802-ae0a-74853fce56cb.png)

### UnitTest
- setUp será executado para todos os testes como primeira atividade, será responsável por definir o driver e abrir o navegador.
- tearDown fechará a página.

![image](https://user-images.githubusercontent.com/51168329/159299415-f2b679d0-8594-4bb2-a63c-94ddf8306549.png)

Ao final do teste o UnitTest informa quantos testes passaram e quantatos falharam indicando qual teste deu erro
<table>
  <tr>
    <td>
      <b>Passed</b>
    </td>
    <td>
      <b>Fail</b>
    </td>
  </tr>
  <tr>
    <td>
       <img src="https://user-images.githubusercontent.com/51168329/159310993-bce3a088-b03c-453c-a667-e2f8e425cf6d.png">
    </td>
    <td>
       <img src="https://user-images.githubusercontent.com/51168329/159309952-2e2b7576-1517-4aea-8118-4181d84931bc.png">
    </td>
  </tr>
</table>


### Testes
A parte mais simples do código, é a hora de definir os casos de teste. Vou exemplificar alguns cenários.

**CT01 - Acessar tela de Boas Vindas**

**-> Código**

![image](https://user-images.githubusercontent.com/51168329/159300717-932e6f76-7d1d-4e3c-b0f7-3bb194966937.png)

**-> Log's**

![image](https://user-images.githubusercontent.com/51168329/159302476-1559f447-e745-46a7-a02d-1aedcdf52e2b.png)

**-> Execução Assistida**

**CT02 - Acessar tela de Login**
**-> Código**

![image](https://user-images.githubusercontent.com/51168329/159300859-66a272aa-cf6f-403c-af5d-35d718069e3e.png)

**-> Log's**

![image](https://user-images.githubusercontent.com/51168329/159303621-08b4cb87-f407-438b-983c-8aa0acd6e324.png)

**-> Execução Assistida**

**CT03 - Senha Inválida**
**-> Código**

![image](https://user-images.githubusercontent.com/51168329/159300929-cdf0033d-c453-4e03-9df8-4c440a2bac59.png)

**-> Log's**

![image](https://user-images.githubusercontent.com/51168329/159303756-a7477632-6ddc-4d93-b6d9-30408d0446ae.png)

**-> Execução Assistida**

**CT04 - Usuário Inválido**
**-> Código**

![image](https://user-images.githubusercontent.com/51168329/159300974-44870b91-cb37-4c7f-bed5-37e4dd9a2d24.png)

**-> Log's**

![image](https://user-images.githubusercontent.com/51168329/159303816-a1f2c023-0480-43f0-a23d-7a96c1f70477.png)

**-> Execução Assistida**

**CT05 - Usuário Válido**
**-> Código**

![image](https://user-images.githubusercontent.com/51168329/159305882-35f93c6f-cbf9-4ad3-972e-d5c36cdf82d1.png)

**-> Log's**

![image](https://user-images.githubusercontent.com/51168329/159305627-f38c896c-b76c-40c5-93be-1a6bcdf0d134.png)

**-> Execução Assistida**
**-> Simulando erro**

![image](https://user-images.githubusercontent.com/51168329/159304888-cfd893cd-a66e-403d-b263-a09af52e4003.png)

