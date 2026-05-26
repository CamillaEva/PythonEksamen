import streamlit as st


def show_about_page():

    st.title("About Us")

    st.markdown("""
    Welcome to our health and food log app.

    We are a small development team with a passion for making health, nutrition, and everyday habits easier to manage and more motivating. Our goal is to create a simple and user-friendly tool where you can easily keep track of your daily meals, calories, and eating habits.

    ---

    ## What Our Platform Can Do

    On our platform, you can:

    - Log your daily meals quickly and easily  
    - Automatically calculate calories for the food you eat  
    - Get a visual overview of your daily calorie intake through a donut chart  
    - Save and organize your meals into breakfast, lunch, dinner, and snacks  
    - Get inspiration for healthy and high-protein recipes generated with AI  

    ---

    ## Our Goal

    We want to make it easier for you to take control of your eating habits without complicated systems or unnecessary hassle. Everything is designed to be fast, simple, and visually clear, so you can focus on your goals instead of difficult calculations.

    ---

    ## Who We Are

    We are a small development team working with modern web technologies such as Streamlit, Python, and AI integration. This project was developed as part of an exam project with a focus on user experience, data visualization, and intelligent functionality.
    """)
