from langchain.tools import tool
from db.connection import Appointment
@tool
def check_appointments(patient_id: str):
    """
    Return all appointments of a patient.
    """

    appointments = list(
        Appointment.find(
            {"patient_id": patient_id},
            {"_id": 0}
        )
    )

    if not appointments:
        return "No appointments found."

    return appointments