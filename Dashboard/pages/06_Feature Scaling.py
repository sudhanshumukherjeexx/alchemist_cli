import streamlit as st
import polars as pl
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler 

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
    st.image("images/brain.gif")
with col2:
    st.markdown('## Feature Scaling Techniques for your Data')
    st.markdown("Discover the fundamental methods in feature scaling, such as Min-Max Scaling, Standardization, Robust Scaler, and more, essential for preparing data before applying machine learning algorithms.")

# Load df
df = st.session_state.get('df')
df_processed = st.session_state.get('df_processed')

# Min-Max Scaling
def min_max_scaling(dataframe):
   dataframe = select_data_types(dataframe)
   for column in dataframe.columns:
       min_max_scaler = MinMaxScaler()
       dataframe[[column]] = min_max_scaler.fit_transform(dataframe[[column]])
   return dataframe

# Standard Scaling (Z-Normalization)
def standard_scaling(dataframe):
   dataframe = select_data_types(dataframe) 
   for column in dataframe.columns:
       standard_scaler = StandardScaler()
       dataframe[[column]] = standard_scaler.fit_transform(dataframe[[column]])
   return dataframe

# Robust Scaling
def robust_scaling(dataframe):
    dataframe = select_data_types(dataframe) 
    for column in dataframe.columns:
        robust_scaler = RobustScaler()
        dataframe[[column]] = robust_scaler.fit_transform(dataframe[[column]])
    return dataframe

if df is None:
    st.warning("Please upload a dataset to get started.")
else:
    st.divider()
    st.markdown('🖲️Select the **Session State** and **Feature Scaling Technique** ⤵️')
    col3, col4 = st.columns(2)
    with col3:
        # Create a dropdown menu to choose the session state
        selected_session_state = st.selectbox("Select Session State", ["Intial DataFrame", "DataFrame after Missing value Imputation"])
        st.divider()
    with col4:
        # Create a dropdown menu to choose the Feature Scaling Technique
        feature_scaling_technique = st.selectbox("Select Feature Scaling Technique", ["Min-Max Scaling (Normalization)", "Standardization (Z-score Normalization)", "Robust Scaler"])
        st.divider()
    
    # Handle the case when "Session State 2" is None
    if selected_session_state == "Intial DataFrame":
        df = df
        #st.session_state.active_session = st.session_state.session_state_1
    else:
        df = df_processed
        if df is None:
            st.warning("This session state is available only after missing value imputation. Please impute the missing values.")
        else:
            df = df_processed

    if st.button("Scale Features", use_container_width=True):
        if feature_scaling_technique == "Min-Max Scaling (Normalization)":
            df_scaled = min_max_scaling(df)
            st.dataframe(df_scaled)
            st.success("Min-Max Scaling performed successfully.")
            st.session_state.df_scaled = df_scaled
        elif feature_scaling_technique == "Standardization (Z-score Normalization)":
            df_scaled = standard_scaling(df)
            st.dataframe(df_scaled)
            st.success("Missing values dropped successfully.")
            st.session_state.df_scaled = df_scaled
        elif feature_scaling_technique == "Robust Scaler":
            df_scaled = robust_scaling(df)
            st.dataframe(df_scaled)
            st.success("Missing values dropped successfully.")
            st.session_state.df_scaled = df_scaled

st.divider()
col5, col6, col7 = st.columns(3)
# Download button to save the processed data as a new session state
with col6:
    if "df_scaled" in st.session_state:
        csv_data = st.session_state.df_scaled.to_csv()
        st.download_button(
            label="Download Scaled Data",
            data=csv_data,
            key="download_csv",
            file_name="scaled_data.csv",
            use_container_width=True,
    )
    else:
        if st.button('Download Scaled Data',use_container_width=True):
            st.write('Recommended: Perform Scaling first!')
    #with col6:
        st.write("")
with col5:
    st.write("")
with col7:
    st.write("")


