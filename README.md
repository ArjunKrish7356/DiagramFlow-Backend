# DiagramFlow Backend

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)

## Overview

DiagramFlow Backend is a powerful codebase analysis service that intelligently extracts and processes information from Python repositories. Built with FastAPI, it provides RESTful endpoints for cloning Git repositories, parsing Python code structures, and generating interactive insights through an AI-powered chat interface.

## Demo

https://github.com/user-attachments/assets/5d8b3baf-1057-43db-9608-99a84bb6869d

## ✨ Key Features

- **🔍 Intelligent Code Analysis**: Automatically parses Python files to extract classes, functions, and dependencies
- **📊 Structured Data Export**: Generates comprehensive JSON reports of codebase structure
- **🤖 AI-Powered Chat Interface**: Query your codebase using natural language through ChromaDB integration
- **🌐 Git Repository Integration**: Clone and analyze repositories directly from Git URLs
- **⚡ Fast API Backend**: High-performance REST API built with FastAPI
- **🐳 Docker Ready**: Containerized deployment for easy scaling

## 🏗️ Architecture

### Core Components

- **`server.py`**: FastAPI application server with health checks and main endpoints
- **`gitCloner.py`**: Git repository cloning and directory management utilities
- **`parser_pyfile.py`**: Python AST-based code parsing and analysis engine
- **`ChatInterface.py`**: AI-powered natural language interface for codebase queries
- **`pushToChromaDB.py` & `fetchFromChromaDB.py`**: Vector database integration for semantic code search
- **`main.py`**: Core directory traversal and analysis orchestration

### Data Flow

1. **Repository Ingestion**: Clone Git repositories or process local directories
2. **Code Parsing**: Extract structural information using Python AST
3. **Vector Storage**: Store code snippets in ChromaDB for semantic search
4. **API Exposure**: Serve analysis results and chat functionality via REST endpoints

## 🚀 Quick Start

### Prerequisites

- Python 3.10
- Git (for repository cloning)

### Local Development Setup

1. **Create and activate virtual environment**:
   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server**:
   ```bash
   fastapi run server.py
   ```

The API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/docs`.

### Docker Deployment

For production deployment or if you prefer containerized environments:

1. **Build the Docker image**:
   ```bash
   docker build -t diagramflow-backend .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 diagramflow-backend
   ```

## 📡 API Endpoints

### Health Check
```http
GET /health
```
Returns the service status.

### Generate AI Response
```http
POST /generate
Content-Type: application/json

{
  "question": "How does the authentication work in this codebase?"
}
```

### Clone and Analyze Repository
```http
POST /clonerepo
Content-Type: application/json

{
  "url": "https://github.com/username/repository.git"
}
```

## 📁 Output Files

- **`formats/codebase.json`**: Comprehensive structural analysis of the codebase
- **`chromadb/`**: Vector database containing code embeddings for semantic search
- **`logs/app.log`**: Application logs and analysis details

## 🛠️ Development

### Project Structure
```
DiagramFlow-Backend/
├── server.py              # FastAPI application
├── gitCloner.py           # Git operations
├── parser_pyfile.py       # Code analysis
├── ChatInterface.py       # AI chat interface
├── pushToChromaDB.py      # Vector DB operations
├── fetchFromChromaDB.py   # Vector DB queries
├── main.py                # Core orchestration
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
└── formats/              # Output directory
    └── codebase.json     # Analysis results
```

### Docker Configuration

The included Dockerfile provides a lightweight, production-ready container:

```dockerfile
# Creating from Python 3.10 image
FROM python:3.10

WORKDIR /app

COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Run FastAPI using Uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

