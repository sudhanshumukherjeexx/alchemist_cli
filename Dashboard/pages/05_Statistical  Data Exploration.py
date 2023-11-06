import streamlit as st
import polars as pl
import pandas as pd
import numpy as np
from scipy.stats import shapiro
from scipy.stats import skew
from scipy.stats import kurtosis
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

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
    st.image("images/stats_page.gif")
with col2:
    st.markdown('## Statistical Data Exploration')
    st.markdown("Explore **skewness** and **kurtosis** for data distribution insights, assess **normality and q-q plots** for statistical assumptions, and detect **outliers** for data cleansing.")
#st.image("images/page_1.gif",use_column_width=True)
# Load df
df = st.session_state.get('df')
df_processed = st.session_state.get('df_processed')

if df is None:
    st.warning("Please upload a dataset to get started.")
else:
    st.divider()
    st.markdown('🖲️Select the **session state** and **click run analysis**')
    col9, col10 = st.columns(2)
    with col9:
        # Create a dropdown menu to choose the session state
        selected_session_state = st.selectbox("Select Session State", ["Intial DataFrame", "DataFrame after Missing value Imputation"])
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

    def find_outliers(dataframe):
        st.subheader("Find Outliers")

        # Add a slider for the value of k with a default of 1.5
        k = st.slider("Select the value of k", 0.1, 5.0, 1.5, 0.1)

        dtype_select_df = select_data_types(dataframe)

        # Create a list to store column names with outliers
        columns_with_outliers = []

        for column in dtype_select_df.columns:
            values = dtype_select_df[column].values
            q1 = np.percentile(values, 25)
            q3 = np.percentile(values, 75)
            iqr = q3 - q1
            lower_bound = q1 - k * iqr
            upper_bound = q3 + k * iqr
            outliers = (values < lower_bound) | (values > upper_bound)
            num_outliers = outliers.sum()
            
            if num_outliers > 0:
                columns_with_outliers.append(column)

        # Display the names of columns with outliers
        if columns_with_outliers:
            st.success(f"Columns with outliers: {columns_with_outliers} ", icon="✅")
        else:
            st.info("No outliers detected in the selected features.", icon="ℹ️")

    def hist_qq_plots(dataframe):
        dataframe = select_data_types(dataframe)
        # Get the numerical columns
        numerical_columns = dataframe.select_dtypes(include=[np.number]).columns
        for column in numerical_columns:
            st.markdown(f"###### {column}".upper())
            # Create a subplot with 1 row and 2 columns
            fig = sp.make_subplots(rows=1, cols=2, subplot_titles=("Histogram", "QQ Plot"))
            # Generate the histogram
            histogram = go.Histogram(x=dataframe[column], name="Histogram")
            fig.add_trace(histogram, row=1, col=1)
            # Sort the data by the current numerical column
            sorted_data = dataframe.sort_values(by=[column])
            # Calculate the quantiles or ranks
            num_points = len(dataframe)
            quantiles = np.arange(1, num_points + 1) / (num_points + 1)
            # Create the QQ plot for the current column
            qq_plot = go.Scatter(x=sorted_data[column], y=quantiles, mode='markers', name="QQ Plot")
            fig.add_trace(qq_plot, row=1, col=2)
            # Add a straight line for expected quantiles of a normal distribution in the QQ plot
            fig.add_shape(
                type='line',
                x0=sorted_data[column].min(),
                x1=sorted_data[column].max(),
                y0=0,
                y1=1,
                line=dict(color='black', width=2),
                row=1,
                col=2
            )
            st.plotly_chart(fig)


    def calculate_skewness(dataframe):
        dataframe = dataframe.to_pandas()
        numeric_data = dataframe.select_dtypes(['number'])
        skewness_values = skew(numeric_data, axis=0, bias=True)
        skewness_df = pd.DataFrame({'Column': numeric_data.columns, 'Skewness': skewness_values})

        st.write("\t\nSkewness present in the data:")
        st.write(skewness_df)

        # Plot skewness values with column names on hover
        fig = px.line(skewness_df, x='Column', y='Skewness', title="Skewness of Columns")
        fig.update_traces(mode="lines+markers+text", text=skewness_df['Column'], textposition="top right")
        st.plotly_chart(fig)
        
    def calculate_kurtosis(dataframe):
        dataframe = dataframe.to_pandas()
        numeric_data = dataframe.select_dtypes(['number'])
        kurtosis_values = kurtosis(numeric_data, axis=0, bias=True)
        kurtosis_df = pd.DataFrame({'Columns':numeric_data.columns, 'Kurtosis': kurtosis_values})

        st.write("\t\nKurtosis present in the data:")
        st.write(kurtosis_df)

        # Plot Kurtosis with column names on hover
        fig = px.line(kurtosis_df, x='Columns', y='Kurtosis', title="Kurtosis of Columns")
        fig.update_traces(mode="lines+markers+text", text=kurtosis_df['Columns'], textposition="top left")
        st.plotly_chart(fig)

    
    # Sidebar with radio buttons
    st.sidebar.title("Select Analysis:")
    analysis_option = st.sidebar.radio("Choose an analysis:", ["Kurtosis", "Skewness","Find Outliers", "Distribution and Q-Q Plots"])

    with col10:
        # Toggle button to run the analysis
        st.markdown("#### ")
        #st.write(" ")
        run_analysis = st.button("Run Analysis", use_container_width=True)
        st.divider()

    if run_analysis:
        if analysis_option == "Kurtosis":
            result = calculate_kurtosis(df)
            #st.write(f"Kurtosis: {result:.4f}")
        elif analysis_option == "Skewness":
            result = calculate_skewness(df)
            #st.write(f"Skewness: {result:.4f}")
        elif analysis_option == "Distribution and Q-Q Plots":
            result = hist_qq_plots(df)
            #st.write(result)
        elif analysis_option == "Find Outliers":
            result = find_outliers(df)

    # Display description based on the selected radio button
    if analysis_option == "Kurtosis":
        col1, col2 = st.columns(2)
        st.divider()
        with col1:
            st.markdown('### Kurtosis')
            st.markdown("- Kurtosis measures the degree to which a probability distribution's tails differ from those of a normal distribution. High kurtosis indicates heavy tails with more extreme values, while low kurtosis indicates light tails with fewer extreme values, comparing the distribution's peakedness or flatness to a normal distribution.")
        with col2:
            st.markdown("### Kurtosis Significance on Datasets")
            st.markdown("- **Defines Data Shape**: It characterizes data distribution shape, identifying heavy or light tails.")
            st.markdown("- **Influences Risk**: High kurtosis indicates fatter tails, impacting risk assessment.")
            st.markdown("- **Detects Outliers**: It aids in outlier identification.")
            st.markdown("- **Impacts Testing**: It affects statistical test assumptions.")
            st.markdown("- **Guides Modeling**: It helps select appropriate data distributions for modeling.")
    elif analysis_option == "Skewness":
        col3, col4 = st.columns(2)
        st.divider()
        with col3:
            st.markdown('### Skewness')
            st.markdown("- Skewness measures the asymmetry of a probability distribution. Positive skewness indicates a longer tail on the right, while negative skewness means a longer left tail compared to a normal distribution.")
        with col4:
            st.markdown("### Kurtosis Significance on Datasets")
            st.markdown("- **Reveals Data Asymmetry**: Skewness quantifies distribution asymmetry, aiding in understanding data patterns.")
            st.markdown("- **Influences Decision-Making**: Identifying positive or negative skewness guides decisions and strategies in finance and business.")
            st.markdown("- **Impacts Model Selection**: Skewness assists in selecting appropriate models for data analysis.")
            st.markdown("- **Detects Non-Normality**: Skewness helps identify departures from normality, crucial for statistical analysis.")
            st.markdown("- **Supports Variable Transformation**: It informs variable transformations to meet model assumptions and improve accuracy.")
    elif analysis_option == "Distribution and Q-Q Plots":
        col5, col6 = st.columns(2)
        st.divider()
        with col5:
            st.markdown("### Q-Q Plots")
            st.markdown("- Quantile-Quantile plots show how well data fits a theoretical distribution. Points on the plot align with the expected quantiles for a distribution.")
            st.markdown("- For a detailed understanding of Q-Q plot interpretation, I suggest referring to an educational video.")
            st.video('https://www.youtube.com/watch?v=okjYjClSjOg')
        with col6:
            st.markdown("### Normal Distribution")
            st.markdown("- A normal distribution, also known as a Gaussian distribution, is a continuous probability distribution characterized by a symmetric, bell-shaped curve. In a normal distribution, the mean, median, and mode are all equal, and the data is evenly spread around the mean.")
            st.markdown("### Significance of Q-Q Plots and Normal Distribution.")
            st.write("1. Q-Q plots help assess if data follows a normal distribution.\n2. Points close to the red line indicate data's similarity to a normal distribution.\n3. Deviations suggest departures from normality.\n4. Useful for statistical analysis and modeling.\n5. Can detect outliers and assess data's goodness-of-fit.")
            #st.markdown("")
            #st.markdown("3. Deviations suggest departures from normality.")
            #st.markdown("4. Useful for statistical analysis and modeling.")
            #st.markdown("5. Can detect outliers and assess data's goodness-of-fit.")
            

    elif analysis_option == "Find Outliers":
        col7, col8 = st.columns(2)
        st.divider()
        with col7:
            st.markdown("### Outliers")
            st.markdown("- Outliers are extreme data points that deviate significantly from the majority of a dataset. They can result from errors, anomalies, or unique observations and play a crucial role in data analysis.Understanding outliers is essential in statistical analysis as they can distort measures, impact data distribution, and offer insights into data quality and patterns.")
        with col8:
            st.markdown("### Why Outliers are Important?")
            st.markdown("- **Reveals Data Asymmetry**: Skewness quantifies distribution asymmetry, aiding in understanding data patterns.")
            st.markdown("- **Influences Decision-Making**: Identifying positive or negative skewness guides decisions and strategies in finance and business.")
            st.markdown("- **Impacts Model Selection**: Skewness assists in selecting appropriate models for data analysis.")
            st.markdown("- **Detects Non-Normality**: Skewness helps identify departures from normality, crucial for statistical analysis.")
            st.markdown("- **Supports Variable Transformation**: It informs variable transformations to meet model assumptions and improve accuracy.")