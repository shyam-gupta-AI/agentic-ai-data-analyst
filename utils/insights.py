# Day 5 Enhancement - AI Dataset Insights Generator

def generate_basic_insights(df):

    insights = []

    insights.append(
        f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns."
    )

    numeric_cols = df.select_dtypes(
        include=['int64', 'float64']
    ).columns

    insights.append(
        f"Dataset has {len(numeric_cols)} numeric columns."
    )

    missing = df.isnull().sum().sum()

    insights.append(
        f"Dataset contains {missing} missing values after cleaning."
    )

    return insights