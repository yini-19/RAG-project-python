# test_dummy_data.py
import random
from sqlalchemy.orm import Session
from db import engine
from models import Document, Chunk

# Generate a random 1536-dimensional vector (fake embedding)
def random_vector(dim=1536):
    return [random.uniform(-1, 1) for _ in range(dim)]

with Session(engine) as session:
    # 1. Insert a dummy document
    dummy_doc = Document(filename="dummy_test.txt")
    session.add(dummy_doc)
    session.commit()  # commit so dummy_doc.id gets populated
    print(f"Inserted dummy document with id: {dummy_doc.id}")

    # 2. Insert a dummy chunk linked to that document
    dummy_vector = random_vector()
    dummy_chunk = Chunk(
        document_id=dummy_doc.id,
        chunk_index=0,
        text="This is a dummy chunk for testing.",
        embedding=dummy_vector
    )
    session.add(dummy_chunk)
    session.commit()
    print(f"Inserted dummy chunk with id: {dummy_chunk.id}")

    # 3. Run a similarity search — compare the dummy vector against itself
    results = session.query(Chunk).order_by(
        Chunk.embedding.l2_distance(dummy_vector)
    ).limit(1).all()

    print("Closest chunk found:", results[0].text, "| distance should be ~0")

    # 4. Clean up — delete the dummy rows so tables start empty for Day 5
    session.delete(dummy_chunk)
    session.delete(dummy_doc)
    session.commit()
    print("Dummy rows deleted. Tables are clean.")