import requests
from modelo import CategoriaContato, TipoTelefone

BASE_URL = 'http://127.0.0.1:8000'

print(f"Iniciando script de consumo da API da aplicação {BASE_URL} \n\n")

# Adicionando Contato 1
print('Adicionando contato 1')
parametros = {"nome" : "Adriano", "categoria" : CategoriaContato.PESSOAL} 
request_body = [
    {
        "numero" : 5130000000,
        "tipo" : TipoTelefone.FIXO
    },
    {
        "numero" : 5199999999,
        "tipo" : TipoTelefone.MOVEL
    },
]

req = requests.post(BASE_URL + '/adicionar', [], request_body, params = parametros)

# Consultar - Contato 1
print('\nConsultando contato id_contato = 1')
req = requests.get(BASE_URL + '/consultar/1')
print (req.json())

# Adicionando Contato 2
print('Adicionando contato 2')
parametros = {"nome" : "Maria", "categoria" : CategoriaContato.PESSOAL} 
request_body = [
    {
        "numero" : 51344444444,
        "tipo" : TipoTelefone.COMERCIAL
    },
    {
        "numero" : 5197777777,
        "tipo" : TipoTelefone.MOVEL
    },
]

req = requests.post(BASE_URL + '/adicionar', [], request_body, params = parametros)

# Consultar - Contato 2
print('\nConsultando contato id_contato = 2')
req = requests.get(BASE_URL + '/consultar/2')
print (req.json())

# Listar
print('\nListando todos os contatos')
req = requests.get(BASE_URL + '/listar')
print (req.json())