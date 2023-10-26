import streamlit as st
import polars as pl
import pandas as pd
import numpy as np

# Function to select data types and convert to Pandas df
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


col1, col2 = st.columns(2)
with col1:
    st.image("images/missing_h.gif")
with col2:
    st.markdown('## Impute Missing values in your Data')
    st.markdown("Restore data integrity effortlessly with `eight` missing value imputation methods. Keep your dataset complete and analysis-ready.")
#st.image("images/page_1.gif",use_column_width=True)
# Load df
df = st.session_state.get('df')
if df is None:
    st.warning("Please upload a dataset to get started.")

st.divider()


# Dropdown for selecting imputation method
imputation_method = st.selectbox("Select Imputation Method", ["1. Drop Missing Values", "2. Replace Missing Values with Specific Value", "3. Impute Missing Data with Fill Forward Strategy", "4. Impute Missing Data with Backward Fill Strategy", "5. Impute Missing Data based on Distribution of Feature", "6. Impute Missing Data with Mean", "7. Impute Missing Data with Median", "8. Impute Missing Data with Nearest Neighbours"])

if imputation_method == "2. Replace Missing Values with Specific Value":
    placeholder_value = st.text_input("Enter the value to replace missing values with", key="placeholder")
    placeholder_value = int(placeholder_value) if placeholder_value else None  # Handle empty input


# Button to trigger imputation
if st.button("Impute", use_container_width=True):
    if imputation_method == "1. Drop Missing Values":
        df = df.drop_nulls()
        st.success("Missing values dropped successfully.")
        st.session_state.df_processed = df
    elif imputation_method == "2. Replace Missing Values with Specific Value":
        if placeholder_value is not None:
            df = df.fill_null(placeholder_value)
            st.success(f"Missing values replaced with {placeholder_value} successfully.")
            st.session_state.df_processed = df
        else:
            st.error("Please enter a specific value for imputation.")
    elif imputation_method == "3. Impute Missing Data with Fill Forward Strategy":
        df = df.select(pl.all().forward_fill())
        st.success(f"Missing values replaced with forward fill strategy successfully.")
        st.session_state.df_processed = df
    elif imputation_method == "4. Impute Missing Data with Backward Fill Strategy":
        df = df.fill_null(strategy="backward")
        st.success(f"Missing values replaced with forward fill strategy successfully.")
        st.session_state.df_processed = df
    elif imputation_method == "5. Impute Missing Data based on Distribution of Feature":
        df = df.to_pandas()
        for column in df.columns:
                if df[column].dtype != pl.Categorical and df[column].dtype != pl.Date and df[column].dtype != pl.Datetime and df[column].dtype != pl.Duration and df[column].dtype != pl.Time and df[column].dtype != pl.Utf8 and df[column].dtype != pl.Boolean and df[column].dtype != pl.Null and df[column].dtype != pl.Object and df[column].dtype != pl.Unknown:
                    mean = df[column].mean()
                    std = df[column].std()
                    random_values = np.random.normal(loc=mean, scale=std, size=df[column].isnull().sum())
                    df[column] = df[column].fillna(pd.Series(random_values,index=df[column][df[column].isnull()].index))
        df = pl.from_pandas(df)
        st.success(f"Missing values replaced with based on distribution of the feature successfully.")
        st.session_state.df_processed = df
    elif imputation_method == "6. Impute Missing Data with Mean":
        df = df.to_pandas()
        for column in df.columns:
            if df[column].dtype != pl.Categorical and df[column].dtype != pl.Date and df[column].dtype != pl.Datetime and df[column].dtype != pl.Duration and df[column].dtype != pl.Time and df[column].dtype != pl.Utf8 and df[column].dtype != pl.Boolean and df[column].dtype != pl.Null and df[column].dtype != pl.Object and df[column].dtype != pl.Unknown:
                df[column] = df[column].fillna(df[column].mean())
        df = pl.from_pandas(df)
        st.success(f"Missing values replaced with mean successfully.")
        st.session_state.df_processed = df        
    elif imputation_method == "7. Impute Missing Data with Median":
        df = df.to_pandas()
        for column in df.columns:
            if df[column].dtype != pl.Categorical and df[column].dtype != pl.Date and df[column].dtype != pl.Datetime and df[column].dtype != pl.Duration and df[column].dtype != pl.Time and df[column].dtype != pl.Utf8 and df[column].dtype != pl.Boolean and df[column].dtype != pl.Null and df[column].dtype != pl.Object and df[column].dtype != pl.Unknown:
                df[column] = df[column].fillna(df[column].median())
        df = pl.from_pandas(df)
        st.success(f"Missing values replaced with median successfully.")
        st.session_state.df_processed = df
    elif imputation_method == "8. Impute Missing Data with Nearest Neighbours":
        df = df.to_pandas()
        for column in df.columns:
            if df[column].dtype != pl.Categorical and df[column].dtype != pl.Date and df[column].dtype != pl.Datetime and df[column].dtype != pl.Duration and df[column].dtype != pl.Time and df[column].dtype != pl.Utf8 and df[column].dtype != pl.Boolean and df[column].dtype != pl.Null and df[column].dtype != pl.Object and df[column].dtype != pl.Unknown:
                missing_inds = df[column].isnull()
                non_missing_inds = ~missing_inds
                non_missing_vals = df[column][non_missing_inds]
                closest_inds = np.abs(df[column][missing_inds].values - non_missing_vals.values.reshape(-1,1)).argmin(axis=0)
                df.loc[missing_inds, column] = non_missing_vals.iloc[closest_inds].values
        df = pl.from_pandas(df)
        st.success(f"Missing values replaced with median successfully.")
        st.session_state.df_processed = df

st.divider()

col1, col2 = st.columns(2)
# Download button to save the processed data as a new session state
with col1:
    col4,col5,col6 = st.columns(3)
    with col5:
        st.image("images/download.png", use_column_width=True)
        if "df_processed" in st.session_state:
            csv_data = st.session_state.df_processed.write_csv()
            st.download_button(
                label="Download Processed Data",
                data=csv_data,
                key="download_csv",
                file_name="processed_data.csv",
                use_container_width=True,
        )
        else:
            if st.button('Download Processed Data',use_container_width=True):
                st.write('Recommended: Impute values first!')
    with col6:
        st.write("")
    with col4:
        st.image("images/table.png", use_column_width=True)
        if st.button("Display Processed Data"):
            #if df is not None:
            if "df_processed" in st.session_state:
                st.success("Processed data has been saved as a new session state. You can download it now.")
                st.write("Processed Data:")
                st.write(st.session_state.df_processed.head())
                
            else:
                st.write('Recommended: Impute values first!')
    with col6:
        st.write("")


