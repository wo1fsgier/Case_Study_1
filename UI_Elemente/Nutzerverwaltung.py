import streamlit as st
from Buisness_Logic.user_service import User_Verwaltung
from styles import set_background

def app():
    set_background("#524E4D")
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

    table_data = {
    "Name": [],
    "Email": [],
    "User-ID": [],
    }

    if not users:
        st.info("Noch keine Nutzer vorhanden.")

    else:

        for n in users:

            table_data["Name"].append(n.name)
            table_data["Email"].append(n.email)
            table_data["User-ID"].append(n.id)

    st.table(table_data, border="horizontal")

    st.divider()

    st.subheader("Nutzer Löschen")
    if users: 
        user_map = {f"{d.name} ({d.id})":d for d in users}
        selected_key = st.selectbox("Nutzer auswäheln", list (user_map.keys()))
        selected_device = user_map[selected_key]
        if st.button("Nutzer löschen"):
            result = user_service.delete_user(selected_device.id)
            if not result.get("success"):
                st.error(result.get("error", "Löschen nicht möglich"))
            else:
                
                st.success("Nutzer gelöscht")
                st.rerun()
    else:
        st.info("Keine Nutzer zum Löschen")
    st.subheader("Nutzer bearbeiten")

    if not users: 
        st.info("Keine Nutzer zum Bearbeiten vorhanden")
    else: 
        edit = st.selectbox("Nutzer auswählen", users)
        default_email = user_service.get_user_by_email(edit)
        with st.form("edit_user"):
            new_name = st.text_input("Nutzername", value = edit.name)
            new_email = st.text_input("Mail der haftenden Person", value = default_email)
            confirm = st.form_submit_button("Bestätigen")

        if confirm:
            result = user_service.edit_user(edit.id,{"name": new_name, "email": new_email})
            st.success("Änderungen gespeichert")
            st.rerun()
