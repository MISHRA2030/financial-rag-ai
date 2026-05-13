from datasets import load_dataset

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings


# =====================================
# LOAD HUGGINGFACE DATASET
# =====================================

dataset = load_dataset(
    "virattt/financial-qa-10K",
    split="train"
)

print("✅ Dataset Loaded")


# =====================================
# CONVERT DATA TO DOCUMENTS
# =====================================

documents = []

# Use only first 500 rows
for item in dataset.select(range(500)):

    text = f"""
    Question: {item['question']}

    Answer: {item['answer']}
    """

    documents.append(
        Document(page_content=text)
    )

print("✅ Documents Created")


# =====================================
# SPLIT DOCUMENTS
# =====================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=30
)

docs = text_splitter.split_documents(documents)

print("✅ Documents Split")


# =====================================
# LOAD HUGGINGFACE EMBEDDINGS
# =====================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
)

print("✅ Embeddings Loaded")


# =====================================
# CREATE FAISS DATABASE
# =====================================

db = FAISS.from_documents(
    docs,
    embeddings
)

print("✅ FAISS Database Created")


# =====================================
# SAVE FAISS INDEX
# =====================================

db.save_local("faiss_index")

print("✅ FAISS Index Saved Successfully!")