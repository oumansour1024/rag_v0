import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def create_vector_store(chunks):
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    faiss.write_index(index, "faiss_index.index")

    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    return index, chunks


def load_vector_store():
    index = faiss.read_index("faiss_index.index")

    with open("chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def search(query, index, chunks, k):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, k)
    return [chunks[i] for i in indices[0]]