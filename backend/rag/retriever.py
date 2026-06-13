from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INDEX_PATH = os.path.join(
    BASE_DIR,
    "scheme_index.faiss"
)

CHUNKS_PATH = os.path.join(
    BASE_DIR,
    "chunks.pkl"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(INDEX_PATH)

with open(CHUNKS_PATH, "rb") as f:
    chunks = pickle.load(f)


def retrieve(query):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        3
    )

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return "\n".join(results)