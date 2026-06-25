import chromadb
from sentence_transformers import SentenceTransformer
import os
path=os.path.abspath("./VectorStore")
client = chromadb.PersistentClient(path=path)
collection = client.get_or_create_collection("hospitalvectors")
from langchain.tools import tool

model = SentenceTransformer("all-MiniLM-L6-v2")

@tool
def retrieve_hospital_info(query: str) -> str:
    """Retrieve hospital information from the vector database."""

    vector = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[vector],
        n_results=3,
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return "No relevant hospital information found."

    return 'query: ',query, "context: ","\n\n".join(documents)

