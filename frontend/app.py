import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import date
from components.donut_chart import donut_chart
from services.api_client import get_calories
from mistralai.client import MistralClient
from components.recipes import show_recipes
from sider.weekly_update import show_weekly_page
from sider.about import show_about_page
from sider.contact import show_contact_page
from styles.colors import PRIMARY_CHART_COLOR, EDGE_COLOR
from dotenv import load_dotenv
from services.food_api import get_meals, save_meal, update_meal, delete_meal
import os

# Constants
MEAL_TYPES = ["Breakfast", "Lunch", "Dinner", "Snacks"]
DAILY_GOAL_KCAL = 2100
EMPTY_COLUMS = ["Date", "Meal", "Food", "Gram", "Calories"]


# Styling
def load_css():
    with open("./styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Page config
st.set_page_config(
    layout="wide",
    page_title="Health App",
    page_icon="./images/favicon.png",
)

load_css()


# Mistral
def create_mistral_client():
    load_dotenv()
    return MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))


# Data
def create_meals_dataframe(meals_data):
    if meals_data:
        return pd.DataFrame(meals_data)

    return pd.DataFrame(columns=EMPTY_COLUMS)


# Meal sections
def show_meal_section(meal, df_today):
    st.markdown(f"### {meal} ###")

    meal_rows = df_today[df_today["Meal"] == meal]

    if meal_rows.empty:
        st.write("No meals added yet.")

    for index, row in meal_rows.iterrows():
        col1, col2, col3 = st.columns([5, 1, 1])

        with col1:
            st.write(f"{row['Food']} - {row['Gram']} gram - {row['Calories']} calories")

        with col2:
            if st.button("Update", key=f"update_{index}"):
                st.session_state["edit_index"] = index
                st.rerun()

        with col3:
            if st.button("Delete", key=f"delete_{index}"):
                delete_meal(index)
                st.success("Meal deleted!")
                st.rerun()


# Forms
def show_add_meal_form(today):
    st.title("Daily board")
    st.subheader("FOODLOG")

    with st.form("meal_form", clear_on_submit=True, border=False):
        food = st.text_input("What have you eaten today?", width=400)
        gram = st.number_input("How much? (gram)", min_value=0, step=1, width=400)
        meal = st.selectbox("Which meal is it?", MEAL_TYPES, width=400)

        submitted = st.form_submit_button("Save")

        if submitted:
            calories = get_calories(food, gram)

            new_data = {
                "Date": today,
                "Meal": meal,
                "Food": food,
                "Gram": gram,
                "Calories": calories,
            }

            save_meal(new_data)

            st.success("Meal saved!")
            st.rerun()


def show_update_form(df):
    if "edit_index" not in st.session_state:
        return

    edit_index = st.session_state["edit_index"]
    row = df.loc[edit_index]

    st.markdown("### Update meal")
    updated_food = st.text_input("Food", value=row["Food"])
    updated_gram = st.number_input("Gram", min_value=0, step=1, value=int(row["Gram"]))
    updated_meal = st.selectbox("Meal", MEAL_TYPES, index=MEAL_TYPES.index(row["Meal"]))

    if st.button("Save update"):
        updated_calories = get_calories(updated_food, updated_gram)

        updated_data = {
            "Date": row["Date"],
            "Meal": updated_meal,
            "Food": updated_food,
            "Gram": updated_gram,
            "Calories": updated_calories,
        }

        update_meal(edit_index, updated_data)

        del st.session_state["edit_index"]
        st.success("Meal updated!")
        st.rerun()


# Dashboard
def show_dashboard_page():
    meals_data = get_meals()

    df = create_meals_dataframe(meals_data)

    today = date.today().isoformat()

    df_today = df[df["Date"] == today]

    col1, col2 = st.columns([1, 1])

    with col1:
        show_add_meal_form(today)
        show_update_form(df)

        for meal in MEAL_TYPES:
            show_meal_section(meal, df_today)

    with col2:
        st.markdown("###")
        total_calories = df_today["Calories"].sum()

        fig = donut_chart(total_calories, DAILY_GOAL_KCAL)

        st.pyplot(fig)
        client = create_mistral_client()
        show_recipes(client)


# Navigation
selected = option_menu(
    menu_title=None,
    options=["Dashboard", "Weekly update", "Contact", "About"],
    icons=["house-fill", "calendar-check-fill", "envelope-fill", "info-circle-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "background-color": PRIMARY_CHART_COLOR,
            "padding": "0!important",
            "max-width": "100%",
        },
        "nav-link": {
            "font-size": "16px",
        },
        "nav-link-selected": {
            "background-color": EDGE_COLOR,
            "color": PRIMARY_CHART_COLOR,
        },
    },
)

# Routing
if selected == "Dashboard":
    show_dashboard_page()

elif selected == "Weekly update":
    show_weekly_page()

elif selected == "Contact":
    show_contact_page()

elif selected == "About":
    show_about_page()
