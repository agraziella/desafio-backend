from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from datetime import datetime

# Criação da aplicação FastAPI
app = FastAPI()

# Banco de dados em memória (dicionário simples)
banco = {}

# Modelo para representar uma notícia
class Noticia(BaseModel):
    titulo: str
    conteudo: str
    autor: str
    
# Criando a aplicação com metadados
app = FastAPI(
    title="API de Gerenciamento de Notícias",
    version="0.1.0",
    description="""
Esta API foi criada para gerenciar notícias de forma simples e eficiente. 
Com ela, é possível criar, listar, buscar, atualizar e excluir notícias. 
A aplicação utiliza o framework FastAPI, que é conhecido por sua alta performance e facilidade de uso.
"""
)
    
# Rota para a raiz do servidor
@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API!"}

# Endpoint para listar todas as notícias (GET /noticias)
@app.get("/noticias")
def listar_noticias():
    return {"status": "success", "data": banco}

# Endpoint para listar uma notícia específica (GET /noticias/{id})
@app.get("/noticias/{noticia_id}")
def buscar_noticia(noticia_id: str):
    if noticia_id in banco:
        return {"status": "success", "data": banco[noticia_id]}
    return {"status": "error", "message": "Notícia não encontrada"}

# Endpoint para criar uma notícia (POST /noticias)
@app.post("/noticias")
def criar_noticia(noticia: Noticia):
    id = str(uuid.uuid4())  # Gera um ID único para a notícia
    data_publicacao = datetime.now().isoformat()  # Gera a data de publicação
    banco[id] = {
        "id": id,
        "titulo": noticia.titulo,
        "conteudo": noticia.conteudo,
        "autor": noticia.autor,
        "data_publicacao": data_publicacao,  # Adiciona a data de publicação
    }
    return {"status": "success", "data": banco[id]}

# Endpoint para atualizar uma notícia (PUT /noticias/{id})
@app.put("/noticias/{noticia_id}")
def atualizar_noticia(noticia_id: str, noticia: Noticia):
    if noticia_id in banco:
        banco[noticia_id].update({
            "titulo": noticia.titulo,
            "conteudo": noticia.conteudo,
            "autor": noticia.autor,
        })
        return {"status": "success", "data": banco[noticia_id]}
    return {"status": "error", "message": "Notícia não encontrada"}

# Endpoint para deletar uma notícia (DELETE /noticias/{id})
@app.delete("/noticias/{noticia_id}")
def deletar_noticia(noticia_id: str):
    if noticia_id in banco:
        del banco[noticia_id]
        return {"status": "success", "message": "Notícia deletada com sucesso"}
    return {"status": "error", "message": "Notícia não encontrada"}
