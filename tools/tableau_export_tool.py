import os
import pandas as pd

OUTPUT_DIR = "data/processed"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def export_dataset_for_tableau(df):

    file_path = os.path.join(OUTPUT_DIR, "tableau_dataset.csv")

    df.to_csv(file_path, index=False)

    return file_path