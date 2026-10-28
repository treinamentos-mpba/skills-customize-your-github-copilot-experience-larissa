# 📘 Atividade: Testes Automatizados para APIs FastAPI

## 🎯 Objetivo

Escreva testes automatizados para a API de livros criada na atividade Building REST APIs with FastAPI. Use `pytest` e `TestClient` para verificar respostas bem-sucedidas, operações CRUD, validação de dados e erros HTTP.

## 📝 Tarefas

### 🛠️ Preparar pytest e testar endpoints básicos

#### Descrição
Instale as dependências de teste e crie um arquivo `test_main.py` na mesma pasta do `main.py` da atividade Building REST APIs with FastAPI. Configure o `TestClient` para exercitar a API sem iniciar um servidor externo.

#### Requisitos
O programa concluído deve:

- Instalar `pytest` e `httpx` no ambiente Python usado pela API.
- Importar a aplicação FastAPI de `main.py` e criar um `TestClient`.
- Testar `GET /health`, verificando o status HTTP `200` e a resposta que indica que a API está ativa.
- Testar `GET /books`, verificando o status HTTP `200` e que a resposta é uma lista.
- Executar os testes com `python -m pytest -q`.

### 🛠️ Testar o ciclo CRUD de livros

#### Descrição
Escreva um teste que crie um livro e use o identificador retornado para consultar, atualizar e remover o mesmo recurso.

#### Requisitos
O programa concluído deve:

- Confirmar que `POST /books` cria um livro válido e retorna status HTTP `201`.
- Confirmar que `GET /books/{book_id}` retorna o livro criado, incluindo título, autor e identificador.
- Confirmar que `PUT /books/{book_id}` atualiza os dados e que uma nova consulta retorna os valores atualizados.
- Confirmar que `DELETE /books/{book_id}` retorna status HTTP `204` e remove o livro.

### 🛠️ Verificar validação e respostas de erro

#### Descrição
Adicione testes para entradas inválidas e identificadores inexistentes, verificando que a API comunica os erros com os status HTTP apropriados.

#### Requisitos
O programa concluído deve:

- Confirmar que uma criação com título ou autor vazio retorna status HTTP `422`.
- Confirmar que `GET`, `PUT` e `DELETE` com um identificador inexistente retornam status HTTP `404`.
- Usar asserções explícitas para verificar o status e, quando relevante, os dados da resposta.
- Executar toda a suíte com `python -m pytest -q` e corrigir os testes que falharem.