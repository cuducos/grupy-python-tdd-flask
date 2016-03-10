
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
