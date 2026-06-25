
import pandas as pd

hypertension_df = pd.read_csv("hypertension_dataset.csv")

# Preview first few rows
print("=== First 5 Rows ===")
print(hypertension_df.head().to_string())

# Shape
print(f"\n=== Dataset Shape ===")
print(f"Rows: {hypertension_df.shape[0]:,}  |  Columns: {hypertension_df.shape[1]}")
