from fastapi import FastAPI, HTTPException
from models import Autor, Livro
from typing import List

app = FastAPI(title="Acervo Biblioteca UMC - Exercício 2")

# armazena os "bancos" em memória
autores_db: List[Autor] = []
livros_db: List[Livro] = []

# modulo de autores

@app.post("/api/autores")
def cadastrar_autor(autor: Autor):
    autores_db.append(autor)
    return autor

@app.get("/api/autores")
def listar_autores():
    return autores_db

# REQUISITO: Listar todos os livros de um autor específico
@app.get("/api/autores/{autor_id}/livros")
def listar_livros_por_autor(autor_id: int):
    # Usando list comprehension para filtrar
    livros_filtrados = [l for l in livros_db if l.id_autor == autor_id]
    return livros_filtrados

# modulo de livros

@app.post("/api/livros")
def cadastrar_livro(livro: Livro):
    # Validação de segurança: o autor existe?
    autor_existe = any(a.id == livro.id_autor for a in autores_db)
    if not autor_existe:
        raise HTTPException(status_code=400, detail="Erro: Autor não cadastrado.")
    
    livros_db.append(livro)
    return livro

@app.get("/api/livros/{id}")
def ver_detalhes(id: int):
    for l in livros_db:
        if l.id == id:
            return l
    return {"erro": "Livro não encontrado"}

@app.put("/api/livros/{id}")
def alterar_livro(id: int, novos_dados: Livro):
    for i, l in enumerate(livros_db):
        if l.id == id:
            livros_db[i] = novos_dados
            return novos_dados
    return {"erro": "ID inválido"}

@app.delete("/api/livros/{id}")
def remover_livro(id: int):
    for i, l in enumerate(livros_db):
        if l.id == id:
            livros_db.pop(i)
            return {"status": "Livro removido com sucesso!"}
    return {"status": "Erro: Livro não localizado"}