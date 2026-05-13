from app.rag.vector_store import db

def retrieve_documents(query):

    docs = db.similarity_search(query, k=3)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    return context