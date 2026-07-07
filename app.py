import streamlit as st
import pandas as pd


# Day 4 Enhancements - Modular Utilities
from utils.prompts import SYSTEM_PROMPT
from utils.data_loader import load_file

# Day 5 Enhancement - Data Cleaning Agent Import
from utils.data_cleaning import clean_data

# Day 5 Enhancement - AI Insights Generator Import
from utils.insights import generate_basic_insights

# Day 7 Enhancement - Visualization Module Import
from utils.charts import show_visualizations


# Page Configuration
st.set_page_config(
    page_title="Agentic AI Data Science Assistant",
    layout="wide"
)

# Sidebar
st.sidebar.header("Dashboard Controls")
st.sidebar.write("Upload a CSV file to begin analysis.")

# Day 4 Enhancement - Session Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.subheader("Interactive Data Visualization Dashboard")

# Day 4 Enhancement - Multi-format File Upload
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file is not None:

    # Day 4 Enhancement - Reusable Dataset Loading
    df = load_file(uploaded_file)

    # Day 5 Enhancement - Automated Dataset Cleaning
    cleaned_df, cleaning_log = clean_data(df)

    # Dataset Overview
    st.subheader("Dataset Overview")

    col1, col2 = st.columns(2)

    # Day 5 Enhancement - Cleaned Dataset Metrics
    with col1:
        st.metric("Rows", cleaned_df.shape[0])

    with col2:
        st.metric("Columns", cleaned_df.shape[1])

    # Day 5 Enhancement - Cleaned Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(cleaned_df.head())

    # Day 5 Enhancement - Cleaning Summary UI
    st.subheader("Cleaning Summary")

    for item in cleaning_log:
        st.success(item)

    # Day 5 Enhancement - AI Generated Dataset Insights

    st.subheader("AI Generated Insights")

    insights = generate_basic_insights(cleaned_df)

    for insight in insights:
        st.info(insight)

        

    # Day 5 Enhancement - Cleaned Dataset Columns
    st.subheader("Columns in Dataset")
    st.write(cleaned_df.columns.tolist())

    # Missing Values
    st.subheader("Missing Values Analysis")

    # Day 5 Enhancement - Post-cleaning Missing Value Analysis
    missing_values = cleaned_df.isnull().sum()

    st.dataframe(
        missing_values[missing_values > 0]
        .reset_index()
        .rename(columns={
            "index": "Column",
            0: "Missing Values"
        })
    )

    # ==========================================================
    # Day 7 Enhancement - Interactive Visualization Dashboard
    # ==========================================================

    show_visualizations(cleaned_df)


    # Day 5 Enhancement - Download Cleaned Dataset

    csv = cleaned_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download Cleaned Dataset",
        data=csv,
        file_name='cleaned_data.csv',
        mime='text/csv',
    )    