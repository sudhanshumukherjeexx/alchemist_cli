import streamlit as st
import polars as pl
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from urllib.request import urlopen
import json


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
    st.markdown('### Scatter Plot')
    st.markdown('- A Scatter Plot is a visual representation of data points on a graph, showcasing the relationship between two variables and revealing patterns or trends in a concise and easily interpretable manner.')
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    st.divider()
    if x_axis and y_axis is not None:
        hue = st.selectbox("View scatter plot based on feature", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
        fig1 = px.scatter(dataframe, x=x_axis, y=y_axis, color=hue)
        st.plotly_chart(fig1)
    else:
        st.warning("Please select both X and Y axes for the scatter plot.")


# Function to plot Box Plot
def plot_boxplot(dataframe):
    st.markdown('### Box Plot')
    st.markdown('- A Box Plot, or box-and-whisker plot, is a graphical representation that displays the distribution of a dataset, providing insights into its central tendency, spread, and presence of outliers. It presents data in a compact and intuitive manner, making it easy to identify key statistical characteristics.')
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
    st.markdown('### Histogram')
    st.markdown("- A histogram is a graphical representation of data distribution, using bars to display the frequency or count of values within specified intervals or bins. It offers a visual overview of data patterns, highlighting peaks and variations, enabling quick insights into the dataset's shape and characteristics.")
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
    st.markdown('### Bar Plot')
    st.markdown('- A Bar Plot is a visual representation of data using rectangular bars of varying heights to illustrate the values of different categories or groups. It is a widely-used tool for comparing data across categories and displaying patterns or variations in a clear and straightforward manner.')
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    st.divider()
    fig = px.bar(dataframe, x=x_axis, y=y_axis)
    st.plotly_chart(fig)


# Function to create Contour Plot
def create_contour_plot(dataframe):
    st.markdown('### Contour Plot')
    st.markdown("- A Contour Plot is a visual representation that displays three-dimensional data on a two-dimensional surface using contour lines to depict changes in a third variable. It's a valuable tool for visualizing complex relationships and surfaces, commonly used in scientific and engineering fields to illustrate topography, temperature, and more.")
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    z_axis = st.selectbox('Choose your Feature 3', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    if x_axis and y_axis and z_axis is not None:
        st.header(f"Contour plot of {x_axis}, {y_axis}, and {z_axis}.")
        fig = go.Figure()
        fig.add_trace(go.Contour(x=dataframe[x_axis], y=dataframe[y_axis], z=dataframe[z_axis], line_smoothing=1.3, colorscale='Electric'))
        st.plotly_chart(fig)
    else:
        st.warning("Please select X, Y and Z axes for the Contour plot.")


# Function to create 2D Histogram Contour
def create_2d_hist_contour(dataframe):
    st.markdown("### 2D Histogram Contour")
    st.markdown("- A 2D Histogram Contour is a graphical representation that combines a two-dimensional histogram with contour lines to visualize the distribution and density of data points in a scatter plot. It provides a clear depiction of data concentration, revealing areas of high and low density in the plot, making it useful for data analysis and pattern recognition.")
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    hue = st.selectbox("View 2D Histogram Contour based on dataset features.", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
    st.divider()
    if x_axis and y_axis is not None:
        st.header(f"2D Histogram Contour of {x_axis} and {y_axis}.")
        fig = px.density_contour(dataframe, x=x_axis, y=y_axis, marginal_x="histogram", marginal_y="histogram", color=hue)
        st.plotly_chart(fig)
    else:
        st.warning("Please select both X and Y axes for the 2D Histogram Contour plot.")


# Function to create Pie Chart
def pie_chart(dataframe):
    st.markdown("### Pie Chart")
    st.markdown("- A Pie Chart is a circular graph that divides data into slices or wedges, where each slice represents a proportion or percentage of the whole. It is a visually intuitive way to display categorical data and illustrate the composition or distribution of different categories within a dataset.")
    x_axis = st.selectbox('Choose your values (Numerical Feature)', options=dataframe.columns, index=None, placeholder="[ Numerical Feature ]",)
    y_axis = st.selectbox('Choose your Labels (Categorical Feature)', options=df.columns, index=None, placeholder="[ Categorical Feature ]",)
    st.divider()
    if x_axis and y_axis is not None:
        fig = px.pie(dataframe, values=x_axis, names=y_axis, title=f"Pie chart of {x_axis} with respect to {y_axis}.", color_discrete_sequence=px.colors.sequential.Teal)
        st.plotly_chart(fig)
    else:
        st.warning("Please select both X and Y axes for the Pie Chart.")


def violin_plot(dataframe):
    st.markdown('### Violin Plot')
    st.markdown('- A Violin Plot is a data visualization that combines elements of a box plot and a kernel density plot to display the distribution and summary statistics of a dataset. It provides a detailed view of data distribution, revealing both central tendency and the probability density of different values, making it useful for comparing multiple categories or groups.')
    y_axis = st.selectbox('Choose a feature to visualize: ', options=df.columns, index=None, placeholder="[ Select Feature ]",)
    st.divider()
    if y_axis is not None:
        fig = px.violin(dataframe, y=y_axis, title=f"Violin Plot of {y_axis}.", color_discrete_sequence=px.colors.sequential.Teal)
        st.plotly_chart(fig)
    else:
        st.write("Please select all the values from the Dropdown to display the Violin Plot")

# Function to plot line plot
def plot_line(dataframe):
    st.markdown('### Line Plot')
    st.markdown("- A Line Plot, also known as a Line Chart, is a graph that uses lines to connect data points, typically over time. It's a powerful tool for visualizing trends and patterns in data, making it easy to identify fluctuations and changes in values. Line plots are widely used in various fields, including finance, science, and data analysis, to track and illustrate changes in a variable.")
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    st.divider()
    if x_axis or y_axis is not None:
        hue = st.selectbox("Color your scatter plot based on feature", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
        fig1 = px.line(dataframe, x=x_axis, y=y_axis,color=hue)
        st.plotly_chart(fig1)
    else:
        st.warning("Please select X or Y axes for the line plot.")



# Function to plot 3D Scatter Plot
def plot_scatter_3d(dataframe):
    st.markdown('### 3D Scatter Plot')
    st.markdown("- A 3D Scatter Plot is a three-dimensional representation of data points, where each point is defined by three variables. It allows for the visualization of complex relationships between multiple variables in a 3D space. This type of plot is particularly useful for exploring and understanding data that involves three key factors or dimensions.")
    st.markdown('Visualize your feature - 3D Scatter Plot')
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    z_axis = st.selectbox('Choose your Feature 3', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    if x_axis and y_axis and z_axis is not None:
        hue = st.selectbox("Color your scatter plot based on feature", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
        fig1 = px.scatter_3d(dataframe, x=x_axis, y=y_axis,z=z_axis, color=hue)
        st.plotly_chart(fig1)
    else:
        st.write("Please select X, Y and Z axes for the 3D Scatter plot.")

# Function to plot 3D Line Plot
def plot_line_3d(dataframe):
    st.markdown('### 3D Line Plot')
    st.markdown("- A 3D Line Plot is a three-dimensional representation of data that uses lines to connect data points in a 3D space. It's a valuable tool for visualizing and understanding data with three dimensions, such as time series data or spatial data. 3D line plots enable the exploration of trends and patterns across three variables, providing a comprehensive view of data relationships.")
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    z_axis = st.selectbox('Choose your Feature 3', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    if x_axis and y_axis and z_axis is not None:
        hue = st.selectbox("Color your scatter plot based on feature", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
        fig1 = px.line_3d(dataframe, x=x_axis, y=y_axis,z=z_axis, color=hue)
        st.plotly_chart(fig1)
    else:
        st.write("Please select X, Y and Z axes for the 3D Line plot.")

#Function to plot Polar Scatter
def plot_scatter_polar(dataframe):
    st.markdown('### Polar Scatter')
    st.markdown("- A Polar Scatter Plot is a data visualization that represents data points in a polar coordinate system. It's particularly useful for displaying data with angular and radial components, such as geographic data or circular patterns. In a polar scatter plot, each point is positioned according to an angle and distance from the center, making it easy to identify patterns and relationships within the data, especially when working with circular or directional data.")
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    hue = st.selectbox('Choose a feature to view results based on color', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    if x_axis and y_axis is not None:
        shape = st.selectbox("Choose a feature to display results based on different shapes.", options=df.columns, index=None, placeholder="[ Select your Feature ]",)
        fig1 = px.scatter_polar(dataframe, r=x_axis, theta=y_axis, color=hue, symbol=shape, color_discrete_sequence=px.colors.sequential.Plasma_r)
        st.plotly_chart(fig1)
    else:
        st.write("Please select both X and Y axes for the Polar Scatter plot.")


# Function to plot Polar Scatter
def plot_bar_polar(dataframe):
    st.markdown('### Polar Bar')
    st.markdown("- A Polar Bar Plot, also known as a Radial Bar Chart, is a unique data visualization that displays data using bars arranged in a circular or radial pattern. It is particularly useful for showcasing data with a directional or cyclical nature, such as time series data with periodic patterns. Each bar extends from the center outward, representing data values at specific angles. This type of plot is ideal for visualizing and comparing data across categories or groups with an inherent circular relationship.")
    x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    hue = st.selectbox('Choose a feature to view results based on color', options=dataframe.columns, index=None, placeholder="[ Select Z-Axis value ]",)
    st.divider()
    if x_axis and y_axis is not None:
        fig1 = px.bar_polar(dataframe, r=x_axis, theta=y_axis, color=hue, color_discrete_sequence=px.colors.sequential.Plasma_r)
        st.plotly_chart(fig1)
    else:
        st.write("Please select both X and Y axes for the Polar Bar plot.")


# Funtion to plot tile map
def plot_tile_map(dataframe):
    st.markdown('### Tile Map')
    st.markdown("- A Tile Map is a data visualization technique that uses small, uniformly-sized squares (tiles) to represent data values within a grid or map. Each tile's color or shading corresponds to a specific data category or variable, allowing for the visualization of spatial data patterns. Tile maps are particularly useful for showcasing geographic and spatial data, making it easy to identify clusters, trends, and variations across regions or areas.")
    x_axis = st.selectbox('Latitude', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
    y_axis = st.selectbox('Longitude', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
    #options = st.multiselect(dataframe.columns)
    st.divider()
    if x_axis and y_axis is not None:
        shape = st.multiselect("Choose a feature to display results based on different shapes.", options=df.columns,placeholder="[ Select your Feature ]",)
        fig1 = px.scatter_mapbox(dataframe, lat=x_axis, lon=y_axis, hover_data=shape, color_discrete_sequence=["fuchsia"])
        fig1.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig1)
    else:
        st.write("Please select both X and Y axes for the Plot Tile Map.")

def plot_choropleth_map(dataframe):
    st.markdown('### Choropleth Map')
    st.markdown("- A Choropleth Map is a thematic map that represents data by shading or coloring geographic regions, such as countries, states, or districts, based on the intensity or magnitude of a particular variable. The varying colors or patterns across the map's regions provide a visual representation of data distribution, making it a powerful tool for displaying spatial data and highlighting geographical patterns or disparities in a clear and easily interpretable manner. Choropleth maps are commonly used in fields like geography, economics, and epidemiology for data visualization and analysis.")
    st.markdown("- Best to visualize US data if FIPS code is available in your data.")
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    
    x_axis = st.selectbox('FIPS Code', options=dataframe.columns, index=None, placeholder="[ FIPS Code ]",)
    y_axis = st.selectbox('Choose a feature to visualize based on FIPS code.', options=dataframe.columns, index=None, placeholder="[ Choose a feature to visualize based on FIPS code. ]",)
    #options = st.multiselect(dataframe.columns)
    st.divider()
    if x_axis and y_axis is not None:
        fig1 = px.choropleth(dataframe, geojson=counties, locations=x_axis, color=y_axis, color_continuous_scale="Viridis",range_color=(0,12), scope="usa", labels={'{y_axis}': '{y_axis} Rate'})
        st.plotly_chart(fig1)
    else:
        st.write("Please select both X and Y axes for the Choropleth Map.")



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
        {"image_url": "images/line.png", "button_label": "Line Plot", "action": plot_line},
        {"image_url": "images/hist2dcontour.png", "button_label": "2D Hist Contour", "action": create_2d_hist_contour},
        {"image_url": "images/contour.png", "button_label": "Contour Plot", "action": create_contour_plot},
        {"image_url": "images/violin.png", "button_label": "Violin Plot", "action": violin_plot},
        {"image_url": "images/3d_scatter.png", "button_label": "3D Scatter Plot", "action": plot_scatter_3d},
        {"image_url": "images/3d_line.png", "button_label": "3D Line Plot", "action": plot_line_3d},
        {"image_url": "images/polar_scatter.png", "button_label": "Polar Scatter", "action": plot_scatter_polar},
        {"image_url": "images/polar_bar.png", "button_label": "Polar Bar", "action": plot_bar_polar},
        {"image_url": "images/tile_map.png", "button_label": "Tile Map", "action": plot_tile_map},
        {"image_url": "images/choropleth_map.png", "button_label": "Choropleth Map", "action": plot_choropleth_map},
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
        elif st.session_state.page == 'plot_line':
            plot_line(df)
        elif st.session_state.page == 'plot_scatter_polar':
            plot_scatter_polar(df)
        elif st.session_state.page == 'plot_bar_polar':
            plot_bar_polar(df)
        elif st.session_state.page == 'plot_tile_map':
            plot_tile_map(df)
        elif st.session_state.page == 'plot_choropleth_map':
            plot_choropleth_map(df)
