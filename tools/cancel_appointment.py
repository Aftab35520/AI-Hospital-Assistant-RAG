from langchain.tools import tool
from db.connection import Appointment
@tool
def cancel_appointment(
    patient_id: str,
    doctor_id: str,
    date: str,
    time: str,
):
    """
    Cancel a booked appointment.
    """

    result = Appointment.delete_one({
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "status": "Booked"
    })

    if result.deleted_count == 0:
        return "No matching appointment found."

    return "Appointment cancelled successfully."