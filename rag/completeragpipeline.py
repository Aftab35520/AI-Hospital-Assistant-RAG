from langchain_community.document_loaders import TextLoader
doc=TextLoader("doc.txt").load()


from langchain_text_splitters import RecursiveCharacterTextSplitter   

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks=splitter.split_documents(doc)
text=[chunk.page_content for chunk in chunks]
metadata=[chunk.metadata for chunk in chunks]

from sentence_transformers import SentenceTransformer
model=SentenceTransformer("All-miniLM-L6-v2")
vectors=model.encode(text)

import chromadb


client = chromadb.PersistentClient(path="../VectorStore")
collection=client.get_or_create_collection('hospitalvectors')

collection.add(
    ids=[str(i) for i in range(len(text))],
    documents=text,
    embeddings=vectors.tolist(),
    metadatas=metadata
)
