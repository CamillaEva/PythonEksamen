import streamlit as st
import matplotlib.pyplot as plt
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

    st.markdown("### Morgenmad")
    st.write("100 g kyllingebryst")
    st.write("30 g mayonnaise")

    st.markdown("### Frokost")
    st.write("100 g kyllingebryst")

    st.markdown("### Aftensmad")
    st.write("...")


#kolonne 2
with col2:
    st.markdown("### ")

    percent = 50

    st.progress(percent / 100)
    st.write(f"**{percent}%** af dine daglige kcal brugt")


def donut(percent):
    fig, ax = plt.subplots()
    ax.pie([percent, 100-percent], startangle=90)
    ax.axis("equal")
    return fig

st.pyplot(donut(50))



# ----- Mistral -----

from components.recipes import show_recipes

load_dotenv()

client = MistralClient(
    api_key=os.getenv("MISTRAL_API_KEY")
)

st.title("healthy recipes for you")

show_recipes(client)