import os
import json

def split_to_chunks(full_text: str, chunk_size: int=300, overlap: int=100) -> list[str]:
        
        words = full_text.split()
        chunks = []
        start = 0

        while start < len(words):
            end = start + chunk_size
            chunk = " ".join(words[start:end])
            chunks.append(chunk)
            start += chunk_size - overlap
        return chunks

def chunk_all_documents(processed_dir, str = "data/processed"):
    all_chunks = []
    for filename in os.listdir(processed_dir):
        filepath = os.path.join(processed_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
             text = f.read()

        chunks = split_to_chunks(text)
        for i, chunk in enumerate(chunks):
             all_chunks.append({
                  "source": filename,
                  "chunk_index": i,
                  "text": chunk
             })
    
    return all_chunks
    
if __name__ == "__main__":
     chunks = chunk_all_documents("data/processed")
     with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)   
     print(f"Saved {len(chunks)} chunks to data/chunks.json")

