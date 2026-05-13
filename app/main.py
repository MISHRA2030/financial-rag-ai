from fastapi import FastAPI

from transformers import pipeline

from app.rag.query_engine import retrieve_documents


# =========================================
# LOAD HUGGINGFACE MODEL
# =========================================

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)


# =========================================
# CREATE FASTAPI APP
# =========================================

app = FastAPI()


# =========================================
# HOME ROUTE
# =========================================

@app.get("/")
def home():

    return {
        "message": "Financial RAG AI Running"
    }


# =========================================
# ASK ROUTE
# =========================================

@app.get("/ask")
def ask(query: str):

    try:

        # Retrieve relevant context
        context = retrieve_documents(query)

        # Better prompt
        prompt = f"""
        Context:
        {context}

        Question:
        {query}

        Answer in a short and clear sentence.
        """

        # Generate response
        response = generator(
            prompt,
            max_new_tokens=50,
            do_sample=False
        )

        return {
            "query": query,
            "answer": response[0]["generated_text"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }