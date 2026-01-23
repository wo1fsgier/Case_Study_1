import streamlit as st
from Buisness_Logic.maintenance_service import maintenance
from Buisness_Logic.device_service import Device_Verwaltung

def app():
    device_service = Device_Verwaltung()
    maintenance_service = maintenance()

    st.write("# Wartungs-Management")
    st.subheader("Alle Gerätewartungen")

    overview = maintenance_service.get_maintenance_overview()

    table_data = {
        "Name": [],
        "User_Email": [],
        "Status": [],
        "Letzte Wartung": [],
        "Nächste Wartung": [],
        "Intervall (Tage)": [],
        "Kosten": []
    }

    for r in overview:
        device = next(
            d for d in device_service.get_all_devices() if d.id == r["device_id"]
        )
        email = device_service.get_user_email_for_device(device)

        table_data["Name"].append(r["device_name"])
        table_data["User_Email"].append(email)
        display_status = "maintenance" if r["locked_today"] else r["status"]
        table_data["Status"].append(display_status)
        lm = r.get("last_maintenance")
        table_data["Letzte Wartung"].append(
        lm.strftime("%d.%m.%Y") if lm else "-"
)
        nm = r.get("next_maintenance")
        table_data["Nächste Wartung"].append(
        nm.strftime("%d.%m.%Y") if nm else "-"
        )
        table_data["Intervall (Tage)"].append(r["service_intervall"])
        table_data["Kosten"].append(r["service_cost"])

    st.table(table_data)

    st.subheader("Wartungskosten pro Quartal")
    costs = maintenance_service.get_costs_per_quarter()


    if not costs:
        st.info("Keine Wartungskosten vorhanden.")
    else:
        st.table({
            "Quartal": list(costs.keys()),
            "Kosten": [costs[q] for q in costs]
        })