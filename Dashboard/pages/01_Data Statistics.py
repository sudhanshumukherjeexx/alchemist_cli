import streamlit as st
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

st.title('Prepup : Pre Processing Utility Package')
st.text('Prepup is a free open-source package that lets you inspect, explore, visualize, and perform pre-processing tasks on datasets in your windows/macOS terminal.\nThis is a dashboard version of the package...')

df = st.session_state['df']

# page Title
st.header('Data Statistics')
st.write(df.describe())

# features Stats
st.header('Features Available')
st.text(df.columns)

st.header('Feature Datatypes')
st.text(df.dtypes)

# shape
st.header('Shape of Data')
st.subheader(df.shape)

# missing value count
st.header('Missing Value Count')
if df.is_empty() == True:
    st.text("No Missing Value Found")
else:
    missing_value = df.null_count()
    st.write(missing_value)


# Correlation Stats
st.header('Correlation Between Features')
dtype_select_df = df.select([pl.col(pl.Decimal),pl.col(pl.Float32),pl.col(pl.Float64),pl.col(pl.Int16),pl.col(pl.Int32),pl.col(pl.Int64),pl.col(pl.Int8),pl.col(pl.UInt16),pl.col(pl.UInt32),pl.col(pl.UInt64),pl.col(pl.UInt8),pl.col(pl.Date),pl.col(pl.Datetime),pl.col(pl.Duration),pl.col(pl.Time)])
dtype_select_df = dtype_select_df.to_pandas()
correlation_value = dtype_select_df.corr()
st.write(correlation_value)


st.header('Correlation Heatmap of our Dataset')
dtype_select_df = df.select([pl.col(pl.Decimal),pl.col(pl.Float32),pl.col(pl.Float64),pl.col(pl.Int16),pl.col(pl.Int32),pl.col(pl.Int64),pl.col(pl.Int8),pl.col(pl.UInt16),pl.col(pl.UInt32),pl.col(pl.UInt64),pl.col(pl.UInt8),pl.col(pl.Date),pl.col(pl.Datetime),pl.col(pl.Duration),pl.col(pl.Time)])
dtype_select_df = dtype_select_df.to_pandas()
corr = dtype_select_df.corr()
trace = go.Heatmap(z=corr.values,x=corr.index.values,y=corr.columns.values)
fig = go.Figure()
fig.add_trace(trace)
st.plotly_chart(fig)