import matplotlib.pyplot as plt
import seaborn as sns


class ChartAgent:

    def generate_chart(self, df, question):

        question = question.lower()

        numeric_cols = df.select_dtypes(include=["int64","float64"]).columns.tolist()
        categorical_cols = df.select_dtypes(include=["object","category","bool"]).columns.tolist()

        if len(categorical_cols) == 0 or len(numeric_cols) == 0:
            return None

        # smaller chart size
        plt.figure(figsize=(4,3))

        # Example logic
        if "distribution" in question or "histogram" in question:

            col = numeric_cols[0]

            sns.histplot(df[col].dropna(), bins=30)

            plt.title(f"{col} Distribution")

            return plt.gcf()


        elif "vs" in question or "relationship" in question:

            if len(numeric_cols) >= 2:

                x = numeric_cols[0]
                y = numeric_cols[1]

                sns.scatterplot(x=df[x], y=df[y])

                plt.title(f"{x} vs {y}")

                return plt.gcf()


        elif "category" in question or "count" in question:

            col = categorical_cols[0]

            sns.countplot(x=df[col])

            plt.title(f"{col} Count")

            return plt.gcf()


        return None