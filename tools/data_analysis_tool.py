import pandas as pd


class DataAnalysisTool:

    def __init__(self, df: pd.DataFrame):
        self.df = df


    def dataset_overview(self):

        return {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1],
            "column_names": list(self.df.columns)
        }


    def missing_values(self):

        return self.df.isnull().sum().to_dict()


    def numeric_summary(self):

        numeric_cols = self.df.select_dtypes(include=["int64", "float64"])

        if numeric_cols.empty:
            return {}

        return numeric_cols.describe().to_dict()


    def top_categories(self):

        categorical_cols = self.df.select_dtypes(include=["object"])

        results = {}

        for col in categorical_cols.columns:
            results[col] = self.df[col].value_counts().head(5).to_dict()

        return results


    def correlation_matrix(self):

        numeric_cols = self.df.select_dtypes(include=["int64", "float64"])

        if numeric_cols.shape[1] < 2:
            return {}

        return numeric_cols.corr().to_dict()


    def run_full_analysis(self):

        results = {
            "overview": self.dataset_overview(),
            "missing_values": self.missing_values(),
            "numeric_summary": self.numeric_summary(),
            "top_categories": self.top_categories(),
            "correlations": self.correlation_matrix()
        }

        return results