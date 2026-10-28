from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/health")
def health_check():
    # TODO: Retorne uma resposta indicando que a API está ativa.
    pass


@app.get("/books")
def list_books():
    # TODO: Retorne todos os livros cadastrados.
    pass


@app.post("/books", status_code=201)
def create_book(book_input: BookInput):
    # TODO: Crie um livro, atribua um id e retorne o livro criado.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Retorne o livro correspondente ou uma resposta 404.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book_input: BookInput):
    # TODO: Atualize o livro correspondente ou retorne uma resposta 404.
    pass


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    # TODO: Remova o livro correspondente ou retorne uma resposta 404.
    pass
