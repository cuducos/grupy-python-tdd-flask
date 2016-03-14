from flask import Flask, render_template

meu_web_app = Flask('meu_web_app')

CUDUCOS = {'nome': 'Eduardo Cuducos',
           'descricao': 'Sociólogo, geek, cozinheiro e fã de esportes.',
           'url': 'http://twitter.com/cuducos',
           'nome_url': 'Twitter',
           'foto': 'https://avatars.githubusercontent.com/u/4732915?v=3&s=128'}

MENDES = {'nome': 'Eduardo Mendes',
          'descricao': 'Apaixonado por software livre e criador de lambdas.',
          'url': 'http://github.com/z4r4tu5tr4',
          'nome_url': 'GitHub',
          'foto': 'https://avatars.githubusercontent.com/u/6801122?v=3&s=128'}

PERFIS = {'cuducos': CUDUCOS,
          'z4r4tu5tr4': MENDES}


@meu_web_app.route('/<perfil>')
def pagina_inicial(perfil):
    perfil = PERFIS[perfil]
    return render_template('home.html', perfil=perfil)

if __name__ == "__main__":
    meu_web_app.run()
