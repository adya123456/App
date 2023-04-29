import streamlit as st
num = st.slider("choose your number", 1,100)
st.write("sqaure of ", num, 'is', num **2)
