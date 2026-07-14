from datetime import datetime
from langchain.tools import tool
from db.connection import Appointment
@tool
def book_appointment(
    patient_id: str,
    patient_name: str,
    doctor_id: str,
    doctor_name: str,
    date: str,
    time: str,
):
    """
    Book an appointment if the slot is free.
    """

    exists = Appointment.find_one({
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "status": "Booked"
    })

    if exists:
        return {
            "status": "failed",
            "message": "This slot is already booked."
        }

    Appointment.insert_one({
        "patient_id": patient_id,
        "patient_name": patient_name,
        "doctor_id": doctor_id,
        "doctor_name": doctor_name,
        "date": date,
        "time": time,
        "status": "Booked",
        "created_at": datetime.now().isoformat()
    })

    return {
        "status": "success",
        "message": "Appointment booked successfully."
    }