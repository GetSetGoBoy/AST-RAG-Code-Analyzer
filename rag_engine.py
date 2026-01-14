import os
from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
DB_PATH = "./my_vector_db"

def build_knowledge_base():
    """Reads the text file and creates the database on your PC."""
    with open("security_knowledge.txt", "r") as f:
        rules = f.readlines()
    
    Chroma.from_texts(rules, embeddings, persist_directory=DB_PATH)
    print("✅ Knowledge Base Built Successfully!")

def get_advice(code_snippet):
    """Searches the database for the best security advice."""
    db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    
    docs = db.similarity_search(code_snippet, k=1)
    return docs[0].page_content if docs else "No specific advice found."