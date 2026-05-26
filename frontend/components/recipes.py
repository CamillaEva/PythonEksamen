import streamlit as st

MODEL_NAME = "open-mistral-7b"
RECIPE_PROMPT = "Give me 3 healthy high-protein recipe titles. Return ONLY the titles, one per line."

def ask_ai(client, prompt):
    response = client.chat(
        model=MODEL_NAME,
        messages=[{
            "role" : "user",
            "content" : prompt
        }]
    )
    return response.choices[0].message.content

def get_recipe_titles(client):
    answer = ask_ai(client, RECIPE_PROMPT)

    return [
        recipe.strip()
        for recipe in answer.split("\n")
        if recipe.strip()
    ]

def get_recipe_details(client, recipe):
    detail_prompt = f"""
                You are a nutrition expert.

                For this recipe:
                {recipe}

                Give:
                - full recipe
                - calories
                - protein amount"""
    
    return ask_ai(client, detail_prompt)

def show_recipe(client):
    if "recipes" not in st.session_state:
        st.session_state["recipes"]= (
            get_recipe_titles(client)
        )
    
    st.subheader("Choose a recipe")

    for recipe in st.session_state["recipes"]:
        with st.expander(recipe):
            recipe_key = f"recipe_{recipe}"

            if recipe_key not in st.session_state:
                st.session_state[recipe_key] = (
                    get_recipe_details(client, recipe)
                )
            
            st.write(st.session_state[recipe_key])
