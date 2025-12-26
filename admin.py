from streamlit_extras.card import card
import streamlit as st
from Verwaltung import geraete, nutzer, reserviert, wartung
def sidebar():
    st.sidebar.title("Menü")

    if st.sidebar.button("Geräte-Verwaltung"):
        st.session_state.page = "geraete"
        st.rerun()

    if st.sidebar.button("Nutzer-Verwaltung"):
        st.session_state.page = "nutzer"
        st.rerun()

    if st.sidebar.button("Reservierungen"):
        st.session_state.page = "reserviert"
        st.rerun()

    if st.sidebar.button("Wartungen"):
        st.session_state.page = "wartung"
        st.rerun()

    st.sidebar.divider()
    if st.sidebar.button("Zurück zum Dashboard"):
        st.session_state.page = None
        st.rerun()
def app():
    if "page" not in st.session_state:
        st.session_state.page = None
    if st.session_state.page in {"geraete", "nutzer", "reserviert", "wartung"}:
        sidebar()
    if st.session_state.page is not None:
        

        if st.session_state.page == "geraete":
            geraete()
        elif st.session_state.page == "nutzer":
            nutzer()
        elif st.session_state.page == "reserviert":
            reserviert()
        elif st.session_state.page == "wartung":
            wartung()
        
        if st.button("Zurück"):
            st.session_state.page = None
            st.rerun()

        return

    st.title("Admin Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        if card(title="Geräteverwaltung", text="Geräte verwalten"):
            st.session_state.page = "geraete"
            st.rerun()
    with col2:
        if card(title="Nutzerverwaltung", text="Nutzer anlegen"):
            st.session_state.page = "nutzer"
            st.rerun()

    col3, col4 = st.columns(2)
    with col3:
        if card(title="Reservierungs-\nsystem", text="Reservierungen anzeigen"):
            st.session_state.page = "reserviert"
            st.rerun()
    with col4:
        if card(title="Wartungs-\nManagement", text="Wartungen anzeigen"):
            st.session_state.page = "wartung"
            st.rerun()

    st.divider()
