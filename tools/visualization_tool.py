import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import numpy as np

OUTPUT_DIR = "data/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_style("darkgrid")


def clean_dataset(df):

    # remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # drop duplicates
    df = df.drop_duplicates()

    return df


def generate_visualizations(df):

    df = clean_dataset(df)

    results = []

    # detect column types
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    datetime_cols = df.select_dtypes(include=["datetime64"]).columns.tolist()

    # remove id columns
    numeric_cols = [c for c in numeric_cols if "id" not in c.lower()]

    # limit for performance
    numeric_cols = numeric_cols[:6]
    categorical_cols = categorical_cols[:4]

    # -------------------------
    # 1 HISTOGRAMS
    # -------------------------

    for col in numeric_cols:

        plt.figure(figsize=(8,5))

        sns.histplot(df[col].dropna(), bins=30, kde=True)

        title = f"{col} Distribution"
        path = f"{OUTPUT_DIR}/{col}_histogram.png"

        plt.title(title)
        plt.xlabel(col)
        plt.ylabel("Frequency")

        plt.tight_layout()
        plt.savefig(path)
        plt.close()

        results.append({
            "path": path,
            "title": title,
            "x": col,
            "y": "Frequency",
            "explanation": f"Distribution of {col}. Peaks represent common value ranges."
        })


    # -------------------------
    # 2 BAR CHARTS
    # -------------------------

    for col in categorical_cols:

        if df[col].nunique() < 30:

            plt.figure(figsize=(8,5))

            df[col].value_counts().head(15).plot(kind="bar")

            title = f"{col} Category Distribution"
            path = f"{OUTPUT_DIR}/{col}_bar_chart.png"

            plt.title(title)
            plt.xlabel(col)
            plt.ylabel("Count")

            plt.tight_layout()
            plt.savefig(path)
            plt.close()

            results.append({
                "path": path,
                "title": title,
                "x": col,
                "y": "Count",
                "explanation": f"Shows frequency of {col} categories."
            })


    # -------------------------
    # 3 PIE CHARTS
    # -------------------------

    for col in categorical_cols[:2]:

        if df[col].nunique() < 10:

            plt.figure(figsize=(6,6))

            df[col].value_counts().plot.pie(autopct="%1.1f%%")

            title = f"{col} Proportion"
            path = f"{OUTPUT_DIR}/{col}_pie_chart.png"

            plt.title(title)
            plt.ylabel("")

            plt.tight_layout()
            plt.savefig(path)
            plt.close()

            results.append({
                "path": path,
                "title": title,
                "x": col,
                "y": "Percentage",
                "explanation": f"Proportion of each {col} category."
            })


    # -------------------------
    # 4 BOX PLOTS
    # -------------------------

    if categorical_cols and numeric_cols:

        for num in numeric_cols[:2]:

            for cat in categorical_cols[:2]:

                if df[cat].nunique() < 15:

                    plt.figure(figsize=(8,5))

                    sns.boxplot(x=df[cat], y=df[num])

                    title = f"{num} vs {cat}"
                    path = f"{OUTPUT_DIR}/{num}_vs_{cat}_boxplot.png"

                    plt.title(title)

                    plt.tight_layout()
                    plt.savefig(path)
                    plt.close()

                    results.append({
                        "path": path,
                        "title": title,
                        "x": cat,
                        "y": num,
                        "explanation": f"Shows distribution of {num} across {cat} categories."
                    })


    # -------------------------
    # 5 VIOLIN PLOTS
    # -------------------------

    if categorical_cols and numeric_cols:

        for num in numeric_cols[:1]:

            for cat in categorical_cols[:1]:

                if df[cat].nunique() < 10:

                    plt.figure(figsize=(8,5))

                    sns.violinplot(x=df[cat], y=df[num])

                    title = f"{num} vs {cat} (Violin)"

                    path = f"{OUTPUT_DIR}/{num}_vs_{cat}_violin.png"

                    plt.title(title)

                    plt.tight_layout()
                    plt.savefig(path)
                    plt.close()

                    results.append({
                        "path": path,
                        "title": title,
                        "x": cat,
                        "y": num,
                        "explanation": f"Shows distribution shape of {num} across {cat} categories."
                    })


    # -------------------------
    # 6 SCATTER RELATIONSHIPS
    # -------------------------

    if len(numeric_cols) >= 2:

        corr = df[numeric_cols].corr().abs()

        pairs = corr.unstack().sort_values(ascending=False).drop_duplicates()

        selected_pairs = []

        for (a,b), val in pairs.items():

            if a != b and val < 1:

                selected_pairs.append((a,b,val))

            if len(selected_pairs) >= 4:
                break


        for x,y,val in selected_pairs:

            plt.figure(figsize=(7,5))

            sns.scatterplot(x=df[x], y=df[y])

            title = f"{x} vs {y}"

            path = f"{OUTPUT_DIR}/{x}_vs_{y}_scatter.png"

            plt.title(title)

            plt.tight_layout()
            plt.savefig(path)
            plt.close()

            results.append({
                "path": path,
                "title": title,
                "x": x,
                "y": y,
                "explanation": f"Relationship between {x} and {y}. Correlation ≈ {round(val,2)}."
            })


    # -------------------------
    # 7 CORRELATION HEATMAP
    # -------------------------

    if len(numeric_cols) > 2:

        plt.figure(figsize=(10,7))

        sns.heatmap(
            df[numeric_cols].corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        title = "Correlation Heatmap"

        path = f"{OUTPUT_DIR}/correlation_heatmap.png"

        plt.title(title)

        plt.tight_layout()
        plt.savefig(path)
        plt.close()

        results.append({
            "path": path,
            "title": title,
            "x": "Features",
            "y": "Features",
            "explanation": "Shows correlation between numeric variables."
        })


    # -------------------------
    # 8 PAIRPLOT
    # -------------------------

    if len(numeric_cols) >= 3:

        sample_df = df[numeric_cols].dropna()

        if len(sample_df) > 500:
            sample_df = sample_df.sample(500)

        pairplot = sns.pairplot(sample_df)

        path = f"{OUTPUT_DIR}/pairplot.png"

        pairplot.savefig(path)

        results.append({
            "path": path,
            "title": "Pairplot Relationships",
            "x": "Multiple",
            "y": "Multiple",
            "explanation": "Shows relationships between multiple numeric variables."
        })


    # -------------------------
    # 9 TIME SERIES CHARTS
    # -------------------------

    if datetime_cols and numeric_cols:

        time_col = datetime_cols[0]
        num_col = numeric_cols[0]

        df_sorted = df.sort_values(time_col)

        plt.figure(figsize=(10,5))

        sns.lineplot(x=df_sorted[time_col], y=df_sorted[num_col])

        title = f"{num_col} Over Time"

        path = f"{OUTPUT_DIR}/time_series.png"

        plt.title(title)

        plt.tight_layout()
        plt.savefig(path)
        plt.close()

        results.append({
            "path": path,
            "title": title,
            "x": time_col,
            "y": num_col,
            "explanation": "Trend of numeric value over time."
        })


    return results