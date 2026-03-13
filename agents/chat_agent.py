from langchain_community.llms import Ollama
import matplotlib.pyplot as plt
import seaborn as sns
import os

OUTPUT_DIR = "data/processed"


class ChatAgent:

    def __init__(self):

        self.llm = Ollama(model="llama3")


    def detect_chart_request(self, question):

        question = question.lower()

        if "relationship" in question or "vs" in question:
            return "scatter"

        if "distribution" in question:
            return "histogram"

        return None


    def generate_chart(self, df, question):

        question = question.lower()

        columns = df.columns.tolist()

        for col1 in columns:
            for col2 in columns:

                if col1.lower() in question and col2.lower() in question:

                    plt.figure()

                    sns.scatterplot(x=df[col1], y=df[col2])

                    path = f"{OUTPUT_DIR}/{col1}_vs_{col2}_chat.png"

                    plt.title(f"{col1} vs {col2}")

                    plt.savefig(path)

                    plt.close()

                    return path

        return None


    def answer_question(self, df, question):

        chart_type = self.detect_chart_request(question)

        if chart_type:

            chart = self.generate_chart(df, question)

            if chart:
                return {"type": "chart", "path": chart}

        schema = ", ".join(df.columns)

        prompt = f"""
You are an AI Data Analyst.

Dataset columns:
{schema}

User question:
{question}

Provide a clear explanation based on the dataset.
"""

        response = self.llm.invoke(prompt)

        return {"type": "text", "content": response}