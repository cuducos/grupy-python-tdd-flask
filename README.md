
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
