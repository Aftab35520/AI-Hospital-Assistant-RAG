from langchain.tools import tool
from db.connection import Appointment
from bson import ObjectId


@tool
def cancel_appointment(
    patient_id: str,
    appointment_id: str = "",
    doctor_id: str = "",
    date: str = "",
    time: str = ""
):
    """
    Cancel an appointment.

    You can cancel either:
    1. Using appointment_id, OR
    2. Using patient_id + doctor_id + date + time.

    Args:
        patient_id: Patient ID.
        appointment_id: Appointment ID (preferred).
        doctor_id: Doctor ID.
        date: Appointment date (YYYY-MM-DD).
        time: Appointment time (HH:MM).

    Returns:
        Cancellation status.
    """

    try:
        # Cancel using appointment ID
        if appointment_id:
            result = Appointment.delete_one({
                "_id": ObjectId(appointment_id),
                "patient_id": patient_id
            })

        else:
            # Cancel using appointment details
            if not all([doctor_id, date, time]):
                return {
                    "status": "failed",
                    "message": (
                        "Please provide either appointment_id or "
                        "doctor_id, date and time."
                    )
                }

            result = Appointment.delete_one({
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "date": date,
                "time": time
            })

        if result.deleted_count == 0:
            return {
                "status": "failed",
                "message": "No matching appointment found."
            }

        return {
            "status": "success",
            "message": "Appointment cancelled successfully."
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }