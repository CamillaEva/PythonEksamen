import numpy as np
import streamlit as st
import pandas as pd

from components.bar_chart import bar_chart
from services.food_api import get_meals

LAST_X_DAYS = 7


def prepare_daily_kcal(meals_data):
    df = pd.DataFrame(meals_data)

    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    start_date = pd.Timestamp.today().date() - pd.Timedelta(days=LAST_X_DAYS)
    last_days = df[df["Date"] >= start_date]

    return last_days.groupby("Date")["Calories"].sum()


def show_weekly_page():
    meals_data = get_meals()

    if not meals_data:
        st.info("No meal data available yet.")
        return

    daily_kcal = prepare_daily_kcal(meals_data)
    avg_kcal = np.mean(daily_kcal.values)

    col1, col2 = st.columns([3, 1])

    with col1:
        fig = bar_chart(daily_kcal)
        st.pyplot(fig)

    with col2:
        st.metric("Your weekly average", f"{round(avg_kcal, 0)} kcal.")
