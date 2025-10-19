# Simple Bus Reservation System
# This is a placeholder app.py file

import streamlit as st
import json, os

st.title("Bus Reservation System")

DATA_FILE = "reservations.json"

# Load reservations
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        reservations = json.load(f)
else:
    reservations = {}

st.write("Current Reservations:")
st.write(reservations)