# language: pt
# encoding: utf-8

Funcionalidade: Validação de login

  Eu, como um usuário da plataforma, desejo realizar o login.

  Contexto:
    Dado que acesso o link

  Cenário: Validação de login correto
    E realizo o login com os campos "teste.me@teste.com" e "devel123"
    Então o login deve ser finalizado com "sucesso"
    E devo deslogar

  Esquema do Cenário: Validação de login <status>
    E realizo o login com os campos "<email>" e "<password>"
    Então o login deve ser finalizado com "<message>"

  Exemplos:
    | status    | email                     | password | message                    |
    | incorreto | teste_incorreto@teste.com | devel123 | Authentication failed.     |
    | vazio     |                           |          | An email address required. |
