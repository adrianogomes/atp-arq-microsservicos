from fastapi import FastAPI, HTTPException
from tinydb import TinyDB, Query
from modelo import Telefone, CategoriaContato

app = FastAPI()

db  = TinyDB('database.json')
ContatoQuery = Query()

# Inclusão de um contato
@app.post('/adicionar')
def adicionar(nome: str, telefones : list[Telefone], categoria : CategoriaContato):
    if db.all() == [] :
        id_contato = 1
    else:
        id_contato = max([contato["id_contato"] for contato in db.all()]) + 1;

    db.insert({
        "id_contato" : id_contato,
        "nome" : nome,
        "telefones" : [telefone.model_dump() for telefone in telefones],
        "categoria" : categoria
    })

    return {"message" : "Contato criado com sucesso"}

# Consulta de um contato
@app.get('/consultar/{id_contato}')
def consultar(id_contato : int):
    contato = db.search(ContatoQuery.id_contato == id_contato)

    if contato == []:
        raise HTTPException(status_code=400, detail="Contato não encontrado")
    
    return contato

# Listar contatos cadastrados
@app.get('/listar')
def listar():
    contatos = db.all()

    if contatos == []:
        raise HTTPException(status_code=400, detail="Sem contatos cadastrados")
    
    return contatos
