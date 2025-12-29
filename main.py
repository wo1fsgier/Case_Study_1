import streamlit as st
import UI_Elemente.Login as Login
import UI_Elemente.Home as Home

st.set_page_config(
        page_title = "HAWG Device Control"
)

def main ():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        Login.app()
    else:
        Home.app()

if __name__ == "__main__":
    main()