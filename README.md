# Foundational RAG System (Local LLM)

This project is a learning-focused implementation of a Retrieval-Augmented Generation (RAG) pipeline built from scratch.

## What this project demonstrates
- PDF document ingestion
- Text chunking
- Semantic embeddings
- Vector-based similarity search
- Context-grounded answer generation
- Local LLM inference using Ollama

## What this project is NOT
- Not production-scale
- Not optimized for speed
- Not deployed as a web application

## Why local LLM?
A local LLM is used to avoid API dependency and focus on understanding the RAG architecture deeply.  
The LLM layer is modular and can be replaced with a cloud-based API later.

## Key Learnings
- RAG pipeline design
- Embedding-based retrieval
- Prompt grounding and hallucination control
- Tradeoffs between local and cloud LLMs

## How to run
1. Install dependencies  
   `pip install -r requirements.txt`

2. Install Ollama  
   https://ollama.com

3. Pull a lightweight model  
   `ollama pull phi3`

4. Run the project  
   `python main.py`
