import chromadb

def query_chromadb(question):
    client = chromadb.PersistentClient(path="./chromadb")
    collection = client.get_collection("CodeBase")
    
    result = collection.query(
        query_texts=[question],
        n_results=5
    )
    
    filepaths = result["metadatas"][0]
    codesnippets = result["documents"][0]
    
    response = [{"path": fp["file"], "snippet": cs} for fp, cs in zip(filepaths, codesnippets)]
    
    return response