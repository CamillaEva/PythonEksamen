import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import date
from components.donut_chart import donut_chart
from services.api_client import get_calories
from mistralai.client import MistralClient
from dotenv import load_dotenv
from services.food_api import (get_meals, save_meal, update_meal, delete_meal)
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

/* Number input */
.stNumberInput input {
    background-color: #F9C5C4;
    color: #3A3A3A;
    border-radius: 10px;
}
    
/* Plus/minus buttons */
.stNumberInput button {
    background-color: #F9C5C4 !important;
    color: #3A3A3A !important;
    border: none !important;
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
        amount = st.number_input("How much? (gram)", width=400)
        meals = st.selectbox("Which meal is it?", ("Breakfast", "Lunch", "Dinner", "Snacks"), width=400)
        

        if st.button("Save"):

            calories = get_calories(food, amount)

            new_data = {
                "Date": date.today().isoformat(),
                "Meal": meals,
                "Food": food,
                "Gram": amount,
                "Calories": calories
            }

            save_meal(new_data)

            st.success("Meal saved!")
            
            meals_data = get_meals()

            if meals_data:

                df = pd.DataFrame(meals_data)
            
            today = date.today().isoformat()
            df_today = df[df["Date"] == today]

            def show_meal_section (meal, df_today, df, file_name):
                st.markdown(f"### {meal} ###")
                meal_rows = df_today[df_today["Meal"] == meal]

                if meal_rows.empty:
                    st.write("No meals added yet.")
                
                for index, row in meal_rows.iterrows():
                    col1, col2, col3 = st.columns([5,1,1])

                    with col1:
                        st.write(
                            f"{row['Food']} - {row['Gram']} gram - {row['Calories']} calories"
                        )

                    with col2:
                        if st.button("Update", key=f"update_{index}"):
                            st.session_state["edit_index"] = index
                    
                    with col3:
                        if st.button("Delete", key=f"delete_{index}"):
                            delete_meal(index)

                            st.success("Meal deleted!")

                            st.rerun()
                            
                
            
            # -------- Update form --------
            if "edit_index" in st.session_state:
                edit_index = st.session_state["edit_index"]
                row = df.loc[edit_index]

                st.markdown("### Update meal")

                updated_food = st.text_input("Food", value=row["Food"])
                updated_gram = st.number_input("Gram", value=row["Gram"])
                updated_meal = st.selectbox("Meal", ["Breakfast", "Lunch", "Dinner", "Snacks"], 
                                             index=["Breakfast", "Lunch", "Dinner", "Snacks"].index(row["Meal"]))
                
                if st.button("Save update"):
                    updated_calories = get_calories(updated_food, updated_gram)

                    updated_data = {
                        "Date": row["Date"],
                        "Meal": updated_meal,
                        "Food": updated_food,
                        "Gram": updated_gram,
                        "Calories": updated_calories
                    }

                    update_meal(edit_index, updated_data)
                    del st.session_state["edit_index"]
                    st.success("Meal updated!")
                    st.rerun()


            show_meal_section("Breakfast", df_today, df, file_name)
            show_meal_section("Lunch", df_today, df, file_name)
            show_meal_section("Dinner", df_today, df, file_name)
            show_meal_section("Snacks", df_today, df, file_name)
            
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
    "container": {"background-color": "#F9C5C4", "padding": "0!important", "max-width": "100%"},
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

