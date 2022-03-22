![Purple and Yellow Colorful Gradient Motivational Quote LinkedIn Article Cover Image](https://user-images.githubusercontent.com/51168329/159381241-c0b2b316-22de-492c-9703-23e84e860551.png)
<div align="center">
  <img src="https://img.shields.io/github/last-commit/andreinaoliveira/qa-base-automation">
  <img src="https://img.shields.io/github/followers/andreinaoliveira?style=social">
  <img src="https://img.shields.io/github/forks/andreinaoliveira/QA-Base-Automation?style=social">
  <img src="https://img.shields.io/github/stars/andreinaoliveira/QA-Base-Automation?style=social">
</div>

# 🧾 Índice
- <a href="#-sobre">Sobre</a>
- <a href="#-índice">Índice</a>
- <a href="#-desenvolvimento">Desenvolvimento</a>
  - <a href="#-controller">Controller</a>
    - <a href="#formatpy">/fortmat.py</a>
    - <a href="#logpy">/log.py</a>
    - <a href="#webdriverpy">/webdriver.py</a>
      - <a href="#find-by">Find By</a>
      - <a href="#click-by">Click By</a>
      - <a href="#set-by">Set By</a>
  - <a href="#-model">Model</a>
    - <a href="#check">Check</a>
    - <a href="#click">Click</a>
    - <a href="#set">Set</a>
  - <a href="#-test">Test</a>
    - <a href="#imports">Imports</a>
    - <a href="#unittest">Unittest</a>
- <a href="#-cenários-de-teste">Cenários de Teste</a>
  - <a href="#ct01---acessar-tela-de-boas-vindas">CT01 - Acessar tela de Boas Vindas</a>
  - <a href="#ct02---acessar-tela-de-login">CT02 - Acessar tela de Login</a>
  - <a href="#ct03---senha-inválida">CT03 - Senha Inválida</a>
  - <a href="#ct04---usuário-inválido">CT04 - Usuário Inválido</a>
  - <a href="#ct05---usuário-válido">CT05 - Usuário Válido</a>

# 💬 Sobre
Base para automação de testes utilizando a linguagem Python com as tecnologias do Selenium WebDriver e UnitTest e com a estrutura organizacional MTC (Model-Test-Controller), uma adaptação do MVC.

Para exemplificar o funcionamento da base será automatizado a tela de login do site Netflix. para cobrir os seguintes cenários de teste:
- CT01 - Acessar tela de Boas Vinda
- CT02 - Acessar tela de Login
- CT03 - Senha Inválida
- CT04 - Usuário Inválido
- CT05 - Usuário Válido

# 🖥 Desenvolvimento
## 🕹 Controller

### /format.py
Contem a função titleTest() recebendo testName. Recebendo o nome do teste, quando a função é chamada imprime o nome do teste de forma mais amigável no terminal. Essa função é chamado em test.
```python
def titleTest(testName):
    print(100 * '-')
    print(testName.center(100))
    print(100 * '-')
```

Exemplo da impressão:
```
----------------------------------------------------------------------------------------------------
                                 CT01 - Acessar tela de Boas Vindas                                 
----------------------------------------------------------------------------------------------------
```


### /log.py

Importa a biblioteca de loggin e formata a mensagem de log. Nesse arquivo é criado as funções debug(), info() e error(). Cada função recebe a mensagem que será enviada como log. Essas funções são chamadas em webdriver.

```python
import logging
log_format = '%(asctime)s :: %(name)s :: %(levelname)s :: %(module)s :: %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO, filemode='w')


def degub(message):
    logging.debug(message)

def info(message):
    logging.info(message)

def error(message):
    logging.error(message)
```

### /webdriver.py

Em webdriver.py é criada a classe Element com os seguintes atribuitos e importações:
- driver: recebe o webdriver que será criado apenas no teste.
- name: nome do elemento ex.: Botão Sign In. O nome será enviado apenas nos log's. 
- as_id/class/css/xpath/text: é a referência do elemento. É necessário atribuir valor a um dos itens para poder usar as funções da classe. 

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from controller import log
```

```python
class Element:
    def __init__(self, driver, name):
        self.driver = driver
        self.name = name
        self.as_id = None
        self.as_class = None
        self.as_css = None
        self.as_xpath = None
        self.as_text = None
```

Para cada referência (id, class, css, xpath e text) há uma função find_by_*referencia*(), click_by_*referencia*() e set_by_*referencia*(). 

A lógica da função para cada referência é a mesma, a diferença consta apenas quando o código tiver por exemplo "self.as_id" ou "By.ID" o temo "ID" deve ser substituído pela refereência correspondente a função, ou seja, find_by_xpath utilizada self.as_xpath e By.XPath.

As funções da classe ao serem chamadas (find, click e set), executará as ações e retornará [True] ou [False] de acordo com o sucesso ou não da atividade. Portanto, além de executar a ação você poderá comparar o resultado, por exemplo, checar se retornou True, ou seja, checar se a ação executado com sucesso.

### Find by
1. A Função tenta localizar o elemento e envia um log informando essa tentativa.
2. Não encontrando, imprime o log de erro e retorna Falso.
3. Encontrando, imprime log informando sucesso e retorna True.
```python
    def find_by_id(self):
        """
        Encontra um elemento web.
        :return: boolean
        """
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.as_id))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True
```
### Click by
1. Chama find_by_*referencia*()
2. Não encontrando, imprime o log de erro e retorna Falso
3. Função _ click() tenta clicar no elemento.
4. Não conseguindo, imprime o log de erro e retorna Falso
5. Conseguindo, imprime log informando sucesso e retorna True

```python
    def _click(self):
        try:
            element.click()
        except Exception as e:
            log.error('Erro ao clicar em ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True
```

```python
    def click_by_id(self):
        Element.find_by_id(self)
        return Element._click(self)
```

### Set by
1. Chama find_by_*referencia*().
2. retorna Element._ set().
3. Função _ set() tenta clicar no elemento.
4. Não conseguindo, imprime o log de erro e retorna Falso.
5. Conseguindo, imprime log informando sucesso e retorna True.

```python
    def _set(self, info):
        try:
            element.send_keys(info)
        except Exception as e:
            log.error('Erro ao escerver ' + self.name)
            print(e)
        else:
            log.info(self.name + ' Inserido(a)')
```

```python
    def set_by_class(self, info):
        Element.find_by_class(self)
        return Element._set(self, info)
```


## 🔧 Model
Modelo armazena todas as páginas de um sistema web em aquivos .py diferentes. O ideal é que os principais elementos de uma página sejam instanciandos nesse arquivo através da classe Element de controller/webdriver. Para exemplificar, criamos o modelo da página de login da Netflix (login.py)

As funções da página é dividida em: 
- Check: Checa se está na página, checa se alguma mensagem de erro é apresentada etc.
- Click: realiza o clique em qualquer elemento da página.
- Set: Insere alguma informação na página.

### Check
1. Instancia o elemento passando o driver e o nome do elemento.
2. Atribuir o valor da referência.
3. Retorna a função find que busca a referência informada.

```python
def check_page_welcome(driver):
    p = Element(driver, 'Tela Welcome')
    p.as_class = 'our-story-card-title'
    return p.find_by_class()
```

### Click
1. Instancia o elemento passando o driver e o nome do elemento.
2. Atribuir o valor da referência.
3. Retorna a função click que tentará clicar na referência informada.

```python
def click_signin_welcome(driver):
    s = Element(driver, 'botão sign in de Welcome')
    s.as_text = 'Sign In'
    return s.click_by_text()
```

### Set
1. Instancia o elemento passando o driver e o nome do elemento.
2. Atribuir o valor da referência.
3. Retorna a função set que tentará inserir uma informação na referência informada.

```python
def set_email(driver, email_or_number):
    e = Element(driver, 'email')
    e.as_id = 'id_userLoginId'
    return e.set_by_id(email_or_number)
```

## 🧪 Test
Onde os testes de fato irão ocorrer. Após controller ser escrito suportando as instancias da página em model chega a hora de criar os casos de teste, para isso, será utilizado UnitTest. O teste será feiro com base no modelo login.py, portanto, o teste será chamado test_login.py

### Imports
Como base para o teste, será importado:
- webdriver do próprio selenium
- format de controller
- página de model, no caso login
- unittest.

```python
from selenium import webdriver
from controller import format
from model import login
import unittest
```

### UnitTest
Por padrão o unitTest possui as funções setUp e tearDown, elas são chamadas para cada função de teste criada na classe test do unittest. setUp é chamada antes do teste e tearDown após o teste. Para o projeto, essas duas funções foram programadas para:

- **setUp**: Responsável por definir o driver e abrir o navegador na página inicial da Netflix.
- **tearDown**: Fechar a página web.

```python
class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.driver.get('https://www.netflix.com/br-en/')

    # Adicionar aqui funções de teste, entre setUp e tearDown.

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
```

Considerando que as funções de teste foram escritas, ao final do teste o UnitTest informa quantos testes passaram e quantatos falharam indicando qual teste deu erro.

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

## 👩🏼‍💻 Cenários de Teste

### CT01 - Acessar tela de Boas Vindas
**Objetivo**
- Acessar o site da Netflix e checar se é carregada a tela de Boas Vindas.

**Código**
```python
    def test_CT01_AccessWelcome(self):
        format.titleTest("CT01 - Acessar tela de Boas Vindas")
        self.assertTrue(login.check_page_welcome(self.driver))
```

**Log's**

<img src="https://user-images.githubusercontent.com/51168329/159302476-1559f447-e745-46a7-a02d-1aedcdf52e2b.png">

**Execução Assistida**

### CT02 - Acessar tela de Login
**Objetivo**
- Acessar o site da Netflix, clicar em "Sign In" e checar se é carregada a tela de Login.

**Código**
```python
    def test_CT02_AccessLogin(self):
        format.titleTest("CT02 - Acessar tela de login")
        login.click_signin_welcome(self.driver)
        self.assertTrue(login.check_page_login(self.driver))
```

**Log's**

<img src="https://user-images.githubusercontent.com/51168329/159303621-08b4cb87-f407-438b-983c-8aa0acd6e324.png">

**Execução Assistida**

### CT03 - Senha Inválida
**Objetivo**
- Dado o acesso ao site da Netflix e clicado em "Sign In" preenchendo um e-mail válido e senha inválida no site, checar se a mensagem referente a senha errada é apresentada.

**Código**

```python
    def test_CT03_InvalidPassword(self):
        format.titleTest("CT03 - Senha inválida")
        login.click_signin_welcome(self.driver)
        login.set_email(self.driver, 'teste@gmail.com')
        login.set_password(self.driver, 'Teste@1234')
        login.click_signin_login(self.driver)
        self.assertTrue(login.check_error_passwordInvalid(self.driver))
```

**Log's**

<img src="https://user-images.githubusercontent.com/51168329/159303756-a7477632-6ddc-4d93-b6d9-30408d0446ae.png">

**Execução Assistida**

### CT04 - Usuário Inválido
**Objetivo**
- Dado o acesso ao site da Netflix e clicado em "Sign In" preenchendo e-mail e senha com dados inexistente no site, checar se a mensagem de que o usuário não existe é apresentada.

**Código**

```python
    def test_CT04_InvalidAccount(self):
        format.titleTest("CT04 - Usuário inválido")
        login.click_signin_welcome(self.driver)
        login.set_email(self.driver, 'testeSelenium@gmail.com')
        login.set_password(self.driver, 'Teste@1234')
        login.click_signin_login(self.driver)
        self.assertTrue(login.check_error_userInvalid(self.driver))
```

**Log's**

<img src="https://user-images.githubusercontent.com/51168329/159303816-a1f2c023-0480-43f0-a23d-7a96c1f70477.png">


**Execução Assistida**

### CT05 - Usuário Válido
**Objetivo**
- Dado o acesso ao site da Netflix e clicado em "Sign In" preenchendo e-mail e senha com dados existentes no site e clicando em "Sign In", checar se a tela de Perfis é carregada.
**Código**

```python
    def test_CT05_ValidUser(self):
        format.titleTest("CT05 - Usuário Válido")
        login.click_signin_welcome(self.driver)

        email = input('Informe um e-mail váido: ')
        senha = input('Informe uma senha válida: ')

        print()

        login.set_email(self.driver, email)
        login.set_password(self.driver, senha)
        login.click_signin_login(self.driver)
        self.assertTrue(login.check_page_profiles(self.driver))
```

**Log's**

<img src="https://user-images.githubusercontent.com/51168329/159305627-f38c896c-b76c-40c5-93be-1a6bcdf0d134.png">

**Execução Assistida**

**Simulando erro**

<img src="https://user-images.githubusercontent.com/51168329/159304888-cfd893cd-a66e-403d-b263-a09af52e4003.png">
