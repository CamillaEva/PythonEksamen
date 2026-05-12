import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from mistralai.client import MistralClient
from dotenv import load_dotenv
import os



st.set_page_config(layout="wide")

col1, col2 = st.columns([2, 1])


#kolonne 1
with col1:
    st.title("Daily Board")
    st.subheader("FOODLOG")

    meal = st.text_input("Hvad har du spist i dag?")
    amount = st.text_input("Hvor meget? (gram)")
    meals = st.selectbox("Hvilket måltid er det?", ("Morgenmad", "Frokost", "Aftensmad", "Snacks"))
    file_name = "foodlog.csv"

    if st.button("Gem"):
        new_data = {
            "Måltid":[meals],
            "Mad":[meal],
            "Gram":[amount]
        }

        df_new = pd.DataFrame(new_data)

        if os.path.exists(file_name):
            df_new.to_csv(file_name, mode="a", header=False, index=False)
        else:
            df_new.to_csv(file_name, index=False)

        st.success("Måltid gemt!")

    if os.path.exists(file_name):

        df = pd.read_csv(file_name)

        #Morgenmad
        st.markdown("### Morgenmad")
        for index, row in df[df["Måltid"] == "Morgenmad"].iterrows():
            st.write(f"{row["Mad"]} - {row["Gram"]} gram")

        #Frokost
        st.markdown("### Frokost")
        for index, row in df[df["Måltid"] == "Frokost"].iterrows():
            st.write(f"{row["Mad"]} - {row["Gram"]} gram")

        #Aftensmad
        st.markdown("### Aftensmad")
        for index, row in df[df["Måltid"] == "Aftensmad"].iterrows():
            st.write(f"{row["Mad"]} - {row["Gram"]} gram")

        #Snacks
        st.markdown("### Snacks")
        for index, row in df[df["Måltid"] == "Aftensmad"].iterrows():
            st.write(f"{row["Mad"]} - {row["Gram"]} gram")
   

#kolonne 2
with col2:
    st.markdown("### ")

    percent = 50

    st.progress(percent / 100)
    st.write(f"**{percent}%** af dine daglige kcal brugt")


st.markdown("## FEEDBACK")

st.info("""
Du ligger på et moderat kalorieindtag i dag.
Prøv at tilføje mere protein til aftensmad.
""")

def donut(percent):
    fig, ax = plt.subplots()
    ax.pie([percent, 100-percent], startangle=90)
    ax.axis("equal")
    return fig

st.pyplot(donut(50))

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

