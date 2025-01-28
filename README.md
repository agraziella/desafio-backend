# API de Gerenciamento de Notícias

Este projeto consiste no desenvolvimento de uma **API para gerenciamento de notícias**. A API foi construída utilizando o **FastAPI**, um framework que permite criar aplicações rápidas e fáceis de usar. Com esta API, é possível realizar operações básicas (CRUD) para gerenciar notícias:

-   Criar novas notícias.
-   Listar todas as notícias.
-   Buscar notícias específicas pelo ID.
-   Atualizar informações de uma notícia existente.
-   Excluir notícias.

Além disso, foi configurado um servidor local para rodar a aplicação e testá-la por meio da documentação interativa gerada automaticamente pelo FastAPI. Foram utilizados princípios simples e boas práticas para garantir um projeto funcional e de fácil compreensão.


## Como rodar o projeto

**Pré-requisitos**

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

-   Python 3.9 ou superior
    
-   Gerenciador de pacotes `pip`
    
-   `virtualenv` para criar um ambiente virtual (opcional, mas recomendado)

### Passos para rodar o projeto

1.  Clone este repositório:
      ```
	git clone https://github.com/agraziella/desafio-backend.git
        cd desafio-backend
      ````
        
2. Crie um ambiente virtual (opcional):
	```
	python -m venv venv
	source venv/bin/activate
	```

   -No Windows: 
   
`venv\Scripts\activate`

4. Instale as dependências do projeto:
`pip install -r requirements.txt`

5. Inicie o servidor FastAPI:
`uvicorn main:app --reload` 

6.  Acesse a API no navegador ou via ferramentas como Postman e Insomnia:
    
    -   Documentação interativa: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
        
    -   Documentação alternativa: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Como testar os endpoints

### Ferramentas recomendadas

-   [Postman](https://www.postman.com/)
    
-   [Insomnia](https://insomnia.rest/)
    
-   [curl](https://curl.se/) para testes no terminal
    


### Endpoints principais

1.  **Listar Notícias**
    
    -   Método: `GET`
        
    -   URL: `/noticias`
        
    -   O que faz: Mostra todas as notícias cadastradas.
        
2.  **Criar Notícia**
    
    -   Método: `POST`
        
    -   URL: `/noticias`
        
    -   Envie este JSON no corpo da requisição:
		  ```json
		 {
		      "titulo": "Título da notícia",
		      "conteudo": "Conteúdo da notícia",
		      "autor": "Nome do autor"
		    }
		``` 
		1.  **Buscar Notícia pelo ID**
    
    -   Método: `GET`
        
    -   URL: `/noticias/{noticia_id}`
        
    -   O que faz: Busca uma notícia específica pelo ID.
        
2.  **Atualizar Notícia**
    
    -   Método: `PUT`
        
    -   URL: `/noticias/{noticia_id}`
        
    -   Envie este JSON no corpo da requisição:
		   ```json
		{
		  "titulo": "Novo título",
		  "conteudo": "Novo conteúdo",
		  "autor": "Novo autor"
		}
		```

1.  **Deletar Notícia**
    
    -   Método: `DELETE`
        
    -   URL: `/noticias/{noticia_id}`
        
    -   O que faz: Remove a notícia com o ID informado.
        

### Exemplo rápido com `curl`

Para criar uma notícia:
```
curl -X POST http://127.0.0.1:8000/noticias \
-H "Content-Type: application/json" \
-d '{"titulo": "Título exemplo", "conteudo": "Conteúdo exemplo", "autor": "Autor exemplo"}'
```


## Tecnologias usadas

-   **Python**: Linguagem principal do projeto.
    
-   **FastAPI**: Framework para criar a API.
    
-   **Uvicorn**: Servidor para rodar a aplicação.
    
-   **pip**: Gerenciador de pacotes para instalar as dependências.
    

----------

## Documentação Consultada
-  [Fast API](https://fastapi.tiangolo.com/)
- [Exemplo de Banco em Memória](https://gist.github.com/bsgabrielsilva/1d8d3ddc61b35c5315343e9924a642)

