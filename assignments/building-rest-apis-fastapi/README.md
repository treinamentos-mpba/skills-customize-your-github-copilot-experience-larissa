# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar livros usando FastAPI. Você praticará a criação de rotas, operações CRUD, validação de dados e respostas HTTP.

## 📝 Tarefas

### 🛠️ Criar a aplicação e as primeiras rotas

#### Descrição
Configure uma aplicação FastAPI para uma biblioteca e crie rotas para verificar se a API está funcionando e consultar os livros cadastrados.

#### Requisitos
O programa concluído deve:

- Criar uma instância da aplicação FastAPI.
- Implementar `GET /health` com uma resposta que indique que a API está ativa.
- Implementar `GET /books` para retornar a lista de livros, inicialmente vazia.
- Iniciar a aplicação localmente e acessar a documentação interativa em `/docs`.

### 🛠️ Implementar operações CRUD para livros

#### Descrição
Permita que clientes criem, consultem, atualizem e removam livros da biblioteca. Nesta atividade, os dados podem ficar armazenados em memória.

#### Requisitos
O programa concluído deve:

- Definir um modelo de livro com `id`, `title` e `author`; título e autor não podem ser vazios.
- Implementar `POST /books` para cadastrar um livro e retornar o recurso criado com status HTTP `201`.
- Implementar `GET /books/{book_id}` para consultar um livro pelo identificador.
- Implementar `PUT /books/{book_id}` para atualizar título e autor.
- Implementar `DELETE /books/{book_id}` para remover um livro.
- Retornar status HTTP `404` quando uma consulta, atualização ou remoção usar um identificador inexistente.

### 🛠️ Validar e testar a API

#### Descrição
Use a documentação interativa ou um cliente HTTP para testar os endpoints e confirmar que a API responde corretamente a entradas válidas e inválidas.

#### Requisitos
O programa concluído deve:

- Testar a criação, consulta, atualização e remoção de pelo menos um livro.
- Confirmar que os dados inválidos são rejeitados pela validação do modelo.
- Confirmar que operações com um identificador inexistente retornam `404`.
- Registrar exemplos de requisição e resposta para cada operação CRUD.
