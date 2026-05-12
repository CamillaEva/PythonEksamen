import streamlit as st

def show_recipes(client):

    # ----- GENERATE RECIPES -----

    if "recipes" not in st.session_state:

        prompt = """
        Give me 3 healthy high-protein recipe titles.
        Return ONLY the titles, one per line.
        """

        response = client.chat(
            model="mistral-small-latest",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        answer = response.choices[0].message.content

        recipes = [r.strip() for r in answer.split("\n") if r.strip()]

        st.session_state["recipes"] = recipes


    # ----- SHOW TITLES -----

    st.subheader("Choose a recipe")

    for recipe in st.session_state["recipes"]:

        if st.button(recipe):

            detail_prompt = f"""
            You are a nutrition expert.

            For this recipe:
            {recipe}

            Give:
            - full recipe
            - calories
            - protein amount
            """

            response = client.chat(
                model="mistral-small-latest",
                messages=[{
                    "role": "user",
                    "content": detail_prompt
                }]
            )

            st.session_state["selected_recipe"] = response.choices[0].message.content


    # ----- SHOW DETAILS -----

    if "selected_recipe" in st.session_state:

        st.subheader("Recipe details")
        st.write(st.session_state["selected_recipe"])