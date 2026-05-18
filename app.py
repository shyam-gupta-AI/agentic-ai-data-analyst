import streamlit as st
import pandas as pd

st.title("Agentic AI Data Analyst")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Dataset Statistics")
    st.write(df.describe())