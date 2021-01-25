# automation-challenge-me
----------------------------------
Projeto de automação com base no site **Automation Practice**.

Projeto realizado em Python


#### Ferramentas utilizadas:
- Selenium;
- Behave;

----------------------------------

## Requisitos

É necessário instalar os `requirements.txt`.
###### Obs: No meu caso utilizo um ambiente virtual como boa prática. Para ativar o ambiente virtual`(opcional)`:
```bash
$ pipenv shell
```

----------------------------------

## Build
Antes de executarmos o projeto é necessário rodar um comando para instalação do requiriments.txt.
```bash
$ pip install -r requeriments.txt
```

Após isso, execute o selenium server com:

```bash
$ java -jar selenium-server-standalone-3.141.59.jar
```
###### Obs: Deixe executando para executar os testes.

----------------------------------

E por último, execute o projeto ou uma feature de sua escolha, com:
```bash
$ behave feature/
```

### Como utilizar?

Podemos executar o projeto das seguintes maneiras:
1. *behave feature/* **(Para executar todas as features);**
2. *behave feature/login.feature* **(Para executar feature específica, no caso a de login);**
3. *behave feature/login.feature:11* **(Para executar um cenário específico, passando o número da linha do cenário no gherkin);**


Foram criadas algumas variáveis no arquivo **behavi.ini**, sendo elas:
1. browser - Para definir o navegador que o projeto irá reproduzir. (Obs: Aceita Chrome e o Firefox. Default está o *chrome*)

2. background - Para definir se os testes irá ser executados em background ou não. (Aceita True/False. Default como False para acompanhar a execução)

3. debug - Para facilitar a investigação, caso falhe algum teste. (Aceita True/False. Default como False para não atrapalhar a execução)


#### Obs: Segue a baixo o link do site utilizado no projeto:

```
http://automationpractice.com/index.php
```


### Curiosidades:
- Caso falhe algum cenário, é salvo um screenshot da tela no momento da falha, para auxiliar na análise da falha;
- Qualquer dado gerado a partir da execução, é salvo no diretório *reports*;
- Áreas automatizadas:
  - Login;
  - Cadastro;
  - Campo de busca;
  - Área de contato;
- Após executar 1 vez, o teste de cadastro com sucesso, será necessário alterar o email para um ainda não cadastrado.
