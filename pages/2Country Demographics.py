import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import seaborn as sns
import plotly.express as px
import text


st.image("country.jpg")

st.title("Country Demographics")


def load_data():
    df = pd.read_csv("final.csv")
    return df

# def selected_countries(df):
#     countries_list = df["country"].tolist()
#     selected_country = st.selectbox("Select Country",countries_list)
#     return selected_country

# def compare_chart(df,selected_country):
#     filtered_df = df[df["country"] == selected_country]
#     st.bar_chart(data=filtered_df,x = "country", y = {"Population, male","Population, female"},height = 500, use_container_width=True)

# def age_dependency(data,selected_country):
#     filtered_df = data[data["country"] == selected_country]
#     st.bar_chart(data = filtered_df,x="country", y={"Age dependency ratio, young (% of working-age population)","Age dependency ratio, old (% of working-age population)"},height = 500 , use_container_width = True)

# def plot_countries(data):
#     filtered_df = data[data["country"] == selected_country]
#     labels = ["country"]

def first():
    df = pd.read_csv("temperature.csv")
    st.dataframe(df)
    st.line_chart(df, x="Country", y="AverageTemperature",use_container_width=True)

def gdp():
    # Load the dataset
    df = pd.read_csv("final.csv")

    # Title for the app
    st.subheader('GDP per Capita Analysis by Region')
    st.write(text.gdp)
    # Bar chart
    fig_bar = px.bar(df, x='Region', y='GDP per capita (constant 2010 US$)', title='GDP per Capita by Region',
                     labels={'gdp per capita': 'GDP per Capita', 'region': 'Region'})
    fig_bar.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig_bar, use_container_width=True)

    st.write(text.gdp_d)
    # Box plot
    fig_box = px.box(df, x='Region', y='GDP per capita (constant 2010 US$)', title='GDP per Capita Distribution by Region',
                     labels={'GDP per capita (constant 2010 US$)': 'GDP per Capita', 'Region': 'Region'})
    st.plotly_chart(fig_box, use_container_width=True)
    st.divider()

def unemploy(df):
    # Plotting
    st.subheader('Unemployment Rates by Country')
    st.write(text.un_country)

    # Creating a bar chart using Streamlit's native chart elements
    st.bar_chart(df.set_index('country')['Unemployment, total (% of total labor force) (modeled ILO estimate)'])

def woman_emp(df):
    # Title for the app
    st.subheader('Women Business and the Law Index Score')
    st.write(text.woman_bus)
    # Create a bar chart using Plotly Express
    fig = px.bar(df, x='Region', y='Women Business and the Law Index Score (scale 1-100)',
                 title='Women Business and the Law Index Score by Region',
                 labels={'Women Business and the Law Index Score (scale 1-100)': 'Index Score', 'region': 'Region'})
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True)


# Geographical representation of countries population and gdp
def geographical_representation_of_population_gdp(df):
    st.subheader("Countries metrics by Population and GDP")

    latitudes = [36.7372, -34.6037, -35.2809, 48.2082, 23.8103,
    53.9045, 50.8503, -15.7942, 45.4215, -33.4489,
    39.9042, 4.7109, 55.6761, 0.1807, 30.0444,
    9.0208, 48.8566, 52.5200, 5.6037, 37.9838,
    28.6139, -6.2088, 33.3152, 53.3498, 31.7683,
    41.9028, 35.6895, 51.1694, 1.2921, 3.1390,
    19.4326, 34.0209, 27.7172, 52.3676, 9.0765,
    59.9139, 33.6844, -12.0464, 14.5995, 52.2297,
    38.7223, 44.4268, 24.7136, 1.3521, -25.7469,
    40.4168, 6.9271, 59.3293, 46.8182, 13.7563,
    36.8065, 39.9334, 0.3476, 50.4501, 24.4539,
    38.9072, 21.0278]

    longitudes = [3.0863, -58.3816, 149.1300, 16.3738, 90.4125,
    27.5615, 4.3517, -47.8825, -75.6910, -70.6693,
    116.4074, -74.0721, 12.5683, -78.4678, 31.2357,
    38.7469, 2.3522, 13.4050, -0.1870, 23.7275,
    77.2090, 106.8456, 44.3661, -6.2603, 35.2137,
    12.4964, 139.6917, 71.4491, 36.8219, 101.6869,
    -99.1332, -6.8416, 85.3240, 4.9041, 7.3986,
    10.7522, 73.0479, -77.0428, 120.9842, 21.0122,
    -9.1393, 26.1025, 46.6753, 103.8198, 28.1879,
    -3.7038, 79.8612, 18.0686, 8.2275, 100.5018,
    10.1815, 32.8597, 32.5825, 30.5234, 54.3773,
    -77.0369, 105.8342]

    # Adding the latituse and longitude into the existing dataframe
    df["latitudes"] = latitudes
    df["longitudes"] = longitudes

    # Sidebar for selecting metric
    selected_metric = st.selectbox("Select Metric", ['Population', 'GDP'])

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

# Population growth by each country
def population_growth_by_country(df):
    st.subheader("Population growth by each country")

    st.area_chart(
        df, x="country", y=["Population growth (annual %)"], height = 600, use_container_width =True
    )
    
def main():
    df = load_data()
    gdp()
    unemploy(df)
    woman_emp(df)
    geographical_representation_of_population_gdp(df)
    population_growth_by_country(df)
    # df = load_data()
    # selected_country = selected_countries(df)

    # compare_chart(df,selected_country)
    # age_dependency(df,selected_country)

main()