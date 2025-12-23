import streamlit as st
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Analyze Your Data",layout="wide",page_icon="🐼")

st.title("🐼Analyze Your Data")
st.write("Upload A **CSV** File and Explore Your Data Interactively")

# for uploading csv file
uploaded_file=st.file_uploader("📁Upload Your CSV File", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        # convert boolean column as string
        bool_cols = df.select_dtypes(include=['bool']).columns
        df[bool_cols] = df[bool_cols].astype(str)
    except Exception as e:
        st.error("Could not read the file. Please upload a CSV file again")
        st.exception(e)
        st.stop()

    st.success("✅File Uploaded Successfully!")
    st.write("**Preview of Data**")
    st.dataframe(df.head())

    st.write("**🔍Data Overview**")
    st.write("Number Of Rows: ", df.shape[0])
    st.write("Number Of Columns: ", df.shape[1])
    st.write("Number Of Missing Values: ", df.isnull().sum().sum())    
    st.write("Number Of Duplicate Record", df.duplicated().sum())

    st.write("**ℹ️Complete Summary Of Dataset**")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()
    st.text(info)

    st.write("**📈Statistical Summar of Dataset**")
    st.dataframe(df.describe())

    st.write("**📈Statistical Summar of Non Numerical Features**")
    st.dataframe(df.describe(include='object'))
    
    st.write("**🕵️Select Your Desired Columns**")
    column = st.multiselect("Choose Columns", df.columns.tolist())
    st.write("**📝Preview**")
    if column:
        st.dataframe(df[column].head())
    else:
        st.info("No Columns Selected. Showing Full Dataset")
        st.dataframe(df.head())