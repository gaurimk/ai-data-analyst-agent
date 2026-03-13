import pandas as pd

from agents.data_agent import DataAgent
from agents.viz_agent import VisualizationAgent
from agents.insight_agent import InsightAgent

from tools.tableau_export_tool import export_dataset_for_tableau


class OrchestratorAgent:

    def __init__(self, dataset_path):

        self.df = pd.read_csv(dataset_path)

        self.data_agent = DataAgent(self.df)
        self.viz_agent = VisualizationAgent(self.df)
        self.insight_agent = InsightAgent()


    def run_pipeline(self):

        print("Running Data Analysis...")

        analysis = self.data_agent.run_analysis()


        print("Generating Visualization...")

        chart = self.viz_agent.create_bar_chart("product")


        print("Generating Insights...")

        insights = self.insight_agent.generate_insights(analysis)


        print("Exporting dataset for Tableau...")

        tableau_path = export_dataset_for_tableau(self.df)


        return {
            "analysis": analysis,
            "chart": chart,
            "insights": insights,
            "tableau_dataset": tableau_path
        }