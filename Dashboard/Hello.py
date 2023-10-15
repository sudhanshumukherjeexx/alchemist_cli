import streamlit as st
import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import streamlit.components.v1 as components
import time


st.set_page_config(
    page_title="Prepup Labs",
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

st.title('Prepup Labs: Data, Design and Discovery 🥽')
col1, col2 = st.columns(2, gap="small")
with col1:
    #main page
    st.image("images/home_remove.gif",use_column_width=True)
with col2:
    
    st.markdown('#### A Rapid Prototyping Environment for Data Scientists')
    st.write('Built with 💖 by [Sudhanshu Mukherjee](https://github.com/sudhanshumukherjeexx)')
    st.write('Research Advisor: [Dr. Alfa R Heryudono](http://www.math.umassd.edu/~aheryudono/index.html)')
    st.write('##### [University of Massachusetts at Dartmouth](https://www.umassd.edu/)')
    audio_file = open("audio/intro_audio.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

st.divider()
st.subheader('💻 Usage') 
tool_desc = """

1. <b>Home Page:</b> Unearth the Data Secrets
   - Right here, at the threshold of data exploration, you stand. Upload your dataset and embark on a journey into the heart of data science.

2. <b>Data Statistics:</b> Decipher the Data Enigma
   - Delve into the essence of your dataset. Discover its hidden stories, features galore, the enigma of missing values, and the intricate dance of feature correlations.

3. <b>Exploratory Data Analysis:</b> Visualize the Data Symphony
   - Step into a realm of data visualization. Dive deep into your dataset with enchanting Scatter Plots, mysterious Box Plots, and an array of captivating visualizations. Uncover the data's artistic side.

4. <b>Missing Values:</b> Restore the Data Harmony
   - Eight methods, eight keys to restore harmony. Impute missing values and resurrect the completeness of your dataset. From Mean to Magic, choose your path to data integrity.

"""
st.write(f"{tool_desc}", unsafe_allow_html=True)

st.divider()
st.subheader('🌐 Summary')
intro_text = """
    Prepup Labs is a rapid prototyping environment designed for data scientists, empowering them to accelerate their data science workflow from start to finish! 
    
    With its intuitive interface, Prepup Labs offers the following key capabilities:

    <b>Data Ingestion:</b> Simplifies the process of reading and importing data from various sources, including CSV, Excel, databases, and more. Users can effortlessly 
    load datasets, making it easy to work with real-world data.

    <b>Exploratory Data Analysis (EDA):</b> provides built-in tools for in-depth EDA. Data scientists can explore data distributions, visualize relationships between 
    variables, and gain insights into the dataset's characteristics. Interactive visualizations, such as histograms, scatter plots, and summary statistics, facilitate a 
    comprehensive understanding of the data.
    
    <b>Missing Value Imputation:</b> Addressing missing data is a breeze with Prepup Labs. Users have the flexibility to choose from various imputation methods, including mean, 
    median, or custom values, ensuring that datasets are complete and ready for analysis.

    <b>Dataset Splitting:</b> Offers a straightforward dataset splitting feature, allowing users to divide their data into training, validation, and testing sets. 
    This is crucial for building, evaluating, and fine-tuning machine learning models.

    <b>Machine Learning Integration:</b> Seamlessly integrates popular machine learning libraries and algorithms. Data scientists can select and apply a wide 
    range of algorithms, from regression and classification to clustering and more. The tool supports model training and evaluation, enabling quick experimentation 
    with different approaches.

    Prepup Labs is designed to streamline the data science prototyping phase, reducing the time and effort required to explore, clean, and analyze datasets. 
    By offering a unified environment for data management, EDA, imputation, and machine learning, it empowers data scientists to iterate rapidly and develop 
    data-driven solutions with efficiency and ease.
    """
st.write(f"{intro_text}", unsafe_allow_html=True)
st.divider()
col3, col4 = st.columns(2)
with col3:
    st.markdown('### Author')
    st.write(" Please feel free to contact me with any issues, comments or questions")
    st.markdown('##### Sudhanshu Mukherjee')
    st.markdown('- Email: smukherjee3@umassd.edu')
    st.markdown('- GitHub: https://github.com/sudhanshumukherjeexx')
    st.markdown('### Research Advisor')
    st.markdown('##### Dr. Alfa R Heryudono')
    st.markdown('- Email: aheryudono@umassd.edu')
    st.markdown('- Research Website: http://www.math.umassd.edu/~aheryudono/index.html')

with col4:
    st.markdown('### License')
    st.write('- Apache License 2.0')

st.divider()
st.write('Developed and Maintained by Sudhanshu Mukherjee')
st.write('[Sudhanshu Mukherjee](https://www.linkedin.com/in/sudhanshumukherjeexx/) - [Data Science Portfolio](https://www.datascienceportfol.io/sudhanshumukherjee)')
st.write('Copyright (c) 2023 Sudhanshu Mukherjee')

# st.title('Prepup : Pre Processing Utility Package')
# st.text('Prepup is a free open-source package that lets you inspect, explore, visualize, and perform pre-processing tasks on datasets in your windows/macOS terminal.\nThis is a dashboard version of the package...')
# st.image("images/home4.gif",use_column_width=True, output_format="auto")
# #st.image("image.png",output_format="auto")




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


