import streamlit as st
import pandas as pd
import numpy as np


st.image("new.jpg")
st.title("Demographics Analysis")

st.subheader("Welcome to our Comprehensive Guide to Global Demographics and Economic Indicators")
text = "In an increasingly interconnected world, understanding the complexities of global demographics and economic indicators is crucial for informed decision-making and strategic planning. Our webpage serves as a comprehensive resource, offering a diverse array of charts and visualizations that illuminate key trends shaping our world today. Here's what you can expect from our site:"

st.write(text)


text2 = "1. **Insightful Analyses:** Explore our collection of charts and visualizations, each accompanied by insightful analysis, to gain a deeper understanding of the demographic and economic landscape of our world."

text3 = "2. **Global Perspective:** We provide a broad view of global demographics and economic indicators, highlighting trends and patterns across countries and regions."

text4 = "3. **Country-Specific Demographics:** Delve into the demographics of specific countries, where we offer detailed analyses and visual representations tailored to each nation. Gain insights into population dynamics, economic trends, and social indicators unique to each country."

text5 = "4. **Focus on India:** As part of our commitment to providing comprehensive insights, we start our exploration with India. Discover the intricate demographics and economic dynamics of one of the world's largest and most diverse countries."

st.write(text2)
st.write(text3)
st.write(text4)
st.write(text5)


st.subheader("Dataset in use")

def load_data():
    df = pd.read_csv("final_demographics_data.csv")
    return df

def fill_missing_data(df):
    df.fillna({
        "Adults (ages 15+) and children (ages 0-14) newly infected with HIV":df["Adults (ages 15+) and children (ages 0-14) newly infected with HIV"].median(),
        "Adults (ages 15-49) newly infected with HIV":df["Adults (ages 15-49) newly infected with HIV"].median(),
        "Arms exports (SIPRI trend indicator values)":df["Arms exports (SIPRI trend indicator values)"].mean(),
        "Arms imports (SIPRI trend indicator values)":df["Arms imports (SIPRI trend indicator values)"].mean(),
        "Automated teller machines (ATMs) (per 100,000 adults)":df["Automated teller machines (ATMs) (per 100,000 adults)"].mean(),
        "Average transaction cost of sending remittances from a specific country (%)":df["Average transaction cost of sending remittances from a specific country (%)"].mean(),
        "Average transaction cost of sending remittances to a specific country (%)":df["Average transaction cost of sending remittances to a specific country (%)"].mean(),
        "Bank capital to assets ratio (%)":df["Bank capital to assets ratio (%)"].mean(),
        "Bank liquid reserves to bank assets ratio (%)":df["Bank liquid reserves to bank assets ratio (%)"].mean(),
        "Bank nonperforming loans to total gross loans (%)":df["Bank nonperforming loans to total gross loans (%)"].mean(),
        "Charges for the use of intellectual property, payments (BoP, current US$)":df["Charges for the use of intellectual property, payments (BoP, current US$)"].mean(),
        "Charges for the use of intellectual property, receipts (BoP, current US$)":df["Charges for the use of intellectual property, receipts (BoP, current US$)"].mean(),
        "Commercial bank branches (per 100,000 adults)":df["Commercial bank branches (per 100,000 adults)"].mean(),
        "Computer, communications and other services (% of commercial service exports)":df["Computer, communications and other services (% of commercial service exports)"].mean(),
        "Computer, communications and other services (% of commercial service imports)":df["Computer, communications and other services (% of commercial service imports)"].mean(),
        "Consumer price index (2010 = 100)":df["Consumer price index (2010 = 100)"].mean(),
        "Domestic credit provided by financial sector (% of GDP)":df["Domestic credit provided by financial sector (% of GDP)"].mean(),
        "Domestic credit to private sector (% of GDP)":df["Domestic credit to private sector (% of GDP)"].mean(),
        "Domestic credit to private sector by banks (% of GDP)":df["Domestic credit to private sector by banks (% of GDP)"].mean(),
        "Employment to population ratio, 15+, female (%) (national estimate)":df["Employment to population ratio, 15+, female (%) (national estimate)"].mean(),
        "Employment to population ratio, 15+, male (%) (national estimate)":df["Employment to population ratio, 15+, male (%) (national estimate)"].mean(),
        "Employment to population ratio, 15+, total (%) (national estimate)":df["Employment to population ratio, 15+, total (%) (national estimate)"].mean(),
        "Employment to population ratio, ages 15-24, female (%) (national estimate)":df["Employment to population ratio, ages 15-24, female (%) (national estimate)"].mean(),
        "Employment to population ratio, ages 15-24, male (%) (national estimate)":df["Employment to population ratio, ages 15-24, male (%) (national estimate)"].mean(),
        "Employment to population ratio, ages 15-24, total (%) (national estimate)":df["Employment to population ratio, ages 15-24, total (%) (national estimate)"].mean(),
        "Final consumption expenditure (% of GDP)":df["Final consumption expenditure (% of GDP)"].mean(),
        "Final consumption expenditure (annual % growth)":df["Final consumption expenditure (annual % growth)"].mean(),
        "Final consumption expenditure (constant 2010 US$)":df["Final consumption expenditure (constant 2010 US$)"].mean(),
        "Final consumption expenditure (constant LCU)":df["Final consumption expenditure (constant LCU)"].mean(),
        "Final consumption expenditure (current LCU)":df["Final consumption expenditure (current LCU)"].mean(),
        "Final consumption expenditure (current US$)":df["Final consumption expenditure (current US$)"].mean(),
        "Fixed broadband subscriptions":df["Fixed broadband subscriptions"].mean(),
        "Fixed broadband subscriptions (per 100 people)":df["Fixed broadband subscriptions (per 100 people)"].mean(),
        "Fixed telephone subscriptions":df["Fixed telephone subscriptions"].mean(),
        "Fixed telephone subscriptions (per 100 people)":df["Fixed telephone subscriptions (per 100 people)"].mean(),
        "GDP (constant 2010 US$)":df["GDP (constant 2010 US$)"].mean(),
        "GDP growth (annual %)":df["GDP growth (annual %)"].mean(),
        "GDP per capita (constant 2010 US$)":df["GDP per capita (constant 2010 US$)"].mean(),
        "GNI (constant 2010 US$)":df["GNI (constant 2010 US$)"].mean(),
        "GNI growth (annual %)":df["GNI growth (annual %)"].mean(),
        "GNI per capita (constant 2010 US$)":df["GNI per capita (constant 2010 US$)"].mean(),
        "High-technology exports (current US$)":df["High-technology exports (current US$)"].mean(),
        "Individuals using the Internet (% of population)":df["Individuals using the Internet (% of population)"].mean(),
        "Military expenditure (% of GDP)":df["Military expenditure (% of GDP)"].mean(),
        "Ratio of female to male labor force participation rate (%) (national estimate)":df["Ratio of female to male labor force participation rate (%) (national estimate)"].mean(),
        "Total reserves (includes gold, current US$)":df["Total reserves (includes gold, current US$)"].mean()},
        inplace=True)
    return df


def main():
    df = load_data()
    st.dataframe(df)
    st.subheader("Filling the missing values")
    st.write("Toggle the button below to fill the missing values in the dataset. the missing values are filled using various statistical information")
    toggle = st.toggle("Fill Missing values")
    if toggle == True:
        final_df = fill_missing_data(df)
        st.dataframe(final_df)

        
    st.subheader("Other datasets in use")    
    with st.expander("Click to expand the datasets"):
        st.subheader("Population distribution of india")
        df_one = pd.read_csv("india_population.csv")
        st.dataframe(df_one,use_container_width=True)
        st.divider()

        st.subheader("Literacy in India")
        df_two = pd.read_csv("literacy.csv")
        st.dataframe(df_two,use_container_width=True)
        st.divider()

        st.subheader("Temperature Variations")
        df_three = pd.read_csv("indian_temp.csv")
        st.dataframe(df_three,use_container_width=True)


main()

