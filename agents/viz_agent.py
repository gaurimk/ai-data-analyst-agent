from tools.visualization_tool import generate_visualizations


class VisualizationAgent:

    def run(self, df):

        charts = generate_visualizations(df)

        return charts