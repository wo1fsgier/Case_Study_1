import streamlit as st

VALID_EMAIL = "admin@admin.com"
VALID_USER  = "admin"

def app():
    st.title("Login")
    user  = st.text_input("Benutzer")
    email = st.text_input("E-Mail")
    if st.button("Anmelden"):
        if email == VALID_EMAIL and user == VALID_USER:
            st.session_state.logged_in = True
            st.session_state.user = user
            st.rerun()
        else:
            st.error("Login fehlgeschlagen")
