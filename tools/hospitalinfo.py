import chromadb

import os
path=os.path.abspath("./VectorStore")
client = chromadb.PersistentClient(path=path)
collection = client.get_or_create_collection("hospitalvectors")
from langchain.tools import tool

from fastembed import TextEmbedding

embedding_model = TextEmbedding()
embeddings = list(embedding_model.embed(["Book an appointment"]))

def retrieve_hospital_info(query: str) -> str:
    """Retrieve hospital information from the vector database."""

    embeddings = list(embedding_model.embed([query]))

    results = collection.query(
        query_embeddings=embeddings,
        n_results=3,
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return "No relevant hospital information found."

    return 'query: ',query, "context: ","\n\n".join(documents)

print(retrieve_hospital_info('what is hospital name'))