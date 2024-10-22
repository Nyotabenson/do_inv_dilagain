import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

import do_datanalysis

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
        paper_bgcolor="green",  
        plot_bgcolor="white",      
        showlegend=False,           
        title={
            'text': "Inventory Usage Pie Chart",  
            'y': 0.95,  
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
        plot_bgcolor='white',  
        paper_bgcolor='green',  
        title_font_size=30,    
        xaxis=dict(
            tickformat='%Y-%m-%d',  
            tickangle=-45  
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
