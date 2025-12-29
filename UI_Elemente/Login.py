import streamlit as st

VALID_EMAIL = "admin@admin.com"
VALID_USER  = "admin"

def app():
    st.title ("HG 3D Control")
    with st.form(key = "signup", clear_on_submit=True):
        st.subheader("Login")
        user  = st.text_input("Benutzer")
        email = st.text_input("E-Mail")
        if st.form_submit_button("Anmelden"):
            user = user.strip()
            email = email.strip()
            if email == VALID_EMAIL and user == VALID_USER:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Login fehlgeschlagen")
        st.write("##### User = admin")
        st.write("##### admin@admin.com")