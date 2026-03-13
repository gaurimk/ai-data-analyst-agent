from models.ollama_client import ask_llm
from tools.rag_search_tool import search_documents


class RAGAgent:

    def answer_question(self, question):

        context = search_documents(question)

        prompt = f"""
        Use the following context to answer the question.

        Context:
        {context}

        Question:
        {question}
        """

        answer = ask_llm(prompt)

        return answer