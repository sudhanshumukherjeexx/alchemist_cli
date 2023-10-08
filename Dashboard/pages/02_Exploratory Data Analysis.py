import streamlit as st
import polars as pl
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set Plotly template
import plotly.io as pio
pio.templates.default = "plotly_white"


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


# Function to plot Scatter Plot
def plot_scatter(dataframe):
    st.markdown('Visualize your feature - Scatter Plot')
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    st.divider()
    hue = st.selectbox("View scatter plot based on feature", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
    fig1 = px.scatter(dataframe, x=x_axis, y=y_axis, color=hue)
    st.plotly_chart(fig1)


# Function to plot Box Plot
def plot_boxplot(dataframe):
    on = st.toggle('Plot for all Features')
    if on:
        for feature in dataframe.columns:
            container = st.container()
            with container:
                st.subheader(f"Box Plot for {feature}")
                fig = px.box(dataframe, y=feature, orientation="v")
                st.plotly_chart(fig)
    else:
        feature3 = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
        st.subheader(f"Box Plot for {feature3}")
        fig2 = px.box(dataframe, y=feature3, notched=True)
        st.plotly_chart(fig2)


# Function to plot Histogram
def plot_histogram(dataframe):
    on = st.toggle('Plot for all Features')
    if on:
        for feature in dataframe.columns:
            container = st.container()
            with container:
                st.subheader(f"Histogram for {feature}")
                fig = px.histogram(dataframe, x=feature)
                st.plotly_chart(fig)
    else:
        feature4 = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
        st.subheader(f"Histogram for {feature4}")
        fig3 = px.histogram(dataframe, x=feature4)
        st.plotly_chart(fig3)


# Function to plot Bar Chart
def plot_barchart(dataframe):
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    st.divider()
    fig = px.bar(dataframe, x=x_axis, y=y_axis)
    st.plotly_chart(fig)


# Function to create Contour Plot
def create_contour_plot(dataframe):
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    z_axis = st.selectbox('Choose your Feature 3', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    st.write("Please select all three values to display the contour plot.")
    st.header(f"Contour plot of {x_axis}, {y_axis}, and {z_axis}.")
    fig = go.Figure()
    fig.add_trace(go.Contour(x=dataframe[x_axis], y=dataframe[y_axis], z=dataframe[z_axis], line_smoothing=1.3, colorscale='Electric'))
    st.plotly_chart(fig)


# Function to create 2D Histogram Contour
def create_2d_hist_contour(dataframe):
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    hue = st.selectbox("View 2D Histogram Contour based on dataset features.", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
    st.divider()
    st.write("Please select all three values to display the contour plot.")
    st.header(f"2D Histogram Contour of {x_axis} and {y_axis}.")
    fig = px.density_contour(dataframe, x=x_axis, y=y_axis, marginal_x="histogram", marginal_y="histogram", color=hue)
    st.plotly_chart(fig)


# Function to create Pie Chart
def pie_chart(dataframe):
    x_axis = st.selectbox('Choose your values (Numerical Feature)', options=dataframe.columns, index=None, placeholder="[ Numerical Feature ]",)
    y_axis = st.selectbox('Choose your Labels (Categorical Feature)', options=df.columns, index=None, placeholder="[ Categorical Feature ]",)
    st.divider()
    st.write("Please select all the values.")
    fig = px.pie(dataframe, values=x_axis, names=y_axis, title=f"Pie chart of {x_axis} with respect to {y_axis}.", color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig)

def violin_plot(dataframe):
    y_axis = st.selectbox('Choose a feature to visualize: ', options=df.columns, index=None, placeholder="[ Select Feature ]",)
    st.divider()
    st.write("Please select all the values.")
    fig = px.violin(dataframe, y=y_axis, title=f"Violin Plot of {y_axis}.", color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig)

# Function to plot 3D Scatter Plot
def plot_scatter_3d(dataframe):
    st.markdown('Visualize your feature - 3D Scatter Plot')
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    z_axis = st.selectbox('Choose your Feature 3', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    hue = st.selectbox("Color your scatter plot based on feature", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
    fig1 = px.scatter_3d(dataframe, x=x_axis, y=y_axis,z=z_axis, color=hue)
    st.plotly_chart(fig1)

# Function to plot 3D Line Plot
def plot_line_3d(dataframe):
    st.markdown('Visualize your feature - 3D Line Plot')
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    z_axis = st.selectbox('Choose your Feature 3', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    hue = st.selectbox("Color your scatter plot based on feature", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
    fig1 = px.line_3d(dataframe, x=x_axis, y=y_axis,z=z_axis, color=hue)
    st.plotly_chart(fig1)


# # Initial Structure and Functionalities
# st.title('Prepup : Pre Processing Utility Package')
# st.text('Prepup is a free open-source package that lets you inspect, explore, visualize, and perform pre-processing tasks on datasets in your windows/macOS terminal.\nThis is a dashboard version of the package...')


# Load DataFrame
df = st.session_state.get('df')
if df is None:
    st.warning("Please upload a dataset to get started.")
else:
    # Select data types and convert to Pandas DataFrame
    dtype_select_df = select_data_types(df)

    # Define your images and buttons
    card_data = [
        {"image_url": "images/box_plot.png", "button_label": "Box Plot", "action": plot_boxplot},
        {"image_url": "images/scatter_plot.png", "button_label": "Scatter Plot", "action": plot_scatter},
        {"image_url": "images/histogram.png", "button_label": "Histogram", "action": plot_histogram},
        {"image_url": "images/statistic.png", "button_label": "Bar Chart", "action": plot_barchart},
        {"image_url": "images/pie_chart.png", "button_label": "Pie Chart", "action": pie_chart},
        {"image_url": "images/hist2dcontour.png", "button_label": "2D Hist Contour", "action": create_2d_hist_contour},
        {"image_url": "images/contour.png", "button_label": "Contour Plot", "action": create_contour_plot},
        {"image_url": "images/violin.png", "button_label": "Violin Plot", "action": violin_plot},
        {"image_url": "images/3d_scatter.png", "button_label": "3D Scatter Plot", "action": plot_scatter_3d},
        {"image_url": "images/3d_line.png", "button_label": "3D Line Plot", "action": plot_line_3d},
    ]

    # st.divider()
    st.title('😎Exploratory Data Analysis: Available Viz')

    # Initialize session state for navigation
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if st.button("Clear Cache", key='home_button', use_container_width=True):
        st.session_state.page = 'home'

    # Create visualization card for EDA
    cols = st.columns(5)
    num_cols = len(card_data)
    rows = num_cols // 5 + (1 if num_cols % 5 != 0 else 0)

    for i in range(rows):
        with st.container():
            cols = st.columns(5)
            for j in range(i * 5, min((i + 1) * 5, num_cols)):
                with cols[j % 5]:
                    st.image(card_data[j]["image_url"], width=100)
                    if st.button(card_data[j]["button_label"]):
                        st.session_state.page = card_data[j]["action"].__name__

    # Navigation logic for different plots
    if st.session_state.page:
        st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
        if st.session_state.page == 'plot_boxplot':
            plot_boxplot(dtype_select_df)
        elif st.session_state.page == 'plot_scatter':
            plot_scatter(dtype_select_df)
        elif st.session_state.page == 'plot_histogram':
            plot_histogram(dtype_select_df)
        elif st.session_state.page == 'plot_barchart':
            plot_barchart(dtype_select_df)
        elif st.session_state.page == 'create_2d_hist_contour':
            create_2d_hist_contour(dtype_select_df)
        elif st.session_state.page == 'create_contour_plot':
            create_contour_plot(dtype_select_df)
        elif st.session_state.page == 'pie_chart':
            pie_chart(df)
        elif st.session_state.page == 'violin_plot':
            violin_plot(df)
        elif st.session_state.page == 'plot_scatter_3d':
            plot_scatter_3d(df)
        elif st.session_state.page == 'plot_line_3d':
            plot_line_3d(df)
