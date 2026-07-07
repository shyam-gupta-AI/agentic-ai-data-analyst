import streamlit as st
import plotly.express as px


# ==========================================================
# Day 7 - Interactive Visualization Dashboard
# Feature: Histogram & Box Plot
# Purpose: Display interactive visualizations for numeric columns
# ==========================================================

def show_visualizations(df):

    # ------------------------------------------------------
    # Step 1 - Identify Numeric Columns
    # ------------------------------------------------------
    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns

    # ------------------------------------------------------
    # Step 2 - Check Numeric Columns Availability
    # ------------------------------------------------------
    if len(numeric_columns) > 0:

        st.subheader("Interactive Visualization")

        # --------------------------------------------------
        # Step 3 - Select Numeric Column
        # --------------------------------------------------
        selected_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        # --------------------------------------------------
        # Step 4 - Select Visualization Type
        # --------------------------------------------------
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Histogram", "Box Plot"]
        )

        # --------------------------------------------------
        # Step 5 - Generate Histogram
        # --------------------------------------------------
        if chart_type == "Histogram":

            fig = px.histogram(
                df,
                x=selected_column,
                title=f"Distribution of {selected_column}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # --------------------------------------------------
        # Step 6 - Generate Box Plot
        # --------------------------------------------------
        elif chart_type == "Box Plot":

            fig = px.box(
                df,
                y=selected_column,
                title=f"Box Plot of {selected_column}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # ------------------------------------------------------
    # Step 7 - Handle Non-Numeric Dataset
    # ------------------------------------------------------
    else:

        st.warning(
            "No numeric columns found in dataset."
        )