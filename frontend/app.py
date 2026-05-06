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

