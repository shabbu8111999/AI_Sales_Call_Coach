from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


KNOWLEDGE_DIR = "knowledge_base"
VECTOR_DB_PATH = "vector_db"


# Loading all knowledge base files
documents = []
for file in os.listdir(KNOWLEDGE_DIR):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(KNOWLEDGE_DIR, file), encoding="utf-8")
        documents.extend(loader.load())


# Splitting the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 50
)
chunks = text_splitter.split_documents(documents)


# Creating embeddings using local HuggingFace model
embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)


# Building the FAISS vector store
vectore_store = FAISS.from_documents(chunks, embeddings)

# Saving the vector store to folder
vectore_store.save_local(VECTOR_DB_PATH)

print(f"Vector store created and saved to {VECTOR_DB_PATH}")