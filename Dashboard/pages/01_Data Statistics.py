import streamlit as st
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

col1, col2 = st.columns(2)
with col1:
    st.image("images/page_1.gif")
with col2:
    st.markdown('## Dataset Overview')
    st.markdown("Get a quick grasp of your dataset's key characteristics: features, data types, shape, missing values count, and feature correlations.")
#st.image("images/page_1.gif",use_column_width=True)
st.divider()

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown('`Data Header`')
    st.markdown("A glimpse of your dataset's initial rows, revealing key information and a snapshot of your data.")
with col2:
    st.markdown('`Features Available`')
    st.markdown("A list of the dataset's variables, providing insights into the data's dimensions and content.")
with col3:
    st.markdown('`Features Datatypes`')
    st.markdown("An overview of the data types associated with each feature, essential for data interpretation and manipulation.")
with col4:
    st.markdown('`Shape of Data`')
    st.markdown("A concise summary of the dataset's dimensions, highlighting the number of rows and columns.")
with col5:
    st.markdown('`Missing value count`')
    st.markdown("A tally of the number of missing or undefined values in the dataset, crucial for data quality assessment.")
with col6:
    st.markdown('`Feature Correlation`')
    st.markdown("Insights into the relationships and associations among different variables in the dataset.")
st.divider()    



# Load DataFrame
df = st.session_state.get('df')
if df is None:
    st.warning("Please upload a dataset to get started.")
else:
    #DataFrame Overview
    st.markdown('### Observe DataFrame')
    st.dataframe(df)
    st.divider()

    # page Title
    st.markdown('### Data Statistics')
    st.dataframe(df.describe())
    st.divider()

    # features Stats
    st.markdown('### Features Available')
    st.text(df.columns)
    st.divider()

    st.markdown('### Feature Datatypes')
    st.text(df.dtypes)
    st.divider()

    # shape
    st.markdown('### Shape of Data')
    st.subheader(df.shape)
    st.divider()

    # missing value count
    st.markdown('### Missing Value Count')
    if df.is_empty() == True:
        st.text("No Missing Value Found")
    else:
        missing_value = df.null_count()
        st.write(missing_value)
    st.divider()


    # Correlation Stats
    st.markdown('### Correlation Between Features')
    dtype_select_df = df.select([pl.col(pl.Decimal),pl.col(pl.Float32),pl.col(pl.Float64),pl.col(pl.Int16),pl.col(pl.Int32),pl.col(pl.Int64),pl.col(pl.Int8),pl.col(pl.UInt16),pl.col(pl.UInt32),pl.col(pl.UInt64),pl.col(pl.UInt8),pl.col(pl.Date),pl.col(pl.Datetime),pl.col(pl.Duration),pl.col(pl.Time)])
    dtype_select_df = dtype_select_df.to_pandas()
    correlation_value = dtype_select_df.corr()
    st.dataframe(correlation_value)
    st.divider()


    st.markdown('### Correlation Heatmap of our Dataset')
    dtype_select_df = df.select([pl.col(pl.Decimal),pl.col(pl.Float32),pl.col(pl.Float64),pl.col(pl.Int16),pl.col(pl.Int32),pl.col(pl.Int64),pl.col(pl.Int8),pl.col(pl.UInt16),pl.col(pl.UInt32),pl.col(pl.UInt64),pl.col(pl.UInt8),pl.col(pl.Date),pl.col(pl.Datetime),pl.col(pl.Duration),pl.col(pl.Time)])
    dtype_select_df = dtype_select_df.to_pandas()
    corr = dtype_select_df.corr()
    trace = go.Heatmap(z=corr.values,x=corr.index.values,y=corr.columns.values, colorscale='Blues')
    fig = go.Figure()
    fig.add_trace(trace)
    st.plotly_chart(fig)