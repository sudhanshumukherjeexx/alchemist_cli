import streamlit as st
import polars as pl
import pandas as pd

# Load DataFrame
df = st.session_state.get('df')
if df is None:
    st.warning("Please upload a dataset to get started.")

# Function to select data types and convert to Pandas DataFrame
def select_data_types(df):
    dtype_select_df = df.select([
        pl.col(pl.Decimal),
        pl.col(pl.Float32),
        pl.col(pl.Float64),
        pl.col(pl.Int16),
        pl.col(pl.Int32),
        pl.col(pl.Int64),
        pl.col(pl.Int8),
        pl.col(pl.UInt16),
        pl.col(pl.UInt32),
        pl.col(pl.UInt64),
        pl.col(pl.UInt8),
        pl.col(pl.Date),
        pl.col(pl.Datetime),
        pl.col(pl.Duration),
        pl.col(pl.Time)
    ])
    return dtype_select_df.to_pandas()

# Dropdown for selecting imputation method
imputation_method = st.selectbox("Select Imputation Method", ["Drop Missing Values", "Replace Missing Values with Specific Value"])

if imputation_method == "Replace Missing Values with Specific Value":
    placeholder_value = st.text_input("Enter the value to replace missing values with", key="placeholder")
    placeholder_value = int(placeholder_value) if placeholder_value else None  # Handle empty input

# Button to trigger imputation
if st.button("Impute"):
    if imputation_method == "Drop Missing Values":
        df = df.drop_nulls()
        st.success("Missing values dropped successfully.")
    elif imputation_method == "Replace Missing Values with Specific Value":
        if placeholder_value is not None:
            df = df.fill_null(placeholder_value)
            st.success(f"Missing values replaced with {placeholder_value} successfully.")
        else:
            st.error("Please enter a specific value for imputation.")

# Download button to save the processed data as a new session state
if st.button("Download Processed Data"):
    if df is not None:
        st.session_state.df_processed = df
        st.success("Processed data has been saved as a new session state. You can download it now.")

# Example: Display the processed data
if "df_processed" in st.session_state:
    st.write("Processed Data:")
    st.write(st.session_state.df_processed.head())

# Download button for CSV
if "df_processed" in st.session_state:
    csv_data = st.session_state.df_processed.write_csv()
    st.download_button(
        label="Download CSV",
        data=csv_data,
        key="download_csv",
        file_name="processed_data.csv",
    )
