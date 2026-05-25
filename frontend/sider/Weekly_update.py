from components.bar_chart import bar_chart
import numpy as np
import streamlit as st
import pandas as pd

from services.food_api import get_meals


def show_weekly_page():

    meals_data = get_meals()

    if meals_data:

        df = pd.DataFrame(meals_data)

        df["Date"] = pd.to_datetime(df["Date"])

        last_7_days = df[
            df["Date"] >= (
                pd.Timestamp.today() - pd.Timedelta(days=7)
            )
        ]

        daily_kcal = last_7_days.groupby("Date")[
            "Calories"
        ].sum()

        col1, col2 = st.columns([3, 1])

        avg_kcal = np.mean(daily_kcal.values)

        with col1:

            fig = bar_chart(daily_kcal)

            st.pyplot(fig)

        with col2:

            st.metric(
                "Your weekly average",
                f"{round(avg_kcal, 0)} kcal"
            )

    else:

        st.info("No meal data available yet.")