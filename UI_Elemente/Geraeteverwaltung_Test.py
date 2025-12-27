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

'''
    devices = devices_table.all()

    if not devices:
        st.info("Noch keine Geräte vorhanden.")
    else:

        table_data = {
        "Gerät": [],
        "Nutzer": [],
        "Status": [],
        "Geräte-ID": []
     }
        for d in devices:

            if d.get("status", "frei") == "frei":
                status = "🟢 :green[Frei]"
            elif d["status"] == "reserviert":
                status = "🟡 :orange[Reserviert]"
            else:
                status = "🔴 :red[Wartung]"

            table_data["Gerät"].append(f":material/devices: {d["name"]}")
            table_data["Nutzer"].append(d["nutzer"])
            table_data["Status"].append(status)
            table_data["Geräte-ID"].append(d["id"])

        st.table(table_data, border="horizontal")

        st.divider()

        st.subheader("Geräte Löschen")
        
    if devices:

        device_map = {}

        for d in devices:

            label = f"{d["name"]} ({d["nutzer"]})"
            device_map[label] = d.doc_id

        selected_device = st.selectbox(
        "Gerät auswählen",
        options=list(device_map.keys())
        )

        if st.button("🗑️ Gerät löschen"):
            devices_table.remove(doc_ids=[device_map[selected_device]])
            st.success("Gerät wurde gelöscht.")
            st.rerun()
    else:
        st.info("Keine Geräte zum Löschen vorhanden.")
'''