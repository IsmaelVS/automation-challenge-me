# language: pt
# encoding: utf-8

Funcionalidade: Validação de cadastro

  Eu, como um usuário, desejo me cadastrar na plataforma.

  Contexto:
    Dado que acesso o link

  Cenário: Validação de cadastro
    Quando preencho com o seguinte email "hihi@hihi.com"
    Então deve ser preenchido com os seguintes dados
    | Name         | Value                |
    | title        | Mr.                  |
    | first name   | teste                |
    | last name    | ME                   |
    | email        | isma@me.com          |
    | password     | xpto12345            |
    | day          | 2                    |
    | month        | May                  |
    | year         | 1998                 |
    | newletter    | True                 |
    | partners     | True                 |
    | company      | ME                   |
    | address1     | Rua da automatização |
    | address2     | Rua dos Bugs         |
    | city         | buglândia            |
    | state        | Hawaii               |
    | post code    | 12345                |
    | country      | United States        |
    | other        | hehe                 |
    | phone        | 199999999            |
    | phone_mobile | 199999999            |
    | alias        | teste                |
    E deve ser cadastrado

  Cenário: Cadastro incompleto
    Quando preencho com o seguinte email "hihihi@me.com"
    Então deve ser preenchido com os seguintes dados
    | Name         | Value                |
    | title        | Mr.                  |
    | first name   | teste                |
    | last name    | ME                   |
    | email        | isma@me.com          |
    | password     | xpto                 |
    | day          | 2                    |
    | month        | May                  |
    | year         | 1998                 |
    | newletter    | True                 |
    | partners     | True                 |
    | company      | ME                   |
    | address1     | Rua da automatização |
    | address2     | Rua dos Bugs         |
    | city         | buglândia            |
    | state        | Hawaii               |
    | post code    | 12345                |
    | country      | United States        |
    | other        | hehe                 |
    | phone        | 199999999            |
    | phone_mobile | 199999999            |
    | alias        | teste                |
    Então deve exibir a mensagem de erro

  Cenário: Validação de email já cadastrado
    Quando preencho com o seguinte email "teste.me@teste.com"
    Então deve exibir a mensagem de erro

  Cenário: Validação de email inválido
    Quando preencho com o seguinte email "teste.inválido.com"
    Então deve exibir a mensagem de erro
