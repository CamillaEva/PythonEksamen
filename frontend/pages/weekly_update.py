import streamlit as st
from components.bar_chart import weekly_calorie_chart

st.title("Weekly update")

days = ["Man", "Tir", "Ons", "Tor", "Fre", "Lør", "Søn"]
values = [1610, 1555, 1880, 1532, 1969, 2000, 1545]

fig = weekly_calorie_chart(days, values)

st.pyplot(fig)