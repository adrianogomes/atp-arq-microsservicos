# Introdução

Atividade Prática (ATP 05) da Disciplina de Arquitetura de Micro-Serviços da Especialização em Engenharia de Software para Aplicações de Ciência de Dados - UFRGS

# Aplicação 

Foi implementada uma API microsserviços REST possibilitando as operações de inclusão, consulta e lista de uma agenda de contatos. Cada contato possui um nome, uma lista de telefones e uma categoria. Para cada telefone está associado um número e um tipo.

# Execução - manual

Abaixo segue os passos necessários para inicialização da API e do script para o consumo da API, de forma manualmente com comandos no terminal.

## Dependências
Para instalar as dependências necessárias, executar o seguinte comando no terminal:

```
pip install -r requirements.txt
```

## Inicialização do servidor
Após a instalação das dependências é necessário inicializar o servidor da API com o seguinte comando:

```
fastapi dev app.py
```

## Consumo da API
Com o servidor iniciado (manter terminal aberto), abrir um novo terminal e executar o seguinte comando para rodar o script de testes de consumo da API.

```
python run.py
```


# Execução - container

Abaixo segue os passos necessários para inicialização da API em um container e a execução do script do consumo da API pelo terminal.
Necessário ter instalado o Docker.


Inicialmente necessário contruir usando o comando

```
docker build -t servico .
```

Após usar o seguinte comando para iniciar o servidor da API

```
docker run -d -p 8001:8001 servico
```

Com o servidor iniciado executar o seguinte comando no terminal para rodar o script de testes de consumo da API.

```
python run.py
```