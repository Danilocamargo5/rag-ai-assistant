# rag-ai-assistant

A hands-on AI Engineering project focused on building production-ready Generative AI applications.

The project is being developed incrementally to explore the architecture and engineering practices behind modern AI systems, including LLM integration, Retrieval-Augmented Generation (RAG), embeddings, vector databases, AI agents, tool calling, memory, multi-model orchestration, evaluation, observability, and cloud deployment.

The goal is not only to build a working AI assistant, but also to understand the engineering decisions required to make Generative AI applications reliable, scalable, observable, testable, and production-ready.

> 🚧 **This project is currently under active development.**  
> Several technologies and features described below are part of the planned roadmap and have not yet been implemented.

---

## 🎯 Project Goals

The main goals of this project are:

- Understand how LLM-based applications work beyond simple API calls
- Build REST APIs for AI applications using Python and FastAPI
- Integrate applications with different LLM providers
- Implement Retrieval-Augmented Generation (RAG)
- Understand embeddings and semantic search
- Work with vector databases
- Implement AI agents and tool calling
- Explore agent workflows with LangGraph
- Implement conversation memory
- Explore multi-model orchestration with LiteLLM
- Explore Model Context Protocol (MCP)
- Implement LLM and RAG evaluation strategies
- Add observability for tokens, latency, cost, and errors
- Apply resilience patterns to AI integrations
- Containerize the application with Docker
- Deploy AI workloads to cloud environments
- Integrate with AWS and Amazon Bedrock
- Apply CI/CD practices
- Document architectural decisions using ADRs

---

## 🏗️ Planned Architecture

The project will gradually evolve toward an architecture similar to:

```text
                         Client
                           │
                           ▼
                       FastAPI
                           │
                           ▼
                  Application Layer
                           │
               ┌───────────┴───────────┐
               │                       │
               ▼                       ▼
              RAG                    Agents
               │                       │
        Retrieval Pipeline          LangGraph
               │                    Tool Calling
               │                      Memory
               ▼                       │
         Vector Database               │
               │                       │
               └───────────┬───────────┘
                           │
                           ▼
                       LLM Layer
                           │
               ┌───────────┼───────────┐
               ▼           ▼           ▼
             Gemini     AWS Bedrock   Other LLMs
                           │
                           ▼
                    Observability
               Tokens / Cost / Latency
```

The architecture above represents the target architecture and will be implemented incrementally throughout the project.

---

## 🧰 Technology Stack

### Currently Implemented

- Python
- FastAPI
- Pydantic
- Uvicorn
- REST APIs
- OpenAPI / Swagger
- Python virtual environments
- Dependency management with pip

### Planned

- LLM APIs
- Google Gemini
- Amazon Bedrock
- Prompt Engineering
- Embeddings
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- pgvector
- LangChain
- LangGraph
- AI Agents
- Function / Tool Calling
- Conversation Memory
- LiteLLM
- Model Context Protocol (MCP)
- LLM Evaluation
- RAGAS / DeepEval
- LLM Observability
- Guardrails / PII protection
- Async APIs
- Streaming
- Retry strategies
- Circuit Breakers
- Docker
- AWS
- CI/CD
- Automated Tests
- Architecture Decision Records (ADRs)

---

# 🗺️ Development Roadmap

## Phase 1 — API Foundations ✅

Foundation of the application and REST API.

- [x] Python project setup
- [x] Virtual environment
- [x] Dependency management
- [x] FastAPI
- [x] Uvicorn
- [x] Health endpoint
- [x] POST endpoint
- [x] Pydantic models
- [x] Request validation
- [x] HTTP 422 validation handling
- [x] OpenAPI / Swagger

---

## Phase 2 — LLM Integration 🚧

Connect the application to its first Large Language Model.

- [ ] LLM provider integration
- [ ] Google Gemini integration
- [ ] Prompt structure
- [ ] System and user prompts
- [ ] Tokens
- [ ] Context windows
- [ ] Model parameters
- [ ] Error handling
- [ ] Provider abstraction

---

## Phase 3 — Retrieval-Augmented Generation (RAG) ⏳

Build the first complete RAG pipeline.

- [ ] Document ingestion
- [ ] Document loaders
- [ ] Text chunking
- [ ] Embeddings
- [ ] Semantic search
- [ ] Vector storage
- [ ] Retrieval
- [ ] Context injection
- [ ] RAG response generation

Target flow:

```text
Documents
    │
    ▼
Chunking
    │
    ▼
Embeddings
    │
    ▼
Vector Database
    │
    ▼
Retrieval
    │
    ▼
Relevant Context
    │
    ▼
LLM
    │
    ▼
Answer
```

---

## Phase 4 — Advanced RAG ⏳

Improve retrieval quality and architecture.

- [ ] pgvector
- [ ] Metadata filtering
- [ ] Hybrid search
- [ ] Reranking
- [ ] Source citations
- [ ] Retrieval optimization
- [ ] Context optimization

---

## Phase 5 — AI Agents ⏳

Extend the application beyond question answering.

- [ ] LangChain
- [ ] LangGraph
- [ ] Tool calling
- [ ] Function calling
- [ ] Agent workflows
- [ ] Conversation memory
- [ ] External API integration

---

## Phase 6 — LLM Integration Layer ⏳

Reduce coupling between the application and individual AI providers.

- [ ] LiteLLM
- [ ] Multi-model orchestration
- [ ] Provider abstraction
- [ ] Model routing
- [ ] Fallback strategies
- [ ] Model Context Protocol (MCP)

Target architecture:

```text
Application
     │
     ▼
LLM Gateway
     │
 ┌───┼────────────┐
 ▼   ▼            ▼
Gemini Bedrock  Other Providers
```

---

## Phase 7 — AI Quality & Evaluation ⏳

Measure AI behavior instead of relying only on manual testing.

- [ ] Unit tests
- [ ] Integration tests
- [ ] LLM evaluations
- [ ] RAG evaluations
- [ ] RAGAS
- [ ] DeepEval
- [ ] Prompt evaluation
- [ ] Guardrails
- [ ] PII protection

---

## Phase 8 — Production Engineering ⏳

Introduce production-grade software engineering practices.

- [ ] Async processing
- [ ] Response streaming
- [ ] Retry strategies
- [ ] Exponential backoff
- [ ] Circuit breakers
- [ ] Structured logging
- [ ] Error handling
- [ ] Token monitoring
- [ ] Latency monitoring
- [ ] Cost monitoring
- [ ] LLM observability

---

## Phase 9 — Cloud & Deployment ⏳

Prepare and deploy the application using cloud-native practices.

- [ ] Docker
- [ ] AWS integration
- [ ] Amazon Bedrock
- [ ] IAM
- [ ] Cloud deployment
- [ ] CI/CD
- [ ] GitHub Actions
- [ ] Production configuration
- [ ] Architecture documentation
- [ ] Architecture Decision Records (ADRs)

---

## 📚 Learning Documentation

The project includes documentation explaining the concepts learned during development.

```text
docs/
├── learning-guide.md
├── architecture/
│   └── architecture.md
└── adr/
```

The learning guide documents concepts such as:

- Python environment setup
- Virtual environments
- Dependency management
- FastAPI
- Pydantic
- REST APIs
- HTTP validation
- OpenAPI
- LLM concepts
- RAG concepts
- AI Engineering practices

The documentation will evolve together with the project.

---

## 📁 Current Project Structure

```text
rag-ai-assistant/
├── app/
│   ├── __init__.py
│   └── main.py
│
├── docs/
│   └── learning-guide.md
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

The project structure will evolve as new architectural layers are introduced.

---

## ▶️ Running the Project

Create the virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 🧠 Learning Approach

This project follows an incremental learning approach:

```text
Understand
    ↓
Implement
    ↓
Test
    ↓
Document
    ↓
Improve
```

Instead of starting with high-level AI frameworks, the project first explores the fundamental building blocks of AI Engineering.

Frameworks such as LangChain, LangGraph, LiteLLM, and RAG evaluation tools are introduced only after understanding the problems they solve.

---

## 📌 Project Status

```text
Phase 1 — API Foundations        ✅ Completed
Phase 2 — LLM Integration        🚧 In Progress
Phase 3 — RAG                    ⏳ Planned
Phase 4 — Advanced RAG           ⏳ Planned
Phase 5 — AI Agents              ⏳ Planned
Phase 6 — LLM Integration Layer  ⏳ Planned
Phase 7 — AI Quality             ⏳ Planned
Phase 8 — Production Engineering ⏳ Planned
Phase 9 — Cloud & Deployment     ⏳ Planned
```

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
