import pandas as pd
import numpy as np
import streamlit as st
import altair as alt


#Example Galary
#https://altair-viz.github.io/gallery/simple_bar_chart.html

energy_source = pd.DataFrame({
    "EnergyType": ["Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas"],
    "Price ($)":  [150,73,15,130,80,20,170,83,20],
    "Date": ["2022-1-23", "2022-1-30","2022-1-5","2022-2-21", "2022-2-1","2022-2-1","2022-3-1","2022-3-1","2022-3-1"]
    })

option = st.selectbox(
     'Streamlit Bar Chart Tutorial',
     ('Streamlit Built-in Bar Chart', 'Altair Chart with Axis Labels','Altair Chart With Stacked Bars','Altair Bar Chart Horizontal','Altair Bar Chart Sort','Altair Bar Chart with Custom Colors'))

if option == 'Streamlit Built-in Bar Chart':
    ""
    "Energy Costs By Month"
    chart_data = pd.DataFrame(
     [10,13, 11],
     columns=["Energy Costs"])

    st.bar_chart(chart_data)
    
    code = '''"Energy Costs By Month"
    chart_data = pd.DataFrame(
     [10,13, 11],
     columns=["Energy Costs"])
     
    st.bar_chart(chart_data)
     '''
    st.code(code, language='python')

elif option == 'Altair Chart with Axis Labels':
    "Energy Costs By Month"
    source = pd.DataFrame({
        'Price ($)': [10, 15, 20],
        'Month': ['January', 'February', 'March']
     })
 
    bar_chart = alt.Chart(source).mark_bar().encode(
        y='Price ($):Q',
        x='Month:O',
    )
 
    st.altair_chart(bar_chart, use_container_width=True)

    code = '''  "Energy Costs By Month"
    source = pd.DataFrame({
        'Price ($)': [10, 15, 20],
        'Month': ['January', 'February', 'March']
    })
 
    bar_chart = alt.Chart(source).mark_bar().encode(
        y='Price ($)',
        x='Month',
    )
    st.altair_chart(bar_chart, use_container_width=True)
     '''
    st.code(code, language='python')
elif option == 'Altair Bar Chart with Custom Colors':
    domain = ["Electricity", "Gasoline", "Natural Gas"]
    range_ = ["red", "green", "blue"]

    bar_chart = alt.Chart(energy_source).mark_bar().encode(
        x="month(Date):O",
        y="sum(Price ($)):Q",
        color=alt.Color("EnergyType", scale=alt.Scale(domain=domain, range=range_))
    )
    st.altair_chart(bar_chart, use_container_width=True)
 
    code = '''
     "Energy Costs By Month"
    domain = ["Electricity", "Gasoline", "Natural Gas"]
    range_ = ["red", "green", "blue"]

    bar_chart = alt.Chart(energy_source).mark_bar().encode(
        x="month(Date):O",
        y="sum(Price ($)):Q",
        color=alt.Color("EnergyType", scale=alt.Scale(domain=domain, range=range_))
    )
    st.altair_chart(bar_chart, use_container_width=True)
     '''
    st.code(code, language='python')

elif option == 'Altair Chart With Stacked Bars':
   
   

    bar_chart = alt.Chart(energy_source).mark_bar().encode(
        x="month(Date):O",
        y="sum(Price ($)):Q",
        color="EnergyType:N"
    )
    st.altair_chart(bar_chart, use_container_width=True)

    code = '''
     "Energy Costs By Month"
    source = pd.DataFrame({
    "EnergyType": ["Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas"],
    "Price ($)":  [150,73,15,130,80,20,170,83,20],
    "Date": ["2022-1-23", "2022-1-30","2022-1-5","2022-2-21", "2022-2-1","2022-2-1","2022-3-1","2022-3-1","2022-3-1"]
    })

    bar_chart = alt.Chart(source).mark_bar().encode(
        x="month(Date):O",
        y="sum(Price ($)):Q",
        color="EnergyType:N"
    )
    st.altair_chart(bar_chart, use_container_width=True)'''
    st.code(code, language='python')
elif option == 'Altair Bar Chart Horizontal':
    "Altair Bar Chart Horizontal"
  
    bar_chart = alt.Chart(energy_source).mark_bar().encode(
        y="month(Date):O",
        x="sum(Price ($)):Q",
        color="EnergyType:N"
    )
    st.altair_chart(bar_chart, use_container_width=True)

    code = ''' 
    "Energy Costs By Month"
    source = pd.DataFrame({
    "EnergyType": ["Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas"],
    "Price ($)":  [150,73,15,130,80,20,170,83,20],
    "Date": ["2022-1-23", "2022-1-30","2022-1-5","2022-2-21", "2022-2-1","2022-2-1","2022-3-1","2022-3-1","2022-3-1"]
    })

    bar_chart = alt.Chart(source).mark_bar().encode(
        y="month(Date):O",
        x="sum(Price ($)):Q",
        color="EnergyType:N"
    )
    st.altair_chart(bar_chart, use_container_width=True)'''
    st.code(code, language='python')

elif option == 'Altair Bar Chart Sort':
    source = pd.DataFrame({
        "Price ($)": [10, 15, 20],
        "Month": ["January", "February", "March"]
 
     })

    bar_chart = alt.Chart(source).mark_bar().encode(
        x="sum(Price ($)):Q",
        y=alt.Y("Month:N", sort="-x")
    )

    st.altair_chart(bar_chart, use_container_width=True)
    
    code = '''
     "Energy Costs By Month"
    source = pd.DataFrame({
        "Price ($)": [10, 15, 20],
        "Month": ["January", "February", "March"]
 
     })

    bar_chart = alt.Chart(source).mark_bar().encode(
        x="sum(Price ($)):Q",
        y=alt.Y("Month:N", sort="-x")
    )

    st.altair_chart(bar_chart, use_container_width=True)'''
    st.code(code, language='python')







