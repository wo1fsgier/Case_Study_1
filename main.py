import streamlit as st
import account, admin

st.set_page_config(
        page_title = "Verwaltung"
)

def main ():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        account.app()
    else:
        admin.app()

if __name__ == "__main__":
    main()