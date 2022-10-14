//from tkinter import Y
from turtle import position
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import time

st.set_page_config(
    page_title="ANALYZER",
    page_icon='📊',
    layout="wide"
)

st.success("Note :- If you face any difficulty while performing some task please go through the instructions page once.")
def igp(Dataframe):
    col1, col2 = st.columns(2)
    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val,width=150,height=600)
    st.plotly_chart(plot, use_container_width=True)
def getid(dfObj, value):
    listOfPos = list()
    result = dfObj.isin([value])
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    return listOfPos

st.header("ANALYZER")

input_file = st.file_uploader( label="Upload SALES_DATA.CSV", accept_multiple_files=False, type=['csv', 'xlsx'], key = "Uploaded File" )
if st.session_state["Uploaded File"] is None:
    st.info("Upload the data file first to start")
    st.stop()

df = pd.read_csv(input_file)
df = df.dropna()
df['Quantity'] = df['Quantity'].astype('int32')
choice = st.selectbox("Select a task",[" ","Display my data","Which Month has Maximum sale ?","At what time there are maximum orders taken ?","Which City has maximum Sales ?","Which product sold out the most ?","Plot Graphs"])
# all_data = df
if(choice == " "):
    st.write("Select a task to start")
elif(choice == "Display my data"):
    with st.spinner('Please wait.... We are fetching some information from your data!!!'):
        time.sleep(2)
    st.info("Your Data :-")
    # my_bar = st.progress(0)
    # for i in range(5):
    #     time.sleep(1)
    #     my_bar.progress((i+1)*10)
    st.write(df.head())
elif(choice == "Which Month has Maximum sale ?"):
    with st.spinner('Please wait.... We are fetching some information from your data!!!'):
        time.sleep(2)
    all_data = df
    nan_df = all_data[all_data.isna().any(axis=1)]
    all_data = all_data.dropna()
    all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
    dt_format = st.selectbox("Please Select the Date-time format of your Data",[" ","DD/MM/YY","MM/DD/YY"]);
    if(dt_format == " "):
        st.info("Please select the format to procced further , If you won't select the correct format it might affect the result or can give error!")
        st.stop()
    if(dt_format == "DD/MM/YY"):
        all_data['Month'] = all_data['Order Date'].str[3:5];
    else:
        all_data['Month'] = all_data['Order Date'].str[0:2];

    all_data['Month'] = all_data['Month'].astype('int32')
    all_data['sales'] = all_data['Quantity'].astype('int32')*all_data['Price'].astype('float32')
    sales_sum = all_data.groupby('Month').sum()
    mx_months = getid(sales_sum,sales_sum['sales'].max())
    # st.write(mx_months)
    for ap in range(len(mx_months)):
        if(mx_months[ap][0] == 1):
            st.success("Best months for sales is :- " + "January")
            break;
        elif(mx_months[ap][0] == 2):
            st.success("Best months for sales is :- " + "February")
            break;
        elif(mx_months[ap][0] == 3):
            st.success("Best months for sales is :- " + "March")
            break;
        elif(mx_months[ap][0] == 4):
            st.success("Best months for sales is :- " + "April")
            break;
        elif(mx_months[ap][0] == 5):
            st.success("Best months for sales is :- " + "May")
            break;
        elif(mx_months[ap][0] == 6):
            st.success("Best months for sales is :- " + "June")
            break;
        elif(mx_months[ap][0] == 7):
            st.success("Best months for sales is :- " + "July")
            break;
        elif(mx_months[ap][0] == 8):
            st.success("Best months for sales is :- " + "Augest")
            break;
        elif(mx_months[ap][0] == 9):
            st.success("Best months for sales is :- " + "September")
            break;
        elif(mx_months[ap][0] == 10):
            st.success("Best months for sales is :- " + "October")
            break;
        elif(mx_months[ap][0] == 11):
            st.success("Best months for sales is :- " + "November")
            break;
        elif(mx_months[ap][0] == 12):
            st.success("Best months for sales is :- " + "December")
            break;
    # sales_sum.columns.get_loc(2475727.727608204)
    st.success("And the sales in this month is :-   " + str(sales_sum['sales'].max()) + "$")
    months = [];
    # cities = [City for City ,  df in all_data.groupby('City')]
    # months = range(1,13)
    months = [Month for Month, df in all_data.groupby('Month')]
    st.header('Plot of Data')
    st.info("X = Month number")
    st.info("Y = Total sales in that month")
    plot = px.scatter(df, x=months, y=sales_sum['sales'],width=150,height=600)
    st.plotly_chart(plot, use_container_width=True)
    # fig, ax = plt.subplots(1,1)
    # ax.scatter(x=months, y=sales_sum['sales'])
    # ax.set_xlabel('Months')
    # ax.set_ylabel('Sales')
    # st.pyplot(fig)
    # st.write("\n\n")
    st.write("REPORT :-")
    st.write(sales_sum)

elif(choice  == "At what time there are maximum orders taken ?"):
    ch = st.radio("Is your data contain the time in column Order Date ",[' ','YES','NO'])
    if(ch == ' '):
        st.info("Please choose the option to procced further")
        st.stop()
    elif(ch == 'NO'):
        st.error("This Task is not performable on you data!!")
        st.stop()
    else:
     dataa = df
     timee = df
     with st.spinner('Please wait.... We are fetching some information from your data!!!'):
         dataa['Order Date'] = pd.to_datetime(dataa['Order Date'])
        #  time.sleep(2)
     timee['Hour'] = dataa['Order Date'].dt.hour
     hours = [hour for hour,df in dataa.groupby('Hour')]
     hours_quantity =  dataa.groupby('Hour').sum('Quantity')
 
 
     hour_sum = hours_quantity['Quantity'].max()
     mx_hour= getid(hours_quantity,hour_sum)
     st.success("At hour : " + str(mx_hour[0][0]) + " , There are maximum order taken");
 
     st.header('Plot of Data')
     st.info("X = Hour")
     st.info("Y = No of orders taken in that hour")
     # st.write(timee.groupby('Hour').count())
     plot = px.scatter(df, x=hours, y=hours_quantity['Quantity'],width=150,height=600)
     st.plotly_chart(plot, use_container_width=True)
     st.write(hours_quantity)
     st.write("REPORT :- ")
     st.write(hours_quantity)

elif(choice  == "Which product sold out the most ?"):
    with st.spinner('Please wait.... We are fetching some information from your data!!!'):
        time.sleep(2)
    alld = df;
    product_grp = alld.groupby('Product name').sum('Quantity')
    mx_product = getid(product_grp,product_grp['Quantity'].max())
    # st.write(mx_product)
    for ap in range(len(mx_product)):
        st.success("Product " + mx_product[ap][0] + " Sold out the most , and the total quantity is  =  " + str(int(product_grp['Quantity'].max())))
    products = [Product_name for Product_name ,  df in product_grp.groupby('Product name')]

    x_axis_val =  products
    y_axis_val =  product_grp['Quantity']

    st.header('Plot of Data')
    st.info("X = Product name")
    st.info("Y = Total Quantity of Product")
    plot = px.scatter(df, x=x_axis_val, y=y_axis_val,width=150,height=600)
    st.plotly_chart(plot, use_container_width=True)

    # fig, ax = plt.subplots(1,1)
    # ax.scatter(x=products, y=product_grp['Quantity'])
    # ax.set_xlabel('Product name')
    # ax.set_ylabel('Quantity')

    st.write("REPORT :-")
    st.write(product_grp)
    # st.pyplot(fig)



elif(choice == "Plot Graphs"):
    with st.spinner('Please wait.... We are fetching some information from your data!!!'):
        time.sleep(2)
    igp(df)


    
else:
    with st.spinner('Please wait.... We are fetching some information from your data!!!'):
        time.sleep(2)
    data = df
    data = data.dropna()
    data['City'] = data['Address'].apply(lambda x : x.split(',')[1] + '(' + x.split(',')[2] + ')')
    data['sales'] = data['Quantity'].astype('int32')*data['Price'].astype('float32')
    city_sales = data.groupby('City').sum('Sales')
    cities = [City for City ,  df in data.groupby('City')]
    mx_city = getid(city_sales,city_sales['sales'].max())
    # st.info("City " + mx_city[0] + " Has the highest sale")
    for ap in range(len(mx_city)):
        st.success(mx_city[ap][0] + "  City  Has the maximum Sales and the amount of sales is " + str(city_sales['sales'].max()) + "$.")
    st.header('Plot of Data')
    plot = px.scatter(df, x=cities, y=city_sales['sales'],width=150,height=600)
    st.info("X = City Name")
    st.info("Y = Total Sales in that City")
    st.plotly_chart(plot, use_container_width=True)
    # fig, ax = plt.subplots(1,1)
    # ax.scatter(x=cities, y=city_sales['sales'])
    # ax.set_xlabel('City')
    # ax.set_ylabel('Sales')
    # st.pyplot(fig)
    # st.write("\n\n")
    st.write("REPORT :-")
    st.write(city_sales)
