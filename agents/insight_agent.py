from models.ollama_client import ask_llm


class InsightAgent:

    def generate_insights(self, analysis_results):

        prompt = f"""
        You are a data analyst.

        Based on the following dataset analysis results,
        generate clear business insights.

        Analysis Results:
        {analysis_results}

        Provide 3-5 short insights.
        """

        insights = ask_llm(prompt)

        return insights