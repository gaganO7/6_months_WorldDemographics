import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fill missing data
def fill_missing_data(df):
    # Fill missing numerical data with mean
    numerical_cols = df.select_dtypes(include=np.number).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
    # Fill missing categorical data with mode
    categorical_cols = df.select_dtypes(include='object').columns
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
    return df

# Function to select columns
def select_columns(df, columns):
    return df[columns]

# Function to generate chart
def generate_chart(df, chart_type, x_column, y_column, hue_column=None):
    if chart_type == 'Line Plot':
        st.line_chart(df , x = x_column , y = y_column , color  = hue_column , use_container_width = True)
    elif chart_type == 'Bar Plot':
        st.bar_chart(df , x = x_column , y = y_column , color  = hue_column , use_container_width = True)
    elif chart_type == 'Histogram':
        st.bar_chart(df , x = x_column , y = y_column , color  = hue_column , use_container_width = True)

# Main function
def main():
    st.title('Advanced Data Visualizations')

    # File upload
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Display uploaded data
        st.write('Uploaded Data:')
        st.dataframe(df , use_container_width = True)

        # Fill missing data
        if st.checkbox('Fill Missing Data'):
            df = fill_missing_data(df)
            st.write('Data after filling missing values:')
            st.dataframe(df,use_container_width = True)

        # Select columns
        columns = st.multiselect('Select Columns', df.columns)
        if columns:
            df = select_columns(df, columns)
            st.write('Data after selecting columns:')
            st.dataframe(df , use_container_width = True)

        # Choose chart options
        st.subheader('Chart Options:')
        chart_type = st.selectbox('Select Chart Type', ['Line Plot', 'Bar Plot', 'Histogram'])

        x_column = st.selectbox('Select X Axis Column', df.columns)
        y_column = st.selectbox('Select Y Axis Column', df.columns)

        hue_column = None
        if st.checkbox('Group by Hue'):
            hue_column = st.selectbox('Select Hue Column', df.columns)

        if st.button('Generate Chart') and chart_type:
            generate_chart(df, chart_type, x_column, y_column, hue_column)

if __name__ == "__main__":
    main()
