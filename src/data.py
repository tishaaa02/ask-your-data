# src/data.py
import pandas as pd
from pathlib import Path

_SAMPLE_PATH = Path(__file__).parents[1] / 'data' / 'sample' / 'ecommerce_sample.csv'

def load_sample():
    return pd.read_csv(_SAMPLE_PATH)

def preview_df(df, n=5):
    return df.head(n)
