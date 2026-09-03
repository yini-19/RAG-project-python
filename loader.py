from pypdf import PdfReader
import os

def read_pdf(filepath: str) -> str:

    try:
        # initialize the pdf reader
        reader = PdfReader(filepath)
        extracted_text = []

        # loop through and extract text from every page 
        for page in reader.pages:
            text = page.extract_text()

            if text:  # make sure text was successfully extracted from page
                extracted_text.append(text)
        
        # join all pages with a new line
        return "\n".join(extracted_text)

    except Exception as e:
        return f"An error occurred, {e}"
    
def read_text_file(filepath: str) -> str:
    with open(filepath, "r", encoding = "utf-8") as f:
        return f.read()
    
def process_all_document(raw_dir: str = "data/raw", processed_dir: str = "data/processed") -> str:
    os.makedirs(processed_dir, exist_ok=True)
    
    for filename in os.listdir(raw_dir):
        filepath = os.path.join(raw_dir, filename)
        name, ext = os.path.splitext(filename)
        
        if ext.lower() == (".pdf"):
            text = read_pdf(filepath)
    
        elif ext.lower() in [".txt", ".md"]:
            text = read_text_file(filepath)

        else:
            print(f"skipping, unsupported file type: {filename}")
            continue
        
        output_path = os.path.join(processed_dir, f"{name}.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Processed {filename} -> {output_path} ({len(text)} chars)")

if __name__ == "__main__":
    process_all_document()
