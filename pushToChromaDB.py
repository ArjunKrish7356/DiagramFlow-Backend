import chromadb
import uuid

def push_to_chromadb(code,nodename,filepath):
    try:
        client = chromadb.PersistentClient(path="./chromadb")
        collection = client.get_or_create_collection("CodeBase")

        collection.add(
            documents=[code],
            ids = [str(uuid.uuid4())],
            metadatas=[{"name": nodename, "file": filepath}]
        )

    except Exception as e:
        print(f"PushToDB error : {e}")
