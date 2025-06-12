# DiagramFlow

## Description

DiagramFlow is a tool that analyzes a Python codebase and extracts information about its structure, dependencies, and components. It parses Python files, identifies classes, functions, and imports, and stores this information in a JSON format. The code snippets are also pushed to ChromaDB for further analysis.

## Functionality

The application performs the following steps:

1.  **Directory Traversal:** Recursively traverses a specified directory (default: `./DirectoryToConvert`).
2.  **Python File Parsing:** Parses Python files (`.py`) using the `parser_pyfile.py` module.
3.  **Codebase Information Extraction:** Extracts key information, including class names, function names, and imports.
4.  **ChromaDB Integration:** Pushes code snippets to ChromaDB, a vector database, for further analysis and retrieval.
5.  **JSON Output:** Stores the extracted information in a JSON file named `codebase.json`.

## Modules

*   `parser_pyfile.py`: This module is responsible for parsing Python files and extracting relevant information. It uses the `ast` module to create an Abstract Syntax Tree (AST) of the code, then traverses the AST to identify classes, functions, and imports. The extracted information is stored in a global `codebase` dictionary. It also integrates with ChromaDB by calling the `push_to_chromadb` function to store code snippets.
*   `gitCloner.py`: (Potentially) used for cloning Git repositories (details need further investigation).
*   `fetchFromChromaDB.py` and `pushToChromaDB.py`: These modules are used for interacting with ChromaDB. `pushToChromaDB.py` pushes code snippets to ChromaDB, while `fetchFromChromaDB.py` likely retrieves code snippets from ChromaDB based on certain queries.
*   `ChatInterface.py`: Provides a chat interface for interacting with the codebase information.
*   `server.py`: Runs a server to expose the functionality of the application.

## Usage

1.  Place the Python files you want to analyze in the `./DirectoryToConvert` directory.
2.  Run the `backend/main.py` script.
3.  The extracted codebase information will be stored in `codebase.json`.
4.  Code snippets will be stored in ChromaDB in the `./chromadb` directory.

## Further Investigation

The following aspects of the project require further investigation:

*   The exact purpose and functionality of `gitCloner.py`.
*   The schema and structure of the `codebase.json` file.
*   The role of ChromaDB in storing and retrieving codebase information.
*   The implementation and features of the chat interface (`ChatInterface.py`).
*   The API endpoints and functionality exposed by the server (`server.py`).
