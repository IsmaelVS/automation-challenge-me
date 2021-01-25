# language: pt
# encoding: utf-8

Funcionalidade: Validação do campo de busca

  Eu, como um usuário da plataforma, desejo realizar uma busca.

  Contexto:
    Dado que acesso o link

  Esquema do Cenário: Validação de busca <status>
    Quando realizo uma busca por "<value>"
    Então devo ter "<result>" items encontrados

  Exemplos:
    | status   | result | value   |
    | valida   | 5      | Printed |
    | inválida | 0      | Python  |
