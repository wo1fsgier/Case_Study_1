import streamlit as st
import datetime
from Buisness_Logic.reservation_service import Reservation
from Buisness_Logic.device_service import Device_Verwaltung

def app():
    st.write("# Reservierungssystem")
    
    reservation_service = Reservation()
    device_service = Device_Verwaltung()

    st.write("## Reservierung erstellen")
    devices = device_service.get_all_devices()

    with st.form("create_reservation_form"):
        today = datetime.date.today()
        start_date = st.date_input("Startdatum", today)
        end_date = st.date_input("Enddatum", today)  
        start_hour = st.time_input("Um", datetime.time(8, 45))
        end_hour = st.time_input("Bis", datetime.time(8, 45))
        user_email = st.text_input("Nutzer-Emailadresse")
        printer = st.selectbox("Drucker auswählen", devices)

        submitted = st.form_submit_button("Reservierung erstellen")

    if submitted:
        result = reservation_service.create_reservation(
            responsible_user_email=user_email,
            printer=printer,
            start_date=start_date,
            end_date=end_date,
            start_hour=start_hour,
            end_hour=end_hour

        )
        if not result["success"]:
            st.error(result["error"])
        else:
            st.success("Reservierung wurde erstellt!")

    st.divider()

    st.subheader("Reservierungen")

    reserviert = reservation_service.get_all_reservations()

    table_data = {
        "Drucker": [],
        "User_Email": [],
        "Startdatum": [],
        "Enddatum": [],
        "Um": [],
        "Bis":[]
        }
    
    devices = device_service.get_all_devices()
    id_to_name = {d.id: getattr(d, "device_name", getattr(d, "name", str(d))) for d in devices}

    if not reserviert:
        st.info("Noch keine Reservierungen.")

    else:

        for n in reserviert:
            drucker_name = id_to_name.get(n.printer, n.printer)
            table_data["Drucker"].append(drucker_name)
            table_data["User_Email"].append(n.responsible_user_email)
            table_data["Startdatum"].append(start_date.strftime("%d.%m.%Y") if start_date else "")
            table_data["Enddatum"].append(end_date.strftime("%d.%m.%Y") if end_date else "")
            table_data["Um"].append(start_hour.strftime("%H:%M"))
            table_data["Bis"].append(end_hour.strftime("%H:%M"))
    st.table(table_data, border="horizontal")
    st.divider()

    st.subheader("Reservierung löschen")
    if reserviert:
        reserviert_map = {f"{d.printer} ({d.responsible_user_email}) ({d.start_date}) - ({d.end_date}) ({d.start_hour}) ({d.end_hour}) ({d.id})": d
            for d in reserviert
        }

        selected_key = st.selectbox("Reservierung auswählen", list(reserviert_map.keys()))
        selected_reservation = reserviert_map[selected_key]

        if st.button("Reservierung löschen"):
            reservation_service.delete_reservation(selected_reservation.id)
            st.success("Reservierung gelöscht")
            st.rerun()
    else:
            st.info("Keine Reservierungen zum Löschen")
