# Multi-Agent AI Research Assistant

A multi-agent AI system that performs research, analysis and report generation using a collaborative agent architecture.

The system integrates **FastAPI**, **Ollama (Llama3)** and **Retrieval-Augmented Generation (RAG)** to provide structured responses through a web-based chat interface.

---

## Features

- Multi-agent architecture
- Retrieval-Augmented Generation (RAG)
- Tool usage (calculator and system utilities)
- Streaming responses
- Chat-based web interface
- Local LLM using Ollama
- Vector database for document retrieval
- Modular agent orchestration

---

## Agents

The system uses specialized AI agents:

**Researcher Agent**
- gathers information
- retrieves relevant documents
- performs initial reasoning

**Analyst Agent**
- analyzes research findings
- extracts insights and patterns

**Writer Agent**
- produces structured final reports

---

## Tech Stack

Backend

- Python
- FastAPI
- SQLAlchemy

AI

- Ollama
- Llama3
- Sentence Transformers

Data

- ChromaDB
- SQLite

Frontend

- HTML
- CSS
- JavaScript

---

## Project Structure
