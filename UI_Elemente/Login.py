import streamlit as st
import time
import keyboard

VALID_EMAIL = "admin@admin.com"
VALID_USER  = "admin"


def app():

    st.title ("HAWG Device Control Software")
    with st.form(key = "signup", clear_on_submit=True):
        st.subheader("Login")
        user  = st.text_input("Benutzer")
        email = st.text_input("E-Mail")
        if st.form_submit_button("Anmelden") or keyboard.press_and_release("enter"):
            user = user.strip()
            email = email.strip()
            if email == VALID_EMAIL and user == VALID_USER:
                st.session_state.logged_in = True
                st.session_state.user = user
                with st.spinner("Bitte Warten Sie einen Moment", show_time=True):
                    time.sleep(2)
                st.success("Done!")
                
                st.rerun()
            else:
                st.error("Login fehlgeschlagen")
            
        st.write("##### User = admin")
        st.write("##### admin@admin.com")
