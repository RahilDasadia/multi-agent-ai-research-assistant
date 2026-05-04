# Multi-Agent AI Research Assistant

A **multi-agent AI research system** that performs automated research, analysis, and report generation using a collaborative agent architecture.

The system combines **FastAPI**, **Ollama (Llama3)**, and **Retrieval-Augmented Generation (RAG)** to generate structured insights through a **chat-style web interface**.

---

# Overview

This project demonstrates how multiple AI agents can collaborate to solve complex tasks such as research and analysis.

Each agent has a specific responsibility:

- **Researcher Agent** gathers information and retrieves documents
- **Analyst Agent** analyzes insights and identifies patterns
- **Writer Agent** produces structured final responses

The system integrates a **vector database for document retrieval**, **tool usage**, and **streaming responses** to create a powerful AI research assistant.

---

# Key Features

- Multi-agent AI architecture
- Retrieval-Augmented Generation (RAG)
- Local LLM using **Ollama + Llama3**
- Vector database using **ChromaDB**
- Tool usage (calculator + system utilities)
- Streaming responses
- Chat-style web interface
- Modular backend with FastAPI
- Conversation-style prompt interface

---

# Architecture

The system workflow:


User Query
↓
Web Chat Interface
↓
FastAPI Backend
↓
Orchestrator
↓
Researcher Agent
↓
(Optional) Analyst Agent
↓
Writer Agent
↓
Final Response


The Researcher agent can also use:


Vector Database (RAG)
Tools (Calculator / System Tools)
Local LLM (Ollama)


---

# Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy

## AI & LLM
- Ollama
- Llama3
- Sentence Transformers

## Data & Storage
- ChromaDB (Vector Database)
- SQLite (Task History)

## Frontend
- HTML
- CSS
- JavaScript

---

# Project Structure


backend
│
├── app
│ ├── agents
│ │ ├── researcher.py
│ │ ├── analyst.py
│ │ ├── writer.py
│ │ └── schemas.py
│ │
│ ├── orchestrator
│ │ └── engine.py
│ │
│ ├── rag
│ │ ├── retriever.py
│ │ ├── chunker.py
│ │ └── vector_store.py
│ │
│ ├── tools
│ │ ├── calculator.py
│ │ ├── system_tools.py
│ │ └── tool_manager.py
│ │
│ ├── db
│ │ ├── models.py
│ │ ├── session.py
│ │ └── base.py
│ │
│ ├── llm
│ │ └── ollama_client.py
│ │
│ ├── frontend
│ │ └── index.html
│ │
│ └── main.py
│
├── knowledge
│ └── documents
│
└── requirements.txt


---

# Installation

### 1. Clone the repository


git clone https://github.com/YOURUSERNAME/multi-agent-ai-research-assistant.git


### 2. Navigate to the backend folder


cd backend


### 3. Install dependencies


pip install -r requirements.txt


---

# Install Ollama

Install Ollama from:


https://ollama.com


Download the model:


ollama pull llama3


Start Ollama server:


ollama serve


---

# Run the Application

Start the FastAPI server:


uvicorn app.main:app --reload


Open the application in browser:


http://127.0.0.1:8000


---

# Example Queries

You can test the system using prompts like:


AI in healthcare
What are the challenges of AI in healthcare?
Compare AI and blockchain in finance
30 * 7
What is the system time?


---

# Future Improvements

Potential enhancements for the project:

- Persistent conversation memory
- Agent reasoning visualization
- Docker containerization
- Cloud deployment
- User authentication
- Advanced tool integration

---

# Author

Developed by **Rahil Dasadia**

This project was built as a learning exercise to explore **multi-agent AI systems, RAG architectures, and LLM integration**.

---
