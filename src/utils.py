# src/utils.py
import pandas as pd

def safe_preview(df: pd.DataFrame, max_rows=1000):
    if len(df) > max_rows:
        return df.sample(max_rows)
    return df
