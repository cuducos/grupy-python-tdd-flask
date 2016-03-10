
# Python com TDD e desenvolvimento de aplicações web com Flask

Palestra para [encontro](http://www.meetup.com/Grupy-SP/events/228437612/) do [Grupy-SP](https://groups.google.com/forum/#!forum/grupy-sp) em 12 de março de 2016.

## 1. Preparando o ambiente

### Requisitos

Para esse exercício usaremos o [Python](http://http://python.org) versão 3.5.1 e com o framework [Flask](http://flask.pocoo.org/). É recomendado, mas não necessário, usar um [virtualenv](http://virtualenv.readthedocs.org).

Você pode verificar a versão do seu Python com esse comando:

```console
$ python --version                                                                                    
```

Dependendo da sua instalação, pode ser que você tenha que usar `python3` ao invés de `python` — ou seja, o comando todo deve ser `python3 --version`. O resultado deve ser esse:

```
Python 3.5.1
```

E instalar o Flask assim:

```
$ pip install Flask
```

O `pip` é um gerenciador de pacotes do Python. Ele vem instalado por padrão nas versões mais novas do Python. Dependendo da sua instalação, pode ser que você tenha que usar `pip3` ao invés de `pip` — ou seja, o comando todo deve ser `pip3 install Flask`. Com esse comando ele vai instalar o Flask e qualquer dependência que o Flask tenha:

```console
Collecting Flask
Collecting Jinja2>=2.4 (from Flask)
  Using cached Jinja2-2.8-py2.py3-none-any.whl
Collecting itsdangerous>=0.21 (from Flask)
Collecting Werkzeug>=0.7 (from Flask)
  Using cached Werkzeug-0.11.4-py2.py3-none-any.whl
Collecting MarkupSafe (from Jinja2>=2.4->Flask)
Installing collected packages: MarkupSafe, Jinja2, itsdangerous, Werkzeug, Flask
Successfully installed Flask-0.10.1 Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.4 itsdangerous-0.24
```
### Arquivos 

Vamos usar, nesse exercício, basicamente 2 arquivos:

* `app.py`: onde criamos nossa aplicação web;;
* `tests.py`: onde escrevemos os testes que guiarão o desenvolvimento da aplicação, e que, também, garantirão que ela funcione.


## 2. Criando a base dos testes

No arquivo `tests.py` vamos usar o módulo [unittest](https://docs.python.org/3.5/library/unittest.html), que já vem instalado por padrão no Python.

Criaremos uma estrutura básica para que, toda vez que esse arquivo seja executado, o `unittest` se encarregue de encontrar todos os nossos testes e rodá-los:

```python
import unittest


class TestFatorial(unittest.TestCase):

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(3), 6)
        self.assertEqual(fatorial(4), 24)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(6), 720)

if __name__ == '__main__':
    unittest.main()
```

Agora podemos rodar os testes assim:

```console
$ python testes.py
```

Veremos uma mensagem de erro, `NameError`, pois não definimos nossa função `fatorial(num)`:

```
E
======================================================================
ERROR: test_fatorial (__main__.TestSimples)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 7, in test_fatorial
    self.assertEqual(fatorial(0), 1)
NameError: name 'fatorial' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

Tudo bem, a ideia não é brincar com matemática agora. Mas vamos criar essa função lá no `app.py` só para ver como a gente pode “integrar” esses dois arquivos — ou seja, fazer o `tests.py` testar o que está em `app.py`.

Vamos adicionar essas linhas ao `app.py`:

```python
def fatorial(numero):
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)
```

E adicionar essa linha no topo do `tests.py`:

```python
from app import fatorial
```

Rodando os testes agora, vemos que a integração entre `app.py` e `tests.py` está funcionando:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## 3. Primeiros passos para a aplicação web

### Criando um servidor web

Como nosso foco é começar uma aplicação web, podemos descartar nossos testes e nosso método que criamos no passo anterior. Ao invés disso, vamos escrever um teste simples, para ver se conseguimos fazer o Flask criar um servidor web.

Descarte tudo do `tests.py` substituindo por essas linhas:

```python
import unittest
from app import meu_web_app


class TestHome(unittest.TestCase):

    def test_get(self):
        app = meu_web_app.test_client()
        response = app.get('/')
        self.assertEqual(200, response.status_code)
        
if __name__ == '__main__':
    unittest.main()
```

Esse arquivo agora faz quatro coisas referentes a nossa aplicação web:

1. Importa o objeto `meu_web_app` (que ainda não criamos) do nosso arquivo `app.py`;
1. Cria uma instância da nossa aplicação web específica para nossos testes (batizamos essa instância de `app`);
1. Tenta acessar a “raíz” da nossa aplicação — ou seja, se essa aplicação web estivesse no servidor `meuservidor.org.br` estaríamos acessando [http://meuservidor.org.br/](http://meuservidor.org.br).
1. Verifica se ao acessar essa URL, ou seja, se ao fazer a requisição HTTP, temos como resposta o código 200, que representa sucesso.

Os códigos de status de requisição HTTP mais comuns são o `200` (sucesso), `404` (página não encontrada) e `302` (redirecionamento) — mas a [lista de completa](https://pt.wikipedia.org/wiki/Lista_de_códigos_de_status_HTTP) é muito maior que isso. 

De qualquer forma não conseguiremos rodar esses testes. O Python vai dar erro:

```
ImportError: cannot import name 'meu_web_app'
```

Então vamos criar o objeto `meu_web_app` lá no `app.py`. Descartamos tudo que tínhamos lá substituindo por essas linhas:

```python
from flask import Flask

meu_web_app = Flask(__name__)
```

Apenas estamos importando a classe principal do Flask, e criando uma instância dela. Em outras palavras, estamos começando a utilizar o framework.

E agora o erro muda:

```
F
======================================================================
FAIL: test_get (__main__.TestHome)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 10, in test_get
    self.assertEqual(200, response.status_code)
AssertionError: 200 != 404

----------------------------------------------------------------------
Ran 1 test in 0.015s

FAILED (failures=1)
```

Temos uma aplicação web rodando, mas quando tentamos acessar a raíz dela, ela nos diz que a página não está definida, não foi encontrada (é o que nos diz o código `404`).

### Criando nossa primeira página

O Flask facilita muito a criação de aplicações web. De forma simplificada qualquer método Python pode ser atribuído a uma URL dessa forma:

```
@app.route('/')
def pagina_inicial():
    return ''
```

Adicionando essas linhas no `app.py`, os testes passam:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.013s

OK
```

Se a curiosidade for grande, esse artigo (em inglês) explica direitinho como o `Flask.route(rule, **options)` faz e como ele funciona: [Things which aren't magic - Flask and @app.route](http://ains.co/blog/things-which-arent-magic-flask-part-1.html).

Para garantir que tudo está certinho mesmo, podemos adicionar mais um teste. Queremos que a resposta do servidor seja um HTML:

```python
def test_content_type(self):
    app = meu_web_app.test_client()
    response = app.get('/')
    self.assertIn('text/html', response.content_type)
```

### Eliminando repetições

Repararam que duas linhas se repetem nos métodos `test_get()` e `test_content_type()`?

```python
app = meu_web_app.test_client()
response = app.get('/')
```

Podemos usar um método especial da classe `TestCase` para reaporiveitar esse código. O método `TestCase.setUp()` é executado a cada teste, e através do `self` podemos acessar objetos de um método a partir de outro método:

```python
class TestHome(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
```