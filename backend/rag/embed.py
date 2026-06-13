from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

model = SentenceTransformer(
"all-MiniLM-L6-v2"
)

with open(
"../../data/knowledge_base.txt",
"r",
encoding="utf-8"
) as f:
    text = f.read()

chunks = text.split(
"------------------------------------------------"
)

embeddings = model.encode(chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(
np.array(embeddings)
)

faiss.write_index(
index,
"scheme_index.faiss"
)

with open(
    "chunks.pkl",
    "wb"
) as f:
    pickle.dump(chunks, f)

print("Index created successfully")
