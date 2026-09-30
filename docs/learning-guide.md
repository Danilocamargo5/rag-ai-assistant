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

# 15. POST, Pydantic e validação

Até agora nossa API possuía um endpoint simples de health check.

Agora criamos um endpoint que recebe dados enviados pelo cliente:

```text
POST /questions
```

O objetivo inicial ainda não é utilizar Inteligência Artificial.
Primeiro queremos entender como uma requisição entra na aplicação.

## Modelo de entrada com Pydantic

Criamos o seguinte modelo:

```python
class QuestionRequest(BaseModel):
    question: str
```

`BaseModel` pertence ao Pydantic.

Ele permite definir o contrato dos dados que nossa API espera receber.

Neste caso:

- `question` é obrigatório
- o valor deve ser uma string

Podemos pensar nesse modelo de forma semelhante a um DTO utilizado em Java/Spring.

Python:

```python
class QuestionRequest(BaseModel):
    question: str
```

Conceitualmente em Java:

```java
public class QuestionRequest {
    private String question;
}
```

## Endpoint POST

Criamos:

```python
@app.post("/questions")
def ask_question(request: QuestionRequest):
    return {"question": request.question}
```

O FastAPI recebe o JSON enviado no body e utiliza o Pydantic para convertê-lo e validá-lo antes de executar a função.

Fluxo:

```text
Cliente
   ↓
POST /questions
   ↓
FastAPI
   ↓
Pydantic
   ↓
Validação do QuestionRequest
   ↓
ask_question()
   ↓
Resposta JSON
```

## Requisição válida

Exemplo:

```json
{
  "question": "O que é RAG?"
}
```

A validação é realizada com sucesso e o endpoint é executado.

Resposta:

```json
{
  "question": "O que é RAG?"
}
```

HTTP Status:

```text
200 OK
```

Neste momento o endpoint apenas devolve a pergunta recebida.

Ainda não existe um LLM conectado ao endpoint.

## Requisição inválida

Testamos também:

```json
{
  "pergunta": "O que é RAG?"
}
```

Porém nosso contrato exige:

```text
question
```

Como o campo obrigatório não foi encontrado, o Pydantic detecta o problema antes da execução do endpoint.

O FastAPI retorna:

```text
HTTP 422
```

A resposta informa, entre outros detalhes:

```text
type: missing
loc: body → question
msg: Field required
```

Isso significa que o campo `question`, obrigatório no body, não foi enviado.

## O que significa HTTP 422?

Nesse contexto, significa que a requisição foi recebida e o JSON pôde ser interpretado, mas os dados enviados não atendem ao contrato esperado pela API.

Por exemplo:

```text
JSON válido

{
  "pergunta": "O que é RAG?"
}

        ↓

Pydantic espera:

question: str

        ↓

campo question não encontrado

        ↓

HTTP 422
```

O Pydantic não sabe que `pergunta` deveria significar `question`.

Ele apenas verifica o contrato definido pela aplicação.

## Validação antes do endpoint

Um ponto importante é que, quando ocorre um erro de validação, a função:

```python
ask_question()
```

não é executada.

A validação acontece antes da lógica do endpoint.

Fluxo com erro:

```text
Cliente
   ↓
JSON
   ↓
FastAPI
   ↓
Pydantic
   ↓
❌ Validação falhou
   ↓
HTTP 422
```

Isso evita que dados inválidos cheguem à lógica da aplicação.

## Tratamento de erros

Atualmente estamos utilizando a resposta padrão de validação do FastAPI/Pydantic.

Em uma API corporativa poderíamos posteriormente criar um tratamento global de erros para padronizar respostas.

Conceitualmente seria semelhante ao uso de:

```java
@ControllerAdvice
```

no Spring.

Não implementamos isso agora porque nosso foco principal é AI Engineering.

## Mapa mental

```text
FastAPI
→ API HTTP e roteamento

Pydantic
→ modelos, contrato e validação dos dados

Uvicorn
→ servidor que executa a aplicação

Swagger UI
→ interface para visualizar e testar a API

OpenAPI
→ especificação utilizada para descrever a API
```

## Conceito principal aprendido

Antes de executar a lógica da aplicação:

```text
HTTP Request
      ↓
FastAPI
      ↓
Pydantic
      ↓
Validação
      ↓
Endpoint
```

Assim, nossa lógica recebe dados que já passaram pela validação do contrato.

# 16. Primeira integração com um LLM

Nesta etapa realizamos nossa primeira chamada real para um Large Language Model (LLM).

Utilizamos a Gemini API como primeiro provider para evitar dependência de infraestrutura AWS durante as etapas iniciais do projeto.

## Provider vs Model

É importante diferenciar os dois conceitos:

```text
Aplicação
    ↓
Provider
    ↓
Model
```

O provider fornece a infraestrutura/API utilizada para acessar os modelos.

O model é o modelo de IA que efetivamente recebe nossa entrada e gera uma resposta.

Neste primeiro teste:

```text
Provider → Google Gemini API
Model    → Gemini Flash
```

Posteriormente o projeto poderá utilizar outros providers, como AWS Bedrock.

## API Key

Para autenticar nossa aplicação criamos uma API Key.

A chave não deve ser armazenada diretamente no código.

Criamos:

```text
.env
```

contendo:

```env
GEMINI_API_KEY=...
```

O arquivo `.env` foi adicionado ao `.gitignore` para evitar que credenciais sejam versionadas no Git.

## Carregando variáveis de ambiente

Utilizamos:

```python
from dotenv import load_dotenv

load_dotenv()
```

Depois podemos acessar a variável utilizando:

```python
import os

api_key = os.getenv("GEMINI_API_KEY")
```

Fluxo:

```text
.env
 │
 │ GEMINI_API_KEY
 ▼
python-dotenv
 │
 ▼
Variável de ambiente
 │
 ▼
os.getenv()
 │
 ▼
Aplicação
```

## SDK do Gemini

Instalamos o SDK:

```bash
pip install -U google-genai
```

O SDK fornece uma abstração Python para comunicação com a Gemini API.

Em vez de construirmos manualmente:

```text
HTTP Request
Headers
Authentication
JSON
Serialization
Response parsing
```

utilizamos o client fornecido pelo SDK.

## Criando o client

Criamos:

```python
from google import genai

client = genai.Client(api_key=api_key)
```

O `client` representa nosso ponto de comunicação com a Gemini API.

## Primeira inferência

Criamos inicialmente um arquivo isolado:

```text
test_gemini.py
```

O objetivo foi validar a integração antes de conectá-la ao FastAPI.

Enviamos um prompt semelhante a:

```text
Explique em uma frase o que é RAG.
```

O modelo respondeu com texto gerado pelo LLM.

Fluxo completo:

```text
Prompt
  ↓
Python
  ↓
Gemini SDK
  ↓
Gemini API
  ↓
LLM
  ↓
Inferência
  ↓
Resposta
```

## O que é inferência?

Nesta etapa não treinamos nenhum modelo.

Estamos utilizando um modelo que já foi treinado.

```text
Modelo treinado
      +
    Prompt
      ↓
  Inferência
      ↓
   Resposta
```

Inferência é o processo de utilizar um modelo treinado para produzir uma saída a partir de uma entrada.

## Erro 404 encontrado

Durante o primeiro teste recebemos:

```text
404 NOT_FOUND
```

O modelo inicialmente configurado não estava mais disponível para novos usuários.

Isso mostrou que modelos disponibilizados pelos providers podem mudar ao longo do tempo.

A aplicação precisa estar preparada para configuração e evolução dos modelos utilizados.

## Erro 503 encontrado

Em outra tentativa recebemos:

```text
503 Service Unavailable
```

Diferente do 404, esse erro indicava indisponibilidade temporária do serviço.

O SDK realizou tentativas novamente automaticamente.

Isso introduziu um conceito importante:

```text
Retry
```

Retry significa tentar novamente uma operação que falhou por uma condição potencialmente temporária.

Esse conceito será estudado posteriormente na etapa de resiliência da aplicação.

## Primeira chamada bem-sucedida

Depois da indisponibilidade temporária, executamos novamente:

```bash
python test_gemini.py
```

e recebemos uma resposta gerada pelo modelo.

Com isso validamos:

```text
Python
  ↓
API Key
  ↓
Gemini SDK
  ↓
Gemini API
  ↓
LLM
  ↓
Resposta
```

## Situação atual

A integração com o LLM ainda está isolada em:

```text
test_gemini.py
```

Ela ainda não está integrada ao endpoint:

```text
POST /questions
```

Isso foi proposital.

Primeiro validamos a comunicação com o provider de forma isolada.

## 17. Abstração de LLM Provider e integração com Gemini

Até este ponto, nossa API apenas recebia uma pergunta e devolvia o mesmo conteúdo.

Agora conectamos a aplicação a um LLM real.

### 17.1 Separação de responsabilidades

Em vez de colocar o código do Gemini diretamente no `main.py`, criamos uma camada específica para LLMs:

```text
app/
├── main.py
└── llm/
    ├── __init__.py
    ├── provider.py
    └── gemini_client.py
```

Responsabilidades:

- `main.py`: API HTTP e endpoints.
- `provider.py`: contrato que os providers de LLM devem implementar.
- `gemini_client.py`: implementação específica do Gemini.

Essa separação evita acoplar toda a aplicação diretamente a um único provedor.

---

### 17.2 O contrato LLMProvider

Criamos:

```python
from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
```

`ABC` significa **Abstract Base Class**.

O decorator:

```python
@abstractmethod
```

define que `generate()` deve ser implementado pelas classes concretas.

O contrato é:

```text
prompt: str
    ↓
LLMProvider
    ↓
response: str
```

Uma analogia aproximada em Java seria:

```java
public interface LLMProvider {

    String generate(String prompt);

}
```

Isso permitirá diferentes implementações:

```text
LLMProvider
     │
     ├── GeminiProvider
     ├── BedrockProvider
     └── outros providers
```

---

### 17.3 Implementação GeminiProvider

Criamos uma implementação concreta:

```python
class GeminiProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        ...
```

Portanto:

```text
LLMProvider
      ▲
      │ implementa
GeminiProvider
```

O `GeminiProvider` utiliza o SDK `google-genai` para enviar o prompt ao modelo.

---

### 17.4 Fluxo completo da requisição

O endpoint:

```text
POST /questions
```

agora executa o seguinte fluxo:

```text
Cliente
   ↓
FastAPI
   ↓
Pydantic
   ↓
GeminiProvider
   ↓
Gemini API
   ↓
LLM
   ↓
GeminiProvider
   ↓
FastAPI
   ↓
HTTP Response
```

Exemplo de entrada:

```json
{
  "question": "Qual a diferença entre LLM e RAG?"
}
```

Exemplo da estrutura de saída:

```json
{
  "question": "Qual a diferença entre LLM e RAG?",
  "answer": "Resposta gerada pelo modelo..."
}
```

---

### 17.5 Primeiro erro real de integração

Durante o primeiro teste, o provider retornou:

```text
503 Service Unavailable
```

O serviço informou que o modelo estava temporariamente sob alta demanda.

Isso mostrou uma diferença importante:

```text
Erro da nossa aplicação
        ≠
Erro de um serviço externo
```

Nossa aplicação conseguiu:

```text
FastAPI
   ↓
GeminiProvider
   ↓
Gemini API
```

mas o serviço externo estava temporariamente indisponível.

Uma nova tentativa retornou:

```text
HTTP 200 OK
```

e a resposta do LLM foi recebida corretamente.

Esse cenário será usado posteriormente para estudar:

- retries;
- timeout;
- tratamento de exceções;
- fallback;
- circuit breaker;
- observabilidade.

---

### 17.6 Situação atual da arquitetura

Atualmente temos:

```text
main.py
   ↓
GeminiProvider
   ↓
Gemini
```

Apesar de existir o contrato `LLMProvider`, o `main.py` ainda instancia diretamente:

```python
llm_provider = GeminiProvider()
```

Portanto, ainda existe dependência da implementação concreta.

O próximo objetivo arquitetural será evoluir para:

```text
              Application
                   ↓
              LLMProvider
                   │
          ┌────────┴────────┐
          ↓                 ↓
GeminiProvider       BedrockProvider
```

Assim poderemos trocar o provider sem alterar a lógica principal da API.

---

### 17.7 Conceitos aprendidos

Nesta etapa foram praticados:

- integração com um LLM real;
- provider de LLM;
- abstração;
- classe abstrata;
- `ABC`;
- `@abstractmethod`;
- separação de responsabilidades;
- inversão de dependência;
- integração com API externa;
- HTTP 503;
- diferença entre falha interna e falha de dependência externa;
- preparação para múltiplos providers.

A aplicação agora possui seu primeiro fluxo completo:

```text
HTTP → aplicação → LLM → aplicação → HTTP
```

O próximo passo será desacoplar a escolha do provider da camada HTTP.

O próximo passo será mover essa responsabilidade para uma camada própria da aplicação e então conectar o FastAPI ao LLM.