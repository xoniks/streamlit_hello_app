import streamlit as st
from datetime import date, datetime

st.title("Hello Streamlit App")

st.header("My name is egezon and this is my fisrt deployed app")

today = date.today()
time_now = datetime.now()
st.write(today)
st.write(time_now)