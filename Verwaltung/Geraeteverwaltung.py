import streamlit as st
from database import devices_table
from styles import set_background
import uuid

def app():
    
    set_background("#524E4D")

    st.write("# Gerätemanagement")

    st.write("")
    st.write("## Neues Gerät hinzufügen")

    with st.form("create_device_form"):
        name  = st.text_input("Gerätname")
        farbe = st.text_input("Gerätfarbe")

        submitted = st.form_submit_button("Gerät erstellen")

    if submitted:
        if name.strip() == "":
            st.error("Bitte einen Gerätenamen eingeben.")
        else:
            device = {
                "id": str(uuid.uuid4()),
                "name": name,
                "farbe": farbe
            }

            devices_table.insert(device)

            st.success("Gerät wurde erfolgreich angelegt!")

    st.divider()