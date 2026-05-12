import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from components.donut_chart import donut_chart
from services.api_client import get_calories
from mistralai.client import MistralClient
from dotenv import load_dotenv
import os



st.set_page_config(layout="wide")

col1, col2 = st.columns([2, 1])


#kolonne 1
with col1:
    st.title("Daily Board")
    st.subheader("FOODLOG")

    food = st.text_input("What have you eaten today?")
    amount = st.text_input("How much? (gram)")
    meals = st.selectbox("Which meal is it?", ("Breakfast", "Lunch", "Dinner", "Snacks"))
    file_name = "foodlog.csv"

    if st.button("Save"):

        calories = get_calories(food, amount)

        new_data = {
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

        #Morgenmad
        st.markdown("### Breakfast")
        for index, row in df[df["Meal"] == "Breakfast"].iterrows():
            st.write(f"{row["Food"]} - {row["Gram"]} gram")

        #Frokost
        st.markdown("### Lunch")
        for index, row in df[df["Meal"] == "Lunch"].iterrows():
            st.write(f"{row["Food"]} - {row["Gram"]} gram")

        #Aftensmad
        st.markdown("### Dinner")
        for index, row in df[df["Meal"] == "Dinner"].iterrows():
            st.write(f"{row["Food"]} - {row["Gram"]} gram")

        #Snacks
        st.markdown("### Snacks")
        for index, row in df[df["Meal"] == "Snacks"].iterrows():
            st.write(f"{row["Food"]} - {row["Gram"]} gram")
   

#kolonne 2
with col2:
    st.markdown("### ")

    daily_goal = 2100
    total_calories = 0

    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
        total_calories = df["Calories"].sum()

    fig = donut_chart(total_calories, daily_goal)
    st.pyplot(fig)


st.markdown("## FEEDBACK")

st.info("""
Du ligger på et moderat kalorieindtag i dag.
Prøv at tilføje mere protein til aftensmad.
""")

# ----- MISTRAL -----

load_dotenv()

client = MistralClient(
    api_key=os.getenv("MISTRAL_API_KEY")
)

st.title("healthy recipes for you")

user_prompt = st.text_area("write your prompt here")

if st.button("send"):
    if user_prompt:
        with st.spinner("generating response..."):
            try: 
                response = client.chat(
                    model="mistral-small-latest", 
                    messages=[{
                        "role": "user",
                        "content": user_prompt
                        }]
                    )
                
                answer = response.choices[0].message.content

                st.subheader("response")

                st.write(answer)

            except Exception as e:
                st.error(f"Error: {e}")

