import streamlit as st
import datetime

def app():
    st.write("# Reservierungssystem")
    st.write("## Alle Reservierungen")

    st.write("## Reservierung erstellen")
    today = datetime.datetime.now()
    Startdatum = st.date_input("Startdatum", today)
    Enddatum = st.date_input("Enddatum", value = None)
    
    st.write("## Reservierung entfernen")