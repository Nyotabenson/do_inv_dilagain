import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import do_datanalysis
import do_datafetch

import plotly.express as px
import streamlit as st

def pie_visual():
    
    data = do_datanalysis.fetch_total_quantities()
    values = data.iloc[0]
    labels = data.columns.to_list()

    
    fig = px.pie(
        values=values, 
        names=labels,
        hole=0.3  
       )
    fig.update_traces(  
        textinfo='label+value',   
        textposition='inside'    
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",  
        plot_bgcolor="white",      
        showlegend=False,           
        title={
            'text': "Inventory Usage",  
            'y': 0.97,  
            'x': 0.5,  
            'xanchor': 'center',
            'yanchor': 'top',
        },
        title_font_size=30,          
    )
    st.plotly_chart(fig)



def daily_orders():
    # Fetch the data for daily orders
    data = do_datanalysis.daily_orders()

    fig = px.line(
        data, 
        x='outdate',  
        y='Orders',  
        line_shape='spline' 
         
    )
  
    fig.update_layout(
        xaxis_title='Date',   
        yaxis_title='Number of Orders',  
        plot_bgcolor='rgba(0,0,0,0)',  
        paper_bgcolor='rgba(0,0,0,0)',  
        title_font_size=30,
        yaxis = dict(color='black'),
        xaxis=dict(
            tickformat='%Y-%m-%d',  
            tickangle=-45,
            title_font=dict(color='#e52020'),
            tickfont=dict(color='#e52020') 
        ),
        title={
            'text': "Daily Order Processing",  
            'y': 0.97,  
            'x': 0.5,  
            'xanchor': 'center',
            'yanchor': 'top',
        }
    )

    st.plotly_chart(fig)



def cost_profit_vis():
    
    data = do_datanalysis.cost_profit()
    values = data.iloc[0]
    labels = data.columns.to_list()

    
    fig = px.pie(
        values=values, 
        names=labels,
        hole=0.5  
       )
    
    custom_colors = ['#e52020', '#316a38'] 
    fig.update_traces(  
        textinfo='label',   
        textposition='inside',
         marker=dict(colors=custom_colors)   
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",  
        plot_bgcolor="white",      
        showlegend=False,           
        title={
            'text': "Cost vs Profit",  
            'y': 0.95,  
            'x': 0.5,  
            'xanchor': 'center',
            'yanchor': 'top',
        },
        title_font_size=30,          
    )
    st.plotly_chart(fig)
#Visualizing daily sale vs orders




# def daily_sale():
#     data = do_datafetch.sales_data()

#     # Create a figure
#     fig1 = go.Figure()

#     # Add bar for "Total Sales" on the primary y-axis
#     fig1.add_trace(
#         go.Bar(
#             x=data["DATE"],
#             y=data["daily_sale"],
#             name="Total Sales",
#             marker_color='blue'
#         )
#     )

#     # Add line plot for "Orders" on the secondary y-axis
#     fig1.add_trace(
#         go.Scatter(
#             x=data["DATE"],
#             y=data["Orders"],
#             name="Orders",
#             marker_color='orange',
#             mode='lines+markers',
#             yaxis="y2"
#         )
#     )

#     # Update layout for dual y-axes and transparent background
#     fig1.update_layout(
#         title={
#             'text': "Daily Sales vs Orders Processed",  
#             'y': 0.95,  
#             'x': 0.5,  
#             'xanchor': 'center',
#             'yanchor': 'top',
#         },
#         title_font_size=35,
#         xaxis=dict(
#             tickformat='%Y-%m-%d',  
#             tickangle=-45) , 
#         xaxis_title="Date",
#         yaxis=dict(
#             title="Total Sales",
#             titlefont=dict(color="blue"),
#             tickfont=dict(color="blue")
#         ),
#         yaxis2=dict(
#             title="Orders",
#             titlefont=dict(color="orange"),
#             tickfont=dict(color="orange"),
#             overlaying="y",
#             side="right"
#         ),
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(0,0,0,0)"
#     )

#     st.plotly_chart(fig1)



def daily_sale():
    data = do_datafetch.sales_data()

    fig1 = go.Figure()

    # Add bar for "Total Sales"
    fig1.add_trace(go.Bar(x=data["DATE"], y=data["daily_sale"], name="Total Sales", marker_color='blue'))

    # Add bar for "Orders"
    fig1.add_trace(go.Bar(x=data["DATE"], y=data["Orders"], name="Orders", marker_color='orange'))

    fig1.update_layout(
        title={
            'text': "Daily Sales vs Orders Processed",  
            'y': 0.95,  
            'x': 0.5,  
            'xanchor': 'center',
            'yanchor': 'top',
        },
        title_font_size=35,
        xaxis_title="Date",
        xaxis = dict( color = "black"),
        yaxis=dict(title = "Values", type="log", color='black'),
        barmode="group",
        bargap=0.2,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig1)
