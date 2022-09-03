<img src="https://user-images.githubusercontent.com/51168329/159381241-c0b2b316-22de-492c-9703-23e84e860551.png">
<div align="center">
  <a href="https://github.com/andreinaoliveira/QA-Base-Automation"><img alt="hits" src="https://hits.sh/github.com/andreinaoliveira/QA-Base-Automation.svg"/></a>
  <a href="https://github.com/andreinaoliveira/QA-Base-Automation/graphs/commit-activity"><img src="https://img.shields.io/github/last-commit/andreinaoliveira/qa-base-automation"></a>
  <a href="https://github.com/andreinaoliveira/QA-Base-Automation"><img src="https://img.shields.io/badge/status-complete-light"></a>
  <a href="https://github.com/andreinaoliveira/QA-Base-Automation/stargazers"><img src="https://img.shields.io/github/stars/andreinaoliveira/QA-Base-Automation?style=social"></a>
  <a href="https://github.com/andreinaoliveira/QA-Base-Automation/network/members"><img src="https://img.shields.io/github/forks/andreinaoliveira/QA-Base-Automation?style=social"></a>
  <a href="https://github.com/andreinaoliveira"><img src="https://img.shields.io/github/followers/andreinaoliveira?style=social"></a>
</div>

# 🧾 Índice
- <a href="#-sobre">Sobre</a>
- <a href="#-índice">Índice</a>
- <a href="#-instalação">Instalação</a>
- <a href="#-desenvolvimento">Desenvolvimento</a>
  - <a href="#-controller">Controller</a>
    - <a href="#formatpy">/fortmat.py</a>
    - <a href="#logpy">/log.py</a>
    - <a href="#webdriverpy">/webdriver.py</a>
      - <a href="#__code">Code</a>
      - <a href="#find">Find</a>
      - <a href="#click">Click</a>
      - <a href="#set">Set</a>
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

# 💾 Instalação

**Projeto**

```
git clone https://github.com/andreinaoliveira/QA-Base-Automation.git
```

**Dependencias**
* Python 3

**Módulos**

Os módulos devem ser instalados no cmd com os comandos abaixos
```
pip install selenium
pip install webdriver-manager
```

# 🖥 Desenvolvimento
## 🕹 Controller

### /format.py
Contem a função titleTest() recebendo testName. Quando a função é chamada imprime o nome do teste passado por parâmetro de forma mais amigável no terminal. Essa função é chamada para cada teste do unittest localizados na pasta test.

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

Importa a biblioteca de loggin e formata a mensagem de log. Nesse arquivo é criado as funções debug(), info() e error(). Cada função recebe a mensagem que será enviada como log. Essas funções são chamadas em controller/webdriver.

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
- element: Ao ser encontrado, o elemento é salvo nesse atributo.
- as_Code_Type...: É a referência do elemento. É necessário atribuir valor a um dos itens para poder usar as funções da classe. 

```python
import os
import sys
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
        self.element = None
        self.as_1_ID = None
        self.as_2_CLASS_NAME = None
        self.as_3_NAME = None
        self.as_4_TAG_NAME = None
        self.as_5_LINK_TEXT = None
        self.as_6_PARTIAL_LINK_TEXT = None
        self.as_7_CSS_SELECTOR = None
        self.as_8_XPATH = None
```

As funções da classe ao serem chamadas (find, click e set), executará as ações e retornará [True] ou [False] de acordo com o sucesso ou não da atividade. Portanto, além de executar a ação você poderá comparar o resultado, por exemplo, checar se retornou True, ou seja, checar se a ação foi executada com sucesso.

### __Code

A função é chamada na função anterior, find(). Recebe um valor inteiro na variável code, o valor está no range de 1 a 8 e se refere ao tipo de referência do elemento (id, class etc.) o código é o mesmo do atributo as_Code_Type da classe. Exemplo, instanciando a classe como as_1_ID o code da função deve ser _ code(1) para buscar por ID.
O ideal é que a função seja chamada apenas pelo find(), nunca diretamente.

```python
    def _code(self, code):
        if code == 1:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.as_1_ID))
            )
        elif code == 2:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.as_2_CLASS_NAME))
            )
        elif code == 3:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, self.as_3_NAME))
            )
        elif code == 4:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, self.as_4_TAG_NAME))
            )
        elif code == 5:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, self.as_5_LINK_TEXT))
            )
        elif code == 6:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.as_6_PARTIAL_LINK_TEXT))
            )
        elif code == 7:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.as_7_CSS_SELECTOR))
            )
        elif code == 8:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.as_8_XPATH))
            )
        else:
            log.error('Código informado em find() fora do range ou inválido.')
            os.system("pause")
            sys.exit()
```

### Find
1. A Função tenta localizar o elemento e envia um log informando essa tentativa.
2. Não encontrando, imprime o log de erro e retorna Falso.
3. Encontrando, imprime log informando sucesso e retorna True.

```python
    def find(self, code):
        try:
            log.degub('Buscando ' + self.name)
            self._code(code)
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True
```

### Click
1. Chama find() para atribuir valor ao atributo element da classe.
2. Tenta clicar no elemento identificado.
4. Não conseguindo, imprime o log de erro e retorna Falso
5. Conseguindo, imprime log informando sucesso e retorna True

```python
    def click(self, code):
        Element.find(self, code)
        try:
            self.element.click()
        except Exception as e:
            log.error('Erro ao clicar em ' + self.name)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True
```

### Set
1. Chama find() para atribuir valor ao atributo element da classe.
2. Tenta clicar no elemento identificado.
4. Não conseguindo, imprime o log de erro e retorna Falso.
5. Conseguindo, imprime log informando sucesso e retorna True.

```python
    def set(self, code, info):
        Element.find(self, code)
        try:
            self.element.send_keys(info)
        except Exception as e:
            log.error('Erro ao escerver ' + self.name)
            return False
        else:
            log.info(self.name + ' Inserido(a)')
            return True
```

## 🔧 Model
Modelo armazena todas as páginas de um sistema web em aquivos .py diferentes. Cada arquivo possui uma classe que se refere a página web em questão. O ideal é que os principais elementos da página sejam instanciados nessa classe herdando da classe Element de controller/webdriver. Para exemplificar, criamos o modelo da página de login da Netflix (login.py)

Como atribuito possuir:
- driver

As funções da página são divididas em: 
- Check: Checa se está na página, checa se alguma mensagem de erro é apresentada etc.
- Click: realiza o clique em qualquer elemento da página.
- Set: Insere alguma informação na página.

### Check
1. Instancia o elemento passando o driver e o nome do elemento.
2. Atribuir o valor da referência.
3. Retorna a função find que busca a referência informada.

```python
    def check_page_welcome(self):
        e = Element(self.driver, '[Welcome] Page')
        e.as_2_CLASS_NAME = 'our-story-card-title'
        return e.find(2)
```

### Click
1. Instancia o elemento passando o driver e o nome do elemento.
2. Atribuir o valor da referência.
3. Retorna a função click que tentará clicar na referência informada.

```python
    def click_signin_welcome(self):
        e = Element(self.driver, '[Welcome] Sign In button')
        e.as_5_LINK_TEXT = 'Sign In'
        return e.click(5)
```

### Set
1. Instancia o elemento passando o driver e o nome do elemento.
2. Atribuir o valor da referência.
3. Retorna a função set que tentará inserir uma informação na referência informada.

```python
    def set_email(self, email_or_number):
        e = Element(self.driver, '[Login] Email')
        e.as_1_ID = 'id_userLoginId'
        return e.set(1, email_or_number)
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
from model import P01_Login
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

<div align="center">
  <table>
    <tr>
      <td><p><b>PASS</b></p></td>
      <td><p><b>FAIL</b></p></td>
    </tr>
    <tr>
      <td><img src="https://user-images.githubusercontent.com/51168329/159310993-bce3a088-b03c-453c-a667-e2f8e425cf6d.png"></td>
      <td><img src="https://user-images.githubusercontent.com/51168329/159309952-2e2b7576-1517-4aea-8118-4181d84931bc.png"></td>
    </tr>
  </table>
</div>

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

<div align="center">
  <table>
    <tr>
      <th><p><b>Execução Assistida</b></p></th> 
      <th><p><b>Log's</b></p></th>
    </tr>
    <tr>
      <th><img src="https://user-images.githubusercontent.com/51168329/159390569-8cfff750-2593-421f-9b83-dc04d3e375a0.gif" width=600px></th>
      <th><img src="https://user-images.githubusercontent.com/51168329/159302476-1559f447-e745-46a7-a02d-1aedcdf52e2b.png" width=600px></th>
    </tr>
  </table>
</div>

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

<div align="center">
  <table>
    <tr>
      <th><p><b>Execução Assistida</b></p></th> 
      <th><p><b>Log's</b></p></th>
    </tr>
    <tr>
      <th><img src="https://user-images.githubusercontent.com/51168329/159391105-1be2aa4f-1808-48b6-8cd0-5c4ef811b470.gif" width=600px></th>
      <th><img src="https://user-images.githubusercontent.com/51168329/159303621-08b4cb87-f407-438b-983c-8aa0acd6e324.png" width=600px></th>
    </tr>
  </table>
</div>

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

<div align="center">
  <table>
    <tr>
      <th><p><b>Execução Assistida</b></p></th> 
      <th><p><b>Log's</b></p></th>
    </tr>
    <tr>
      <th><img src="https://user-images.githubusercontent.com/51168329/159392417-3f95dfeb-8e5d-45d6-8dae-6b55e0d0c963.gif" width=600px></th>
      <th><img src="https://user-images.githubusercontent.com/51168329/159393494-7d307bbe-d090-473f-b426-68631896d391.png" width=600px></th>
    </tr>
  </table>
</div>

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

<div align="center">
  <table>
    <tr>
      <th><p><b>Execução Assistida</b></p></th> 
      <th><p><b>Log's</b></p></th>
    </tr>
    <tr>
      <th><img src="https://user-images.githubusercontent.com/51168329/159392369-420cc93b-d050-49ca-8fc1-a2dff3a1937e.gif" width=600px></th>
      <th><img src="https://user-images.githubusercontent.com/51168329/159305627-f38c896c-b76c-40c5-93be-1a6bcdf0d134.png" width=600px></th>
    </tr>
  </table>
</div>
                                                                                                             
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

<div align="center">
  <table>
    <tr>
      <th><p><b>Execução Assistida</b></p></th> 
      <th><p><b>Log's</b></p></th>
    </tr>
    <tr>
      <th><img src="https://user-images.githubusercontent.com/51168329/188284644-58c144c0-7ab3-47f6-8496-a0a9e804939f.gif" width=600px></th>
      <th>
      <p>[PASS] Log quando usuário correto</p>
      <img src="https://user-images.githubusercontent.com/51168329/159305627-f38c896c-b76c-40c5-93be-1a6bcdf0d134.png" width=600px>
      <p>[FAIL] Log quando usuário incorreto</p>
      <img src="https://user-images.githubusercontent.com/51168329/159304888-cfd893cd-a66e-403d-b263-a09af52e4003.png" width=600px>
      </th>
    </tr>
  </table>
</div>
