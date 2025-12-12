import streamlit as st
import pandas as pd
import duckdb
import altair as alt

st.set_page_config(page_title="Ask Your Data – Virtual Data Analyst", layout="wide")

st.title("Ask Your Data — Virtual Data Analyst")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if st.button("Load sample data"):
    uploaded_file = "data/sample/ecommerce_sample.csv"

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Auto-Generated SQL (DuckDB)")
    query = "SELECT * FROM df LIMIT 5"
    st.code(query)

    result = duckdb.query("SELECT * FROM df LIMIT 5").to_df()
    st.dataframe(result)

    st.subheader("Distribution Plot")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) > 0:
        col_to_plot = st.selectbox("Choose column to visualize", numeric_cols)
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(col_to_plot, bin=True),
            y='count()',
            tooltip=[col_to_plot]
        )
        st.altair_chart(chart, use_container_width=True)
