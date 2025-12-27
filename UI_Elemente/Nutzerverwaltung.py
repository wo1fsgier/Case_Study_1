import streamlit as st
from Buisness_Logic.user_service import User_Verwaltung

def app():
    user_service = User_Verwaltung()
    st.write("# Nutzer-Verwaltung")
    st.write("## Nutzer anlegen")

    with st.form("create_user_form"):
        name  = st.text_input("Name")
        email = st.text_input("E-Mail")

        submitted = st.form_submit_button("User erstellen")

    if submitted:
        result = user_service.create_user(name, email)
        if not result["success"]:
            st.error(result["error"])
        else:
            st.success("User wurde erstellt!")
    
    st.divider()

    st.subheader("Nutzer Übersicht")

    users = user_service.get_all_users()

    if not users:
        st.info("Noch keine Geräte vorhanden.")

    else:

        table_data = {
        "Name": [],
        "Email": [],
        "User-ID": [],
     }
    for n in users:

        table_data["Name"].append(n.name)
        table_data["Email"].append(n.email)
        table_data["User-ID"].append(n.id)

    st.table(table_data, border="horizontal")

    st.divider()

    st.subheader("Nutzer Bearbeiten/Löschen")
