import streamlit as st


def show_contact_page():

    st.title("Contact")

    st.markdown("""
    If you have any questions about the project, feel free to contact us.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Team")

        st.write("**Developer:** Lærke Lønborg")
        st.write("**Developer:** Camilla Eva Hansen")

        st.write("**Project:** Health App (Exam Project)")

    with col2:
        st.subheader("Contact Information")

        st.write("**Email:** example@email.com")
        st.write("**Phone:** +45 xx xx xx xx")
        st.write("**GitHub:** https://github.com/")

    st.divider()
