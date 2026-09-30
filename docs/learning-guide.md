# RAG AI Assistant — Learning Guide

Este documento registra passo a passo a construção do projeto **RAG AI Assistant**.

O objetivo não é apenas construir uma aplicação funcionando, mas entender os principais conceitos de **Engenharia de IA**, relacionando-os, quando útil, com conceitos de Java, Spring Boot, APIs e Cloud.

---

# 1. Preparação do ambiente

## 1.1 Objetivo do projeto

O projeto será construído incrementalmente.

A evolução planejada é:

```text
REST API
   ↓
LLM
   ↓
Embeddings
   ↓
Vector Database
   ↓
RAG
   ↓
Agents / Tools
   ↓
Cloud / AWS
```

Cada etapa será adicionada somente depois que a anterior estiver funcionando e seus conceitos estiverem compreendidos.

---

# 2. Python

O projeto utiliza Python como linguagem principal.

Verificamos a versão instalada com:

```bash
python --version
```

No ambiente utilizado durante o desenvolvimento:

```text
Python 3.14.2
```

Python possui um ecossistema muito forte para Engenharia de IA, Machine Learning, LLMs e processamento de dados.

---

# 3. Ambiente virtual — venv

## O que é?

Um ambiente virtual permite criar um ambiente Python isolado para o projeto.

Criamos o ambiente com:

```bash
python -m venv .venv
```

Isso cria a pasta:

```text
.venv/
```

Ela contém o interpretador Python e as bibliotecas instaladas especificamente para esse ambiente.

## Ativando o ambiente

No Linux/macOS:

```bash
source .venv/bin/activate
```

Quando o ambiente está ativo, o terminal apresenta:

```text
(.venv)
```

Exemplo:

```text
(.venv) /workspaces/rag-ai-assistant
```

Isso indica que comandos como `python` e `pip` estão utilizando o ambiente virtual do projeto.

---

# 4. pip

`pip` é o gerenciador de pacotes do Python.

Ele possui uma função semelhante ao gerenciamento de dependências que fazemos com Maven ou Gradle no ecossistema Java.

Por exemplo:

```bash
pip install fastapi
```

instala a biblioteca FastAPI no ambiente Python atual.

Podemos verificar qual `pip` estamos utilizando com:

```bash
pip --version
```

No nosso projeto, o caminho apresentado contém:

```text
rag-ai-assistant/.venv/
```

Isso confirma que as dependências estão sendo instaladas dentro do ambiente virtual.

---

# 5. Primeiras dependências

Instalamos:

```bash
pip install fastapi "uvicorn[standard]"
```

## FastAPI

FastAPI é um framework Python utilizado para construção de APIs HTTP.

Para quem vem do ecossistema Java, podemos pensar nele, de maneira simplificada, como desempenhando parte do papel que Spring Web / Spring Boot desempenha na construção de APIs.

## Uvicorn

Uvicorn é um servidor ASGI utilizado para executar aplicações web Python.

Ele será responsável por executar nossa aplicação FastAPI.

---

# 6. Dependências transitivas

Ao instalar FastAPI e Uvicorn, percebemos que várias outras bibliotecas foram instaladas automaticamente.

Exemplos:

```text
pydantic
starlette
anyio
websockets
uvloop
```

Isso acontece porque uma biblioteca pode depender de outras bibliotecas.

De maneira simplificada:

```text
Nossa aplicação
      |
      +--- FastAPI
      |       |
      |       +--- Starlette
      |       +--- Pydantic
      |
      +--- Uvicorn
              |
              +--- h11
              +--- click
              +--- uvloop
              +--- websockets
```

Esse conceito é semelhante às **dependências transitivas do Maven**.

---

# 7. requirements.txt

Depois de instalar as dependências executamos:

```bash
pip freeze
```

Esse comando lista os pacotes instalados no ambiente Python atual e suas versões.

Exemplo:

```text
fastapi==0.141.1
pydantic==2.13.5
uvicorn==0.53.0
```

Depois executamos:

```bash
pip freeze > requirements.txt
```

O símbolo:

```text
>
```

é um operador do shell que redireciona a saída de um comando para um arquivo.

Portanto:

```text
pip freeze
      ↓
lista as dependências
      ↓
>
      ↓
requirements.txt
```

O arquivo `requirements.txt` registra as dependências utilizadas pelo projeto.

---

# 8. Reproduzindo o ambiente

Quando outro desenvolvedor clonar o projeto, ele poderá criar seu próprio ambiente virtual e instalar as mesmas dependências utilizando:

```bash
pip install -r requirements.txt
```

O `-r` indica que o `pip` deve ler as dependências de um arquivo.

Assim conseguimos reproduzir o ambiente utilizado durante o desenvolvimento.

---

# 9. Estrutura atual

Até este momento nosso projeto possui aproximadamente:

```text
rag-ai-assistant/
├── .venv/
├── docs/
│   └── learning-guide.md
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

A pasta `.venv` é utilizada somente no ambiente local e não deve ser versionada no Git.

---

# 10. Criando nossa primeira API com FastAPI

Criamos a pasta `app`, que será responsável por armazenar o código da aplicação.

A estrutura ficou:

```text
app/
├── __init__.py
└── main.py
```

## 10.1 Package Python

Criamos:

```text
app/__init__.py
```

O arquivo `__init__.py` permite que o diretório seja tratado como um package Python e possa participar de imports dentro da aplicação.

---

## 10.2 Importando FastAPI

No arquivo `main.py`:

```python
from fastapi import FastAPI
```

Estamos importando a classe `FastAPI` do pacote `fastapi`.

Uma comparação simplificada com Java seria:

```java
import alguma.biblioteca.FastAPI;
```

---

## 10.3 Criando a aplicação

Criamos uma instância de FastAPI:

```python
app = FastAPI()
```

Temos:

```text
FastAPI     → classe
FastAPI()   → criação de uma instância
app         → referência para essa instância
```

Conceitualmente, em Java teríamos algo semelhante a:

```java
FastAPI app = new FastAPI();
```

O objeto `app` representa nossa aplicação FastAPI.

---

# 11. Criando um endpoint

Criamos nosso primeiro endpoint:

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

## Decorator

A linha:

```python
@app.get("/health")
```

é um decorator Python.

Ela registra a função abaixo como responsável por requisições HTTP:

```text
GET /health
```

Para quem vem de Spring Boot, a ideia é semelhante a:

```java
@GetMapping("/health")
```

## Função

```python
def health_check():
```

`def` é utilizado para definir uma função em Python.

A função retorna:

```python
{"status": "ok"}
```

Esse valor é um `dict` Python.

O FastAPI serializa automaticamente esse objeto para JSON.

O cliente recebe:

```json
{
  "status": "ok"
}
```

---

# 12. Uvicorn

Para executar nossa aplicação utilizamos:

```bash
uvicorn app.main:app --reload
```

O comando pode ser entendido como:

```text
app.main:app
│   │    │
│   │    └── objeto app = FastAPI()
│   └────── arquivo main.py
└────────── package app
```

O parâmetro:

```text
--reload
```

faz o servidor reiniciar automaticamente quando alteramos o código durante o desenvolvimento.

---

# 13. Testando a API

Testamos nosso endpoint utilizando:

```bash
curl http://127.0.0.1:8000/health
```

O fluxo executado foi:

```text
curl
  │
  │ HTTP GET /health
  ▼
Uvicorn :8000
  │
  ▼
FastAPI
  │
  ▼
@app.get("/health")
  │
  ▼
health_check()
  │
  ▼
dict Python
  │
  │ serialização
  ▼
JSON
  │
  ▼
{"status":"ok"}
```

Nesse ponto temos nossa primeira aplicação HTTP funcionando com Python e FastAPI.

# 14. OpenAPI e Swagger

Ao criar endpoints com FastAPI, a aplicação gera automaticamente uma especificação da API utilizando o padrão **OpenAPI**.

## OpenAPI

OpenAPI é uma especificação utilizada para descrever APIs HTTP.

Ela pode descrever informações como:

```text
Endpoints
Métodos HTTP
Parâmetros
Request Body
Response Body
Status Codes
Schemas
```

O FastAPI disponibiliza essa especificação automaticamente em:

```text
/openapi.json
```

---

## Swagger UI

O **Swagger UI** utiliza a especificação OpenAPI para gerar uma interface visual e interativa da API.

No FastAPI, ela fica disponível automaticamente em:

```text
/docs
```

No nosso projeto, o Swagger identificou o endpoint:

```text
GET /health
```

e permitiu executar a requisição diretamente pelo navegador.

O teste retornou:

```text
HTTP 200
```

com:

```json
{
  "status": "ok"
}
```

---

## Relação entre FastAPI, OpenAPI e Swagger

Podemos visualizar o fluxo assim:

```text
Código Python
     ↓
FastAPI
     ↓
OpenAPI
     ↓
/openapi.json
     ↓
Swagger UI
     ↓
/docs
```

É importante diferenciar os conceitos:

**FastAPI** é o framework utilizado para construir nossa API.

**OpenAPI** é a especificação que descreve a API.

**Swagger UI** é uma interface visual que interpreta essa especificação.

---

## Executando pelo Swagger

Ao clicar em:

```text
Try it out
    ↓
Execute
```

o Swagger realizou uma requisição HTTP real para:

```text
GET /health
```

O fluxo foi:

```text
Swagger UI
    ↓
HTTP GET /health
    ↓
Uvicorn
    ↓
FastAPI
    ↓
health_check()
    ↓
HTTP 200
    ↓
JSON
```

O Swagger também gera automaticamente um exemplo de comando `curl` equivalente à requisição executada.

# Próximo passo

