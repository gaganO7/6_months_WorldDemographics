import pandas as pd
import numpy as np
import streamlit as st
import plotly.figure_factory as ff

from streamlit_echarts import st_echarts
from pyecharts.faker import Faker
from streamlit_echarts import JsCode
from streamlit_echarts import Map

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from streamlit_echarts import st_pyecharts
import random,json



st.image("world.jpg")

st.title('World Demographics')


text1 = "A bar chart comparing male population to female population can provide several insights into the gender distribution within a population. Here's what it can tell you:  \n\n Gender Imbalance : The most obvious insight is whether there is a gender imbalance within the population. If one bar is significantly taller than the other, it indicates a disproportionate number of males or females in comparison to the other gender."
 
text2 = "The age dependency ratio compares the number of dependent individuals (typically children and elderly people) to the number of working-age individuals in a population. When specifically examining the age dependency ratio for males, it focuses on the dependency of males on the working-age male population.\n\n Economic Burden: A higher age dependency ratio for males suggests that a larger proportion of males, compared to females, are dependent on the working-age male population for support. This can indicate a heavier economic burden on the working-age male population to provide for the needs of dependents."

text3 = "Charts displaying the average transaction cost of sending and receiving remittances to a specific country as percentages provide insights into the costs associated with international money transfers. Here's what these charts can reveal: \n\n Cost Comparison: By comparing the average transaction costs of sending and receiving remittances to a specific country, you can assess the relative expense of sending money from one location to another. If one percentage is higher than the other, it indicates that either sending or receiving money in that particular country is more costly. \n\n Remittance Corridors: Analyzing transaction costs for specific countries can highlight differences in remittance corridors. Some countries or regions may have more competitive markets or better-developed financial systems, resulting in lower transaction costs, while others may face challenges such as regulatory barriers or limited access to formal financial services. " 

text4 = "A bar chart depicting the gold reserves of different countries provides insights into the distribution and comparative holdings of gold across the world. Here's what such a chart can reveal: \n\n Wealth and Economic Power: Countries with large gold reserves often signal economic strength and stability. They may have accumulated gold reserves as a hedge against currency fluctuations, economic uncertainties, or geopolitical risks. The bar chart can visually represent which countries possess significant wealth in terms of gold holdings.\n\n Monetary Policy and Stability: Central banks often hold gold reserves as part of their monetary policy and to maintain financial stability. High gold reserves can indicate a country's confidence in its currency and its ability to weather financial crises. Conversely, low gold reserves may suggest vulnerability to economic shocks."

def load_data():
    df = pd.read_csv("final.csv")
    return df

def age_dependency_male(df):
    st.line_chart(data=df, x= "Age dependency ratio (% of working-age population)", y = "Population, male", height = 500 )

def population_trends(data):
    st.bar_chart(data, x="country", y={"Population, female","Population, male"}, height = 600 , use_container_width = True )
    
def stability_trends(data):
    st.bar_chart(data,x="country",y=["Average transaction cost of sending remittances from a specific country (%)","Average transaction cost of sending remittances to a specific country (%)"], height = 600)

def reserve(data):
    st.bar_chart(data,x="country",y="Total reserves (includes gold, current US$)", height=500)

def age_dependency_country(data):
    st.scatter_chart(data=data, x="country", y="Age dependency ratio (% of working-age population)", color="Region", height=600, use_container_width=True)


def region_gdp(df):
    # Initialize an empty list to hold dictionaries
    data_list = []

    # Iterate over the rows and construct dictionaries
    for index, row in df.iterrows():
        data_list.append({"value":row["Military expenditure (% of GDP)"],"name":row["Region"]})

    options = {
        "title": {"text": "Military Expenditure", "subtext": "Military expenditure of the countries according to their GDP %", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "bottom",},
        "series": [
            {
                "name": "Military Expenditure",
                "type": "pie",
                "radius": "70%",
                "data": [
                   
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 50,
                        "shadowOffsetX": 1,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }

    options["series"][0]["data"] = data_list

    st_echarts(
        options=options, height="700px",
    )

def main():
    df = load_data()

    st.divider()
    st.subheader("Age dependency Ratio")
    st.write(text2)
    age_dependency_male(df)
   
    st.divider()
    st.subheader("Region census")
    st.write(text4)
    age_dependency_country(df)

    st.divider()
    st.subheader("Population Trend")
    st.write(text1)
    population_trends(df)
    
    st.divider()
    st.subheader("Remittances transaction cost")
    st.write(text3)
    stability_trends(df)
    
    st.divider()
    st.subheader("Gold Reserves")
    st.write(text4)
    reserve(df)

    region_gdp(df)

    
main()


