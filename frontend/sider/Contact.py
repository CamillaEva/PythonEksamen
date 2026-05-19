import streamlit as st


def show_contact_page():

    st.title("Contact")

    st.markdown("""
    Hvis du har spørgsmål til projektet, er du velkommen til at kontakte os
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Team")

        st.write("**udvikler:** Lærke Lønborg")
        st.write("**udvikler:** Camilla Eva Hansen")
       

        st.write("**Projekt:** Health App (Eksamensprojekt)")

    with col2:
        st.subheader("Kontakt")

        st.write("**Email:** eksempel@email.com")
        st.write("**Telefon:** +45 xx xx xx xx")
        st.write("**GitHub:** https://github.com/")

    st.divider()

