from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader


def load_text_document(path):

    loader = TextLoader(path)

    documents = loader.load()

    return documents


def load_pdf_document(path):

    loader = PyPDFLoader(path)

    documents = loader.load()

    return documents