import streamlit as st

def app():
    st.write("# Nutzer-Verwaltung")
    st.write("## Nutzer anlegen")

    with st.form("create_user_form"):
        name  = st.text_input("Name")
        email = st.text_input("E-Mail")

        submitted = st.form_submit_button("User erstellen")