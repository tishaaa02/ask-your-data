# src/analysis.py
import pandas as pd
import plotly.express as px

def run_quick_eda(df: pd.DataFrame) -> dict:
    # Basic summary
    summary = {
        'num_rows': len(df),
        'num_cols': len(df.columns),
        'missing_values': df.isna().sum().to_dict(),
        'column_types': df.dtypes.apply(lambda x: str(x)).to_dict()
    }

    # Example plot: numeric distribution of first numeric column found
    numeric_cols = df.select_dtypes(include=['number']).columns
    sample_plot = None
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        fig = px.histogram(df, x=col, nbins=30, title=f'Distribution of {col}')
        sample_plot = fig

    return {'summary': summary, 'sample_plot': sample_plot}
