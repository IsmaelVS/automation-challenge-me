# language: pt
# encoding: utf-8

Funcionalidade: Validação da área de contato

  Eu, como um usuário da plataforma, entrar em contato com a área de suporte.

  Contexto:
    Dado que acesso o link

  Cenário: Validação de envio de mensagem
    E acesso a área de contato
    Quando preencho com os seguintes dados
    | Name    | Value              |
    | subject | Webmaster          |
    | email   | teste.me@teste.com |
    | order   | order teste        |
    | message | mensagem teste     |
    Então a mensagem deve ser enviada com "sucesso"

  Cenário: Validação de dados inclompletos
    E acesso a área de contato
    Quando preencho com os seguintes dados
    | Name    | Value              |
    | subject | Webmaster          |
    | email   | teste.me@teste.com |
    | order   | order teste        |
    | message |                    |
    Então a mensagem deve ser enviada com "falha"
