import imp


import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Instructions",
    page_icon='📜',
    layout="wide"
)


st.title("Instructions :- ")

st.write("1) First Your data file is must be a type of CSV/EXCELL.")
st.write("2) The data file must contain atleast 6 comumns.")
st.write("3) The main 6 columns are : Order ID, Product name, Quantity, Price, Order Date, Address.")
st.write("4) Also take care of all the namings of the columns (Because it is case sensetive) , and also the type of values in the rows.")
st.header("Sample Data :- ")
df = pd.read_csv("all_months_sales.csv");
df = df.dropna()
df['Quantity'] = df["Quantity"].astype('int32')
st.write(df.head())

st.info("Still if you face any difficulty feel free to contact me!!")