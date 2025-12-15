from streamlit_extras.card import card
import streamlit as st
import Geraeteverwaltung, Nutzerverwaltung, Reservierungssystem, Wartung

def app():

    if "page" not in st.session_state:
        st.session_state.page = None

        
    if st.session_state.page is None:

        col1, col2 = st.columns(2)
    
        with col1:
            if card(title="Geräteverwaltung", text="Geräte verwalten"):
                st.session_state.page = "Geraeteverwaltung"
                st.rerun()
        with col2:
            if card(title="Nutzerverwaltung", text="Nutzer anlegen"):
                st.session_state.page = "Nutzerverwaltung"
                st.rerun()
        col3, col4 = st.columns(2)
        with col3:
            if card(title="Reservierungs-system", text="Reservierungen anzeigen"):
                st.session_state.page = "Reservierungssystem"
                st.rerun()
        with col4:
            if card(title="Wartungs-Management", text="Wartungen anzeigen"):
                st.session_state.page = "Wartung"
                st.rerun()


    else:
        if st.button("Zurück"):
            st.session_state.page = None
            st.rerun()
        if st.session_state.page == "Geraeteverwaltung":
            Geraeteverwaltung.app()
        elif st.session_state.page == "Nutzerverwaltung":
            Nutzerverwaltung.app()
        
    
        elif st.session_state.page == "Reservierungssystem":
            Reservierungssystem.app()
        elif st.session_state.page == "Wartung":
            Wartung.app()
    

    st.divider()

