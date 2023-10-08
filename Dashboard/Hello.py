import streamlit as st
import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px


st.set_page_config(
    page_title="Prepup-App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        "Report a bug": None,
        "About": None
    }
)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.title('Prepup-App')
uploaded_file = st.sidebar.file_uploader("Choose a file")

st.title('Prepup : Pre Processing Utility Package')
st.text('Prepup is a free open-source package that lets you inspect, explore, visualize, and perform pre-processing tasks on datasets in your windows/macOS terminal.\nThis is a dashboard version of the package...')
st.image("image.png",output_format="auto")

#Upload CSV/EXCEL file
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pl.read_csv(uploaded_file, ignore_errors=True)
        st.session_state['df'] = df
    elif uploaded_file.name.endswith('.xlsx'):
        df = pl.read_excel(uploaded_file)
        st.session_state['df'] = df
    elif uploaded_file.name.endswith('.parquet'):
        df = pl.read_parquet(uploaded_file)
        st.session_state['df'] = df
    else:
        st.write("Invalid File Format, Only CSV, EXCEL and PARQUET file formats are supported.")


