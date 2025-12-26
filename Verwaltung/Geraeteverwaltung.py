import streamlit as st
from database import devices_table
from styles import set_background
import uuid

def app():
    
    set_background("#524E4D")

    st.write("# Gerätemanagement")

    st.write("")
    st.write("## Neues Gerät hinzufügen")

    with st.form("create_device_form"):
        name  = st.text_input("Gerätname")
        farbe = st.text_input("Gerätfarbe")

        submitted = st.form_submit_button("Gerät erstellen")

    if submitted:
        if name.strip() == "":
            st.error("Bitte einen Gerätenamen eingeben.")
        else:
        
            exists = False
            for d in devices_table.all():
                if d.get("name") == name:
                    exists = True
                    break
        
            if exists:
                st.error("Ein Gerät mit diesem Namen existiert bereits.")
            else:
                device = {
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "farbe": farbe,
                    "status": "frei"
                }
                devices_table.insert(device)
                st.success("Gerät wurde erfolgreich angelegt!")

    st.divider()

    st.subheader("Geräte Übersicht")

    devices = devices_table.all()

    if not devices:
        st.info("Noch keine Geräte vorhanden.")
    else:

        table_data = {
        "Gerät": [],
        "Farbe": [],
        "Status": []
     }
        for d in devices:

            if d.get("status", "frei") == "frei":
                status = "🟢 :green[Frei]"
            elif d["status"] == "reserviert":
                status = "🟡 :orange[Reserviert]"
            else:
                status = "🔴 :red[Wartung]"

            table_data["Gerät"].append(f":material/devices: {d['name']}")
            table_data["Farbe"].append(d["farbe"])
            table_data["Status"].append(status)

        st.table(table_data, border="horizontal")