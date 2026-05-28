import pandas as pd


def clean_data(df):

    cleaning_log = []

    # Remove duplicates
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        df = df.drop_duplicates()
        cleaning_log.append(f"Removed {duplicate_count} duplicate rows")

    # Handle missing values
    missing_values = df.isnull().sum().sum()

    if missing_values > 0:

        for column in df.columns:

            if df[column].dtype in ['int64', 'float64']:
                df[column] = df[column].fillna(df[column].median())

            else:
                df[column] = df[column].fillna("Unknown")

        cleaning_log.append(f"Handled {missing_values} missing values")

    return df, cleaning_log