import streamlit as st
import pandas as pd
import numpy as np
import plost as pl
import text 

st.image("india_map.jpg")

text1 = "India, the world's largest democracy and second-most populous country, boasts a rich tapestry of cultures, languages, and traditions. Exploring the demographics of this diverse nation provides valuable insights into its societal fabric and economic landscape."

st.title("Indian Demographics")
st.write(text1)

def load_data():
    df = pd.read_csv("india_population.csv")
    return df


def area_chart_male(df):
	st.area_chart(df, x="State", y=("population_male","total_population"), color = ("#306BAC","#9AD5CA"), height = 600 )

def area_chart_female(df):
	st.area_chart(df, x="State", y=("population_female","total_population"), color=("#A379C9","#9AD5CA"), height = 600 )

def population_trends(data):
    st.bar_chart(data, x="State", y={"population_male","total_population","population_female"}, height = 600 , use_container_width = True )

def temp():
	df = pd.read_csv("indian_temp.csv")
	st.line_chart(df, x="yeat", y="temperature",use_container_width=True)

def literacy():
	df = pd.read_csv("literacy.csv")
	st.line_chart(df,x="State", y="Literacy", height=400 , use_container_width=True)  	

def punjab():
	df = pd.read_csv("pun.csv")
	st.line_chart(df, x="State/Union Territory/District", y="Persons", color="Census Year", height=600, use_container_width=True)


def main():
	df = load_data()
	


	st.subheader("Temperature variations in India over the years")
	st.write(text.temp_chart)
	temp()
	st.divider()
	
	st.subheader("Population in India (state)")
	st.write(text.population_state)
	population_trends(df)
	st.divider()

	st.subheader("Male and Female populations in Indian states")
	st.write(text.male_female)
	area_chart_male(df)
	st.divider()
	area_chart_female(df)
	st.divider()

	st.subheader("Literacy rate in indian states")
	st.write(text.state_literacy)
	literacy()
	st.divider()

	st.subheader("Punjab's population over the years")
	st.write(text.punjab)
	punjab()

	

main()