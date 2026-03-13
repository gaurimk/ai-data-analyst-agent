from rag.vector_store import load_vector_store


def search_documents(query):

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    return context