import pandas as pd

# Fill missing Medication values with 'No Medication'
hypertension_clean_df = hypertension_df.copy()
hypertension_clean_df['Medication'] = hypertension_clean_df['Medication'].fillna('No Medication')

# Verify
print("=== Medication Value Counts After Cleaning ===")
print(hypertension_clean_df['Medication'].value_counts())
print(f"\nMissing values remaining: {hypertension_clean_df['Medication'].isna().sum()}")
