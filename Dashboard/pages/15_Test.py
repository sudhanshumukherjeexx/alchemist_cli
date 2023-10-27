####### EDA CODE ###########
# #-----------------------------------------------------------
# import streamlit as st
# import polars as pl
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.graph_objects as go
# import plotly.express as px
# import plotly.io as pio

# pio.templates.default = "plotly_white"

# #------------------------------------------------------------------
# # Initial Structure and Functionalities
# #------------------------------------------------------------------
# st.title('Prepup : Pre Processing Utility Package')
# st.text('Prepup is a free open-source package that lets you inspect, explore, visualize, and perform pre-processing tasks on datasets in your windows/macOS terminal.\nThis is a dashboard version of the package...')

# df = st.session_state['df']

# dtype_select_df = df.select([pl.col(pl.Decimal),pl.col(pl.Float32),pl.col(pl.Float64),pl.col(pl.Int16),pl.col(pl.Int32),pl.col(pl.Int64),pl.col(pl.Int8),pl.col(pl.UInt16),pl.col(pl.UInt32),pl.col(pl.UInt64),pl.col(pl.UInt8),pl.col(pl.Date),pl.col(pl.Datetime),pl.col(pl.Duration),pl.col(pl.Time)])
# dtype_select_df = dtype_select_df.to_pandas()


# # Define your images and buttons
# card_data = [
#     {"image_url": "images/box_plot.png", "button_label": "Box Plot", "action": "Display Message 1"},
#     {"image_url": "images/scatter_plot.png", "button_label": "Scatter Plot", "action": "Display Message 2"},
#     {"image_url": "images/histogram.png", "button_label": "Histogram", "action": "Display Message 3"},
#     {"image_url": "images/statistic.png", "button_label": "Bar Chart", "action": "Display Message 4"},
#     {"image_url": "images/pie_chart.png", "button_label": "Pie Chart", "action": "Display Message 5"},
#     {"image_url": "images/hist2dcontour.png", "button_label": "2D Hist Contour", "action": "Display Message 6"},
#     {"image_url": "images/contour.png", "button_label": "Contour Plot", "action": "Display Message 7"},
#     {"image_url": "image.png", "button_label": "Button 8", "action": "Display Message 8"},
#     {"image_url": "image.png", "button_label": "Button 9", "action": "Display Message 9"},
#     {"image_url": "image.png", "button_label": "Button 10", "action": "Display Message 10"},
# ]

# st.divider()
# st.title('🖌️ Plots Available - Exploratory Data Analysis')

# # Initialize session state for navigation
# if 'page' not in st.session_state:
#     st.session_state.page = 'home'

# if st.button("Clear Cache", key='home_button', use_container_width=True):
#     st.session_state.page = 'home'

# #------------------------------------------------------------------------------------------------------------
# # # Visualize
# # st.sidebar.title('Plots Available')
# # options1 = st.sidebar.radio("Classic" ,options=["Box Plot","Histogram","Scatter Plot", "Bar Chart"])
# # if options1 == "Scatter Plot":
# #     plot_scatter(dtype_select_df)
# # elif options1 == "Box Plot":
# #     plot_boxplot(dtype_select_df)
# # elif options1 == "Histogram":
# #     plot_histogram(dtype_select_df)
# # elif options1 == "Bar Chart":
# #     plot_barchart(df)
# #------------------------------------------------------------------------------------------------------------


# # Scatter Plot
# def plot_scatter(dataframe):
#     st.markdown('Visualize your feature - Scatter Plot')
#     x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns,index=None,  placeholder = "[ Select X-Axis value ]",)
#     y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns,index=None,  placeholder = "[ Select Y-Axis value ]",)
#     st.divider()
#     hue =  st.selectbox("View scatter plot based on feature",options=df.columns, index=None, placeholder= "[ Select your Feature ]",)
#     fig1 = px.scatter(dtype_select_df, x = x_axis, y = y_axis, color=hue)
#     st.plotly_chart(fig1)
#     return 1


# # Box Plot
# def plot_boxplot(dataframe):
#     on = st.toggle('Plot for all Features')
#     if on:
#         for feature in dataframe.columns:
#             container = st.container()
#             with container:
#                 st.subheader(f"Box Plot for {feature}")
#                 fig = px.box(dataframe, y=feature, orientation="v")
#                 st.plotly_chart(fig)
#     else:
#         feature3 = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder = "[ Select X-Axis value ]",)
#         st.subheader(f"Box Plot for {feature3}")
#         fig2 = px.box(dataframe,y=feature3, notched=True)
#         st.plotly_chart(fig2)


# # Histogram
# def plot_histogram(dataframe):
#     on = st.toggle('Plot for all Features')
#     if on:
#         for feature in dataframe.columns:
#             container = st.container()
#             with container:
#                 st.subheader(f"Histogram for {feature}")
#                 fig = px.histogram(dataframe, x=feature)
#                 st.plotly_chart(fig)
#     else:
#         feature4 = st.selectbox('Choose your Feature 1', options=dataframe.columns, index=None, placeholder = "[ Select X-Axis value ]",)
#         st.subheader(f"Histogram for {feature4}")
#         fig3 = px.histogram(dataframe,x=feature4)
#         st.plotly_chart(fig3)

# # Bar Chart
# def plot_barchart(dataframe):
#     x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns,index=None,  placeholder = "[ Select X-Axis value ]",)
#     y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns,index=None,  placeholder = "[ Select Y-Axis value ]",)
#     st.divider()
#     fig = px.bar(dataframe, x=x_axis, y=y_axis)
#     st.plotly_chart(fig)
#     return 1
    
# # Contour Plot
# def create_contour_plot(dataframe):
#     x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns,index=None,  placeholder = "[ Select X-Axis value ]",)
#     y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns,index=None,  placeholder = "[ Select Y-Axis value ]",)
#     z_axis = st.selectbox('Choose your Feature 3', options=dataframe.columns,index=None,  placeholder = "[ Select Z-Axis value ]",)
#     st.divider()
#     st.write("Please select all the three values to displat the contour plot.")
#     st.header(f"Contour plot of {x_axis} , {y_axis} and {z_axis}.")
#     fig = go.Figure()
#     fig.add_trace(go.Contour(x=dataframe[x_axis], y=dataframe[y_axis], z=dataframe[z_axis], line_smoothing=1.3,colorscale='Electric' ))
#     st.plotly_chart(fig)
#     return 1

# # 2D Histogram Contour
# def create_2d_hist_contour(dataframe):
#     x_axis = st.selectbox('Choose your Feature 1', options=dataframe.columns,index=None,  placeholder = "[ Select X-Axis value ]",)
#     y_axis = st.selectbox('Choose your Feature 2', options=dataframe.columns,index=None,  placeholder = "[ Select Y-Axis value ]",)
#     hue =  st.selectbox("View 2D Histogram Contour based on dataset features.",options=df.columns, index=None, placeholder= "[ Select your Feature ]",)
#     st.divider()
#     st.write("Please select all the three values to displat the contour plot.")
#     st.header(f"2D Histogram Contour of {x_axis} and {y_axis}.")
#     fig = px.density_contour(dataframe, x=x_axis, y=y_axis, marginal_x="histogram", marginal_y="histogram", color=hue)
#     st.plotly_chart(fig)
#     return 1


# # Pie Chart
# def pie_chart(dataframe):
#     x_axis = st.selectbox('Choose your values (Numerical Feature)', options=dataframe.columns,index=None,  placeholder = "[ Numerical Feature ]",)
#     y_axis = st.selectbox('Choose your Labels (Categorical Feature)', options=df.columns,index=None,  placeholder = "[ Categorical Feature ]",)
#     #hue =  st.selectbox("View 2D Histogram Contour based on dataset features.",options=df.columns, index=None, placeholder= "[ Select your Feature ]",)
#     st.divider()
#     st.write("Please select all the values.")
#     fig = px.pie(dataframe, values=x_axis, names=y_axis, title=f"Pie chart of {x_axis} with respect to {y_axis}.", color_discrete_sequence=px.colors.sequential.Teal)
#     st.plotly_chart(fig)
#     return 1


# #------------------------------------------------
# # Create visualization card for EDA
# # Create 3 columns
# #------------------------------------------------


# col1, col2, col3, col4, col5 = st.columns(5)

# # Box Plot
# with col1:
#     #st.write("1. Box Plot")
#     st.image(card_data[0]["image_url"],width=100 )
#     if st.button(card_data[0]["button_label"]):
#         st.session_state.page='box_plot'
#         #plot_boxplot(dtype_select_df)
#         #st.write(card_data[0]["action"])

# # box pLot navigation logic
# if st.session_state.page == 'box_plot':
#     st.header("Box Plot")
#     st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
#     plot_boxplot(dtype_select_df)
#     st.divider()


# # Scatter Plot
# with col2:
#     st.image(card_data[1]["image_url"],width=100 )
#     if st.button(card_data[1]["button_label"]):
#         st.session_state.page='scatter_plot'
#         # plot_scatter(dtype_select_df)
#         # st.write(card_data[1]["action"])

# # scatter pLot navigation logic
# if st.session_state.page == 'scatter_plot':
#     st.header("Scatter Plot")
#     st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
#     plot_scatter(dtype_select_df)
#     st.divider()


# # Histogram
# with col3:
#     st.image(card_data[2]["image_url"],width=100 )
#     if st.button(card_data[2]["button_label"]):
#         st.session_state.page='histogram'
#         # plot_histogram(dtype_select_df)
#         # st.write(card_data[2]["action"])

# # histogram pLot navigation logic
# if st.session_state.page == 'histogram':
#     st.header("Histogram")
#     st.write("Histogram")
#     st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
#     plot_histogram(dtype_select_df)
#     st.divider()


# # Bar Chart
# with col4:
#     st.image(card_data[3]["image_url"],width=100 )
#     if st.button(card_data[3]["button_label"]):
#         st.session_state.page='barchart'
        
# # barchart navigation logic
# if st.session_state.page == 'barchart':
#     st.header("Bar Chart")
#     st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
#     plot_barchart(dtype_select_df)
#     st.divider()

# with col5:
#     #st.write("1. Box Plot")
#     st.image(card_data[4]["image_url"],width=100 )
#     if st.button(card_data[4]["button_label"]):
#         st.session_state.page='pie_chart'
        
# # barchart navigation logic
# if st.session_state.page == 'pie_chart':
#     st.header("Pie Chart")
#     st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
#     pie_chart(df)
#     st.divider()



# # New Row
# st.write("\n")
# # Create 3 columns
# col6, col7, col8, col9, col10 = st.columns(5)

# # 2D Histogram Contour
# with col6:
#     #st.write("1. Box Plot")
#     st.image(card_data[5]["image_url"],width=100 )
#     if st.button(card_data[5]["button_label"]):
#         st.session_state.page='2d_contour'
        
# # 2D Histogram Contour Chart navigation logic
# if st.session_state.page == '2d_contour':
#     st.header("Contour Chart")
#     st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
#     create_2d_hist_contour(dtype_select_df)
#     st.divider()

# # Contour
# with col7:
#     #st.write("1. Box Plot")
#     st.image(card_data[6]["image_url"],width=110 )
#     if st.button(card_data[6]["button_label"]):
#         st.session_state.page='contour'
        

# # Contour chart navigation logic
# if st.session_state.page == 'contour':
#     st.header("Contour Chart")
#     st.markdown("<a name='scroll'></a>", unsafe_allow_html=True)
#     create_contour_plot(dtype_select_df)
#     st.divider()





# TILE MAP
# def plot_map(dataframe):
#     x_axis = st.selectbox('Latitude', options=dataframe.columns, index=None, placeholder="[ Select X-Axis value ]",)
#     y_axis = st.selectbox('Longitude', options=dataframe.columns, index=None, placeholder="[ Select Y-Axis value ]",)
#     data = [
#         go.Scattergeo(
#             lat=dataframe[x_axis],
#             lon=dataframe[y_axis],
#             mode='markers',
#             marker=dict(
#                 size=10,
#                 symbol='circle',
#                 color='blue',
#                 opacity=0.7,
#             ),
#         )
#     ]
#     layout = go.Layout(
#         geo=dict(
#             showland=True,
#         ),
#         margin=dict(l=0, r=0, t=0, b=0),
#     )

#     fig1 = go.Figure(data=data, layout=layout)

#     st.plotly_chart(fig1)

import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

def q_q_plots(dataframe):
    # Get the numerical columns
    numerical_columns = dataframe.select_dtypes(include=[np.number]).columns
    for column in numerical_columns:
        # Sort the data by the current numerical column
        sorted_data = dataframe.sort_values(by=[column])
        # Calculate the quantiles or ranks
        num_points = len(dataframe)
        quantiles = np.arange(1, num_points + 1) / (num_points + 1)
        # Create the tail-tail plot for the current column
        fig = px.scatter(sorted_data, x=column, y=quantiles, labels={column: "Data Values", "y": "Quantiles"}, hover_data=column, title=column)
        # Add a straight line for expected quantiles of a normal distribution
        fig.add_shape(
            type='line',
            x0=sorted_data[column].min(),
            x1=sorted_data[column].max(),
            y0=0,
            y1=1,
            line=dict(color='red', width=2)
        )
        st.plotly_chart(fig)



import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.subplots as sp

def hist_qq_plots(dataframe):
    # Get the numerical columns
    numerical_columns = dataframe.select_dtypes(include=[np.number]).columns
    for column in numerical_columns:
        st.markdown(f"##### {column}".upper())
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

# Example usage:
# hist_qq_plots(your_dataframe)




df = st.session_state.get('df')
df = df.to_pandas()
# Example usage:
#q_q_plots(df)
hist_qq_plots(df)
