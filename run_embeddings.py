import json
from embedder import embed_batch

def load_chunks(path: str="data/chunks.json") -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def batch_list(items: list, batch_size: int=5):
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

chunks = load_chunks()
print(f"loaded {load_chunks} chunks")

for batch in batch_list(chunks, batch_size=50):
    texts = [chunk["text"] for chunk in batch]
    vectors = embed_batch(texts)

    for chunk, vector in zip(batch, vectors):
        chunk["embedding"] = vector

    print(f"Embedded batch of {len(batch)} chunks")


from sqlalchemy.orm import Session
from db import engine
from models import Document, Chunk

def insert_chunks(chunks: list[dict]):
    with Session(engine) as session:
        # group chunks by their source document filename
        doc_cache = {}  # filename -> Document.id, avoids inserting the same document twice

        for chunk in chunks:
            filename = chunk["source"]

            if filename not in doc_cache:
                doc = Document(filename=filename)
                session.add(doc)
                session.commit()  # commit so doc.id is populated
                doc_cache[filename] = doc.id

            new_chunk = Chunk(
                document_id=doc_cache[filename],
                chunk_index=chunk["chunk_index"],
                text=chunk["text"],
                embedding=chunk["embedding"]
            )
            session.add(new_chunk)

        session.commit()
        print(f"Inserted {len(chunks)} chunks into the database")

insert_chunks(chunks)