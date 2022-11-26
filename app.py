import streamlit as st
from datetime import date 

st.title("Hello Streamlit App")

st.header("My name is egezon and this is my fisrt deployed app")

today = date.today()
st.write(today)