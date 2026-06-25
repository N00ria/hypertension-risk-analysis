
import pandas as pd

# --- Column types and non-null counts ---
print("=== Column Info ===")
_info_rows = []
for col in hypertension_df.columns:
    dtype = hypertension_df[col].dtype
    n_missing = hypertension_df[col].isna().sum()
    pct_missing = n_missing / len(hypertension_df) * 100
    _info_rows.append({"Column": col, "Dtype": str(dtype), "Non-Null": len(hypertension_df) - n_missing, "Missing": n_missing, "Missing %": round(pct_missing, 1)})

column_summary = pd.DataFrame(_info_rows)
print(column_summary.to_string(index=False))

# --- Numeric summary ---
print("\n=== Numeric Column Statistics ===")
print(hypertension_df.describe().round(2).to_string())

# --- Categorical value counts ---
print("\n=== Categorical Columns — Unique Values ===")
_cat_cols = hypertension_df.select_dtypes(include="object").columns
for col in _cat_cols:
    print(f"\n{col}:")
    print(hypertension_df[col].value_counts(dropna=False).to_string())
