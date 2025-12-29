from streamlit_extras.card import card
import streamlit as st

from streamlit_option_menu import option_menu
from UI_Elemente.Geraeteverwaltung import app as geraete
from UI_Elemente.Nutzerverwaltung import app as nutzer
from UI_Elemente.Reservierungssystem import app as reserviert
from UI_Elemente.Wartung import app as wartung
page = {
    "Geräteverwaltung": "geraete",
    "Nutzerverwaltung": "nutzer",
    "Reservierungen": "reserviert",
    "Wartung": "wartung",
}

def sidebar():

    with st.sidebar:
        selected = option_menu(
            menu_title = "Menü",
            options = list(page.keys()),
        )
    new_page = page[selected]
    if st.session_state.get("page") != new_page:
        st.session_state.page = new_page
        st.rerun()
    if st.sidebar.button("Zurück zum Dashboard"):
        st.session_state.page = None
        st.rerun()


def app():
    if "page" not in st.session_state:
        st.session_state.page = None
    if st.session_state.page in {"geraete", "nutzer", "reserviert", "wartung"}:
        sidebar()
    
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