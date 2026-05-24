import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import date
from components.donut_chart import donut_chart
from services.api_client import get_calories
from mistralai.client import MistralClient
from dotenv import load_dotenv
import os



st.set_page_config(layout="wide",
                   page_title="Health App",
                   page_icon="./images/favicon.png")



st.markdown("""
<style>

.stApp {
    background-color: #FDF0E6; 
    color: #3A3A3A;
}

.stButton > button {
    background-color: #F9C5C4;
    color: #3A3A3A;
    border-radius: 10px;
    border: none;
    padding: 0.5em 1em;
    transition: 0.3s ease;
}

.stButton > button:hover {
    background-color: #F5A3A1;
    color: white;
}

/* Text input */
.stTextInput > div > div > input {
    background-color: #F9C5C4;
    color: #3A3A3A;
    border-radius: 10px;
}

/* Selectbox */
.stSelectbox > div > div {
    background-color: #F9C5C4;
    border-radius: 10px;
}

details {
    background-color: #F9C5C4;
    border-radius: 12px;
    padding: 5px;
    margin-bottom: 10px;
    border: none;
}


details summary {
    color: #FDF0E6;
    font-weight: bold;
    font-size: 16px;
}

/* Expander content */
details p {
    color: #3A3A3A;
}


</style>
""", unsafe_allow_html=True)


def show_dashboard_page():
    col1, col2 = st.columns([1, 1])


    # ----- kolonne 1 -----
    with col1:
        st.title("Daily Board")
        st.subheader("FOODLOG")

        food = st.text_input("What have you eaten today?", width=400,)
        amount = st.text_input("How much? (gram)", width=400)
        meals = st.selectbox("Which meal is it?", ("Breakfast", "Lunch", "Dinner", "Snacks"), width=400)
        file_name = "foodlog.csv"

        if st.button("Save"):

            calories = get_calories(food, amount)

            new_data = {
                "Date": [date.today().isoformat()],
                "Meal":[meals],
                "Food":[food],
                "Gram":[amount],
                "Calories":[calories]
            }

            df_new = pd.DataFrame(new_data)

            if os.path.exists(file_name):
                df_new.to_csv(file_name, mode="a", header=False, index=False)
            else:
                df_new.to_csv(file_name, index=False)

            st.success("Meal saved!")

        if os.path.exists(file_name):

            df = pd.read_csv(file_name)
            
            # det her har jeg sat ind:
            today = date.today().isoformat()
            df_today = df[df["Date"] == today]

            def show_meal_section (meal, df_today):
                st.markdown(f"### {meal} ###")
                meal_rows = df_today[df_today["Meal"] == meal]

                if meal_rows.empty:
                    st.write("No meals added yet.")
                
                for index, row in meal_rows.iterrows():
                    st.write(f"{row['Food']} - {row['Gram']} gram - {row['Calories']} calories")

            show_meal_section("Breakfast", df_today)
            show_meal_section("Lunch", df_today)
            show_meal_section("Dinner", df_today)
            show_meal_section("Snacks", df_today)
            
    # ----- kolonne 2 -----
    with col2:
        st.markdown("### ")

        daily_goal = 2100
        total_calories = 0

        if os.path.exists(file_name):
            df = pd.read_csv(file_name)
            
            today = date.today().isoformat()
            df_today = df[df["Date"] == today]
            
            total_calories = df_today["Calories"].sum()

        fig = donut_chart(total_calories, daily_goal)
        st.pyplot(fig)
        
    # ----- mistral generator -----
        
        load_dotenv()

        from components.Recipes2 import show_recipes2

        client = MistralClient(
            api_key=os.getenv("MISTRAL_API_KEY")
        )


        show_recipes2(client)




selected = option_menu(
    menu_title=None,
    options=["Dashboard", "Weekly update", "Contact", "About"],
    icons=["house-fill", "calendar-check-fill", "envelope-fill", "info-circle-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
    "container": {"background-color": "#F9C5C4"},
    "nav-link": {"font-size": "16px",},
    "nav-link-selected": {"background-color": "#3A3A3A",
                            "color": "#F9C5C4"},  
    }
)
    
if selected == "Dashboard":
    show_dashboard_page()
if selected == "Weekly update":
    from sider.Weekly_update import show_weekly_page
    show_weekly_page()
if selected == "Contact":
    from sider.Contact import show_contact_page
    show_contact_page()
if selected == "About":
    from sider.About import show_about_page
    show_about_page()

