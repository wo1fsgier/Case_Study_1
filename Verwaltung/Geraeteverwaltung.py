import streamlit as st
from styles import set_background

def app():
    
    set_background("#524E4D")

    st.write("# Gerätemanagement")

    st.write("")
    st.write("## Geräteauswahl")

    with st.form("create_device_form"):
        name  = st.text_input("Gerätname")
        farbe = st.text_input("Gerätfarbe")

        submitted = st.form_submit_button("Gerät erstellen")

    