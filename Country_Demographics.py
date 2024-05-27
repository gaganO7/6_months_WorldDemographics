import streamlit as st
import pandas as pd
import data_preprocessing
import plotly.express as px
from streamlit_echarts import st_echarts
import plotly.graph_objs as go
import pydeck as pdk
import numpy as np
import math
import altair as alt
import folium

# ------------------------------------------------------------------------------
# Page Configuration
st.set_page_config(
     page_title="Country Demographics",
     page_icon=":earth_asia:",
     layout="wide",
     initial_sidebar_state="expanded"
)

# -------------------------------------------------------------------------------
# GDP and GNI per capita of each country
def gdp_gni_per_capita_by_country(df,selected_country):
    st.subheader("GDP and GNI per capita by Single country")
    
    filtered_data = df[df["country"] == selected_country]

    st.markdown("Selected Country " + " " + selected_country)
    d = alt.Chart(filtered_data).mark_bar().encode(
    alt.X("GDP (constant 2010 US$)", bin=True),
    y='GNI (constant 2010 US$)',
    )

    st.altair_chart(d,use_container_width=True)

#---------------------------------------------------------------------------------
# Population by each country
def country_population(df,selected_country):
    filtered_data = df[df["country"] == selected_country]

    # Area Chart
    st.subheader("Population by each country")
    st.line_chart(
        data=filtered_data,
        x="Population density (people per sq. km of land area)",
        y="Population growth (annual %)",
        height=400
        )

# --------------------------------------------------------------------------------
# Age Dependency Ratio for old,young population for each country
def age_dependency_ratio(df,selected_country):
    st.subheader("Age Dependency By Country")

    # Filter data for selected region
    filtered_data = df[df["country"] == selected_country]

    options = {
        "title":{"text":"Age Dependency","subtext":"Age Dependency By Country","left":"center"},
        "tooltip":{"trigger":"item"},
        "legend":{"orient":"vertical","left":"bottom"},
        "series":[
            {
                "name": "Age Dependency",
                "type":"pie",
                "radius":"50%",
                "data":[
                    {"value":filtered_data["Age dependency ratio, young (% of working-age population)"].values[0],"name":"{a} Young".format(a=selected_country)},
                    {"value":filtered_data["Age dependency ratio, old (% of working-age population)"].values[0],"name":"{b} Old".format(b=selected_country)},
                    {"value":filtered_data["Age dependency ratio (% of working-age population)"].values[0],"name":"{c} Ratio".format(c=selected_country)}
                ],
                "emphasis":{
                    "itemStyle":{
                        "shadowBlur":50,
                        "shadowOffsetX":1,
                        "shadowColor":"rgba(0,0,0,0.5)",
                    }
                }
            }
        ]
    }
    st_echarts(
        options=options,height="700px"
    )

# --------------------------------------------------------------------------------
# Economic Indicators for countries
def economic_indicators(df,selected_country):
    st.subheader("Economic Indicators by Each Country")

    filtered_data = df[df["country"] == selected_country]

    st.scatter_chart(data=filtered_data,x="country",y=[
        "GDP per capita (constant 2010 US$)",
        "GNI per capita (constant 2010 US$)"])

# --------------------------------------------------------------------------------
# Usage of Internet by countries
def usage_of_internet_using_internet(df):
    st.subheader("Internet Usage by individual according to Countries")

    st.scatter_chart(data=df,x="country",y="Individuals using the Internet (% of population)")

# --------------------------------------------------------------------------------
# Geographical representation of countries population and gdp
def geographical_representation_of_population_gdp(df):
    st.subheader("Countries metrics by Population and GDP")

    # Adding the latituse and longitude into the existing dataframe
    df["latitudes"] = data_preprocessing.latitudes
    df["longitudes"] = data_preprocessing.longitudes

    # Sidebar for selecting metric
    selected_metric = st.sidebar.selectbox("Select Metric", ['Population', 'GDP'])

    # Selecting the appropriate column based on selected metric
    if selected_metric == 'Population':
        metric_column = 'Population, total'
    elif selected_metric == 'GDP':
        metric_column = 'GNI (constant 2010 US$)'

    # Plot map using plotly
    fig = px.scatter_geo(df, 
                         lat='latitudes',
                         lon='longitudes',
                         size=metric_column,
                         hover_name='country',
                         projection='natural earth',
                         title=f'Map Visualization - {selected_metric}',size_max=30,
                         width=100,
                         height=650)
    
    # Set layout
    fig.update_geos(showcountries=True, countrycolor="Black", countrywidth=1, showcoastlines=True)

    # Render the map
    st.plotly_chart(fig,use_container_width=True)

# --------------------------------------------------------------------------------
# Military Expenditure of the countries by GDP percentage
def military_expenditure(df):
    st.subheader("Military Expenditure of the Countries by % of GDP")
    
    bars = alt.Chart(df).mark_bar().encode(
        y='Military expenditure (% of GDP)',
        color='Military expenditure (% of GDP)',
        x='count(Military expenditure (% of GDP)):Q'
        )
    st.altair_chart(bars, use_container_width=True)

# --------------------------------------------------------------------------------
# Employment ratio of different countries
def employement_ratio(df):
    st.subheader("Employement ratio of different countries")
    
    # Box Plot
    fig_box = px.box(df,x="country",y="Employment to population ratio, 15+, total (%) (national estimate)",
                     labels={"Employment to population ratio, 15+, total (%) (national estimate)":"Employement to Population Ration Total","country":"Countries"})
    st.plotly_chart(fig_box,use_container_width=True)

# --------------------------------------------------------------------------------
def commercial_services_import_export(df):
    st.subheader("Military services of import and export by countries")

    st.bar_chart(
        df, x="country", y=["Arms exports (SIPRI trend indicator values)", "Arms imports (SIPRI trend indicator values)"], 
    )

# --------------------------------------------------------------------------------
# Population growth by each country
def population_growth_by_country(df,selected_country):
    st.subheader("Population growth by each country")

    st.area_chart(
        df, x="country", y=["Population growth (annual %)"]
    )

def main():
    with st.sidebar:
        selected_country = st.selectbox(
            "Select Country",
            data_preprocessing.processed_df["country"].unique()
        )

    gdp_gni_per_capita_by_country(data_preprocessing.processed_df,selected_country)
    
    st.divider()

    country_population(data_preprocessing.processed_df,selected_country)
    
    st.divider()

    age_dependency_ratio(data_preprocessing.processed_df,selected_country)

    st.divider()

    economic_indicators(data_preprocessing.processed_df,selected_country)

    st.divider()

    usage_of_internet_using_internet(data_preprocessing.processed_df)

    st.divider()

    geographical_representation_of_population_gdp(data_preprocessing.processed_df)

    st.divider()

    military_expenditure(data_preprocessing.processed_df)

    st.divider()

    employement_ratio(data_preprocessing.processed_df)

    st.divider()

    commercial_services_import_export(data_preprocessing.processed_df)

    st.divider()

    population_growth_by_country(data_preprocessing.processed_df,selected_country)
main()


