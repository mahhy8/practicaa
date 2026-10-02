import streamlit as st
import datetime
import pandas as pd

today=datetime.date.today()
today_date=st.date_input('current date', today)
st.success('Current date: '%s '%(today_date)')

titanic_data= pd.read.csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")

st.header("Dataset")
if agree:
    st.dataframe(titanic_data)
    selected_town=st.radio("select embark Town", )titanic_data['embark_town'.unique()]
st.write("Selected embark Town", selected_town
)