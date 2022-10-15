import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    page_title="SALES ANALYZER",
    page_icon='📈',
    layout="wide"
)

# 📊
st.title("WELCOME TO SALES ANALYZER")

st.markdown("<p style='text-align: justify;'>Sales Analyzer is a web application that helps you to Analyze your data and to retrive some usefull information from the data.</p>",unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>By this app you can Display some graph with some information.</p>",unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>If you face any difficulty while using this app , Please refer the instructions page.</p>",unsafe_allow_html=True)

with open("project.html",'r') as f:
        pic=f.read();
        components.html(pic, height=450 ,width=600)