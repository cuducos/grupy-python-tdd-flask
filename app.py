from flask import Flask

meu_web_app = Flask(__name__)


@meu_web_app.route('/')
def pagina_inicial():
    return ''
