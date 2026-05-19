import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Agentic AI Data Science Assistant",
    layout="wide"
)

# Sidebar
st.sidebar.header("Dashboard Controls")
st.sidebar.write("Upload a CSV file to begin analysis.")

# Main Title
st.title("Agentic AI Data Science Assistant")

st.subheader("Interactive Data Visualization Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload Your CSV File", type=["csv"])

if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv(uploaded_file)

    # Dataset Overview
    st.subheader("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # Preview Dataset
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Show Columns
    st.subheader("Columns in Dataset")
    st.write(df.columns.tolist())

    # Missing Values
    st.subheader("Missing Values Analysis")

    missing_values = df.isnull().sum()

    st.dataframe(
        missing_values[missing_values > 0]
        .reset_index()
        .rename(columns={
            "index": "Column",
            0: "Missing Values"
        })
    )

    # Numeric Columns
    numeric_columns = df.select_dtypes(include=['number']).columns

    if len(numeric_columns) > 0:

        st.subheader("Interactive Visualization")

        # Column Selection
        selected_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        # Chart Type Selection
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Histogram", "Box Plot"]
        )

        # Histogram
        if chart_type == "Histogram":

            fig = px.histogram(
                df,
                x=selected_column,
                title=f"Distribution of {selected_column}"
            )

            st.plotly_chart(fig, use_container_width=True)

        # Box Plot
        elif chart_type == "Box Plot":

            fig = px.box(
                df,
                y=selected_column,
                title=f"Box Plot of {selected_column}"
            )

            st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("No numeric columns found in dataset.")