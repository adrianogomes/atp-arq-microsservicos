# Introdução

Atividade Prática (ATP 05) da Disciplina de Arquitetura de Micro-Serviços da Especialização em Engenharia de Software para Aplicações de Ciência de Dados - UFRGS

# Aplicação 

Foi implementada uma API microsserviços REST possibilitando as operações de inclusão, consulta e lista de uma agenda de contatos. Cada contato possui um nome, uma lista de telefones e uma categoria. Para cada telefone está associado um número e um tipo.

# Execução

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