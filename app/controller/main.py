from Model.hospede import Hospede
from Model.quarto import Quarto
from Model.reserva import Reserva
from services.reserva_service import ReservaService
import streamlit as st

# Initialize the ReservaService
reserva_service = ReservaService()

# Streamlit app title
st.title("Hotel Reservation System")

# Create a new guest
st.header("Create Guest")
guest_name = st.text_input("Guest Name")
guest_cpf = st.text_input("Guest CPF")
guest_phone = st.text_input("Guest Phone")
if st.button("Add Guest"):
    guest = Hospede(guest_name, guest_cpf, guest_phone)
    reserva_service.add_guest(guest)
    st.success("Guest added successfully!")

# Create a new room
st.header("Create Room")
room_number = st.number_input("Room Number", min_value=1)
room_type = st.selectbox("Room Type", ["Single", "Double", "Suite"])
if st.button("Add Room"):
    room = Quarto(room_number, room_type)
    reserva_service.add_room(room)
    st.success("Room added successfully!")

# Create a new reservation
st.header("Create Reservation")
selected_guest = st.selectbox("Select Guest", reserva_service.get_all_guests())
selected_room = st.selectbox("Select Room", reserva_service.get_all_rooms())
check_in_date = st.date_input("Check-in Date")
check_out_date = st.date_input("Check-out Date")
if st.button("Make Reservation"):
    reservation = Reserva(0, selected_guest, selected_room, check_in_date, check_out_date)
    reserva_service.add_reservation(reservation)
    st.success("Reservation made successfully!")

# Display all reservations
st.header("Current Reservations")
reservations = reserva_service.get_all_reservations()
for reservation in reservations:
    st.write(f"Reservation ID: {reservation.id}, Guest: {reservation.hospede.nome}, Room: {reservation.quarto.numero}, Check-in: {reservation.data_entrada}, Check-out: {reservation.data_saida}")