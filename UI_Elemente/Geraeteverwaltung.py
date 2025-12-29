import streamlit as st
from Buisness_Logic.device_service import Device_Verwaltung
from styles import set_background
import uuid

## Gerät erstellen funktioniert für die Datenbank bereits. Alles weitere also Anzeige etc. muss noch implementiert werden

def app():

    device_service = Device_Verwaltung()

    set_background("#524E4D")

    st.write("# Gerätemanagement")

    st.write("")
    st.write("## Neues Gerät hinzufügen")

    with st.form("create_device_form"):
        name  = st.text_input("Gerätname")
        nutzeremail = st.text_input("Nutzer-Emailadresse")

        submitted = st.form_submit_button("Gerät erstellen")

    if submitted:
        result = device_service.create_device(name, nutzeremail)
        if not result["success"]:
            st.error(result["error"])
        else:
            st.success("User wurde erstellt!")

    st.divider()

    st.subheader("Geräte Übersicht")

    devices = device_service.get_all_devices()

    table_data = {
        "Name": [],
        "User_Email": [],
        "Status": [],
        "Last_Update": []
        }

    if not devices:
        st.info("Noch keine Geräte vorhanden.")

    else:

        for n in devices:
            email = device_service.get_user_email_for_device(n)

            table_data["Name"].append(n.name)
            table_data["User_Email"].append(email)
            table_data["Status"].append(n.status)
            table_data["Last_Update"].append(n.last_update.strftime("%d.%m.%Y %H:%M"))

    st.table(table_data, border="horizontal")

    st.divider()

    st.subheader("Gerät Löschen")
    if devices: 
        device_map = {f"{d.name} ({d.id})":d for d in devices}
        selected_key = st.selectbox("Gerät auswäheln", list (device_map.keys()))
        selected_device = device_map[selected_key]
        if st.button("Gerät löschen"):
            device_service.delete_device(selected_device.id)
            st.success("Gerät gelöscht")
            st.rerun()
    else:
        st.info("Keine Geräte zum Löschen")

    st.subheader("Gerät bearbeiten")
    
    if not devices: 
        st.info("Keine Geräte zum Bearbeiten vorhanden")
    else: 
        edit = st.selectbox("Gerät auswählen", devices)
        default_email = device_service.get_user_email_for_device(edit)
        with st.form("edit_device"):
            new_name = st.text_input("Gerätename", value = edit.name)
            new_email = st.text_input("Mail der haftenden Person", value = default_email)
            confirm = st.form_submit_button("Bestätigen")

        if confirm:
            result = device_service.update_device(edit.id,{"name": new_name, "responsible_user_email": new_email})
            st.success("Änderungen gespeichert")
            st.rerun()
