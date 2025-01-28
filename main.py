from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from datetime import datetime

#criaçao da aplicação FastAPI

app = FastAPI()


# Banco de dados em memória (dicionário)
banco = {}

# Modelo pra representar uma notícia
class Noticia(BaseModel):
    titulo: str
    conteudo: str
    autor: str

# Endpoint par alistar todas as notícias
@app.get("/noticias")
def listar_noticias():
    return banco

# Endpoint para listar uma notícia específica
@app.get("/noticias/{noticia_id}")
def buscar_noticia(id: str):
    noticia = banco.get(id)
    if noticia:
        return noticia
    return {"erro": "Notícia não encontrada"}  

# Endpoint para criar uma notícia
@app.post("/noticias")
def criar_noticia(noticia: Noticia):
    id = str(uuid.uuid4()) # Gera um ID único
    data_publicacao = datetime.now().isoformat()
    banco[id_noticia] = {
        "id": id_noticia,
        "titulo": noticia.titulo,
        "conteudo": noticia.conteudo,
        "autor": noticia.autor,
        data_publicacao: data_publicacao,
    }
    
    return banco[id_noticia]

# Endpoint para atualizar uma notícia
@app.put("/noticias/{noticia_id}")
def atualizar_noticia(id: str, noticia: Noticia):
   if id in banco:
       banco[id].update({
           "titulo": noticia.titulo,
           "conteudo": noticia.conteudo,
           "autor": noticia.autor,
       })
       return banco[id]
   return {"erro": "Notícia não encontrada"}

# Endpoint para deletar uma notícia
@app.delete("/noticias/{noticia_id}")
def deletar_noticia(id: str):
    if id in banco:
        del banco[id]
        return {"mensagem": "Notícia deletada com sucesso"}
    return {"erro": "Notícia não encontrada"}   

