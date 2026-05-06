import streamlit as st
from components.donut_chart import donut_chart


st.title("This is the dashbord page")

fig = donut_chart(600, 1610)

st.pyplot(fig)
