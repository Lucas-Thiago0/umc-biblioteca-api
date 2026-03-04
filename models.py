from pydantic import BaseModel

class Autor(BaseModel):
    id: int
    nome: str

class Livro(BaseModel):
    id: int
    titulo: str
    id_autor: int  # Relaciona o livro ao autor pelo ID
    editora: str
    isbn: str
    resumo: str