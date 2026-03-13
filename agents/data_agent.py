import pandas as pd
from tools.data_analysis_tool import DataAnalysisTool


class DataAgent:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.analyzer = DataAnalysisTool(df)


    def run_analysis(self):

        results = self.analyzer.run_full_analysis()

        return results