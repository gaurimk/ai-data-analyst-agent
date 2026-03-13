from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings


def create_vector_store(documents):

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="rag/vector_db"
    )

    return vector_store


def load_vector_store():

    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory="rag/vector_db",
        embedding_function=embeddings
    )

    return vector_store