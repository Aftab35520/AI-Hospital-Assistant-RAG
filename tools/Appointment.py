from langchain.tools import tool
from db.connection import Appointment
from datetime import datetime
from dateutil import parser

@tool
def book_appointment(
    patient_id: str,
    patient_name: str,
    doctor_id: str,
    doctor_name: str,
    date: str,
    time: str
):
    """
    Book an appointment for a patient.

    Call this tool only after the patient has confirmed the appointment details.

    Args:
        patient_id: Unique patient ID.
        patient_name: Patient name.
        doctor_id: Doctor ID.
        doctor_name: Doctor name.
        date: Appointment date.
        time: Appointment time.

    Returns:
        Appointment booking status and details.
    """

    try:
        if not all([
            patient_id,
            patient_name,
            doctor_id,
            doctor_name,
            date,
            time
        ]):
            return {
                "status": "failed",
                "message": "Missing required appointment information."
            }

        try:
            appointment_date = parser.parse(date).date()
            today = datetime.today().date()

            if appointment_date < today:
                return {
                    "status": "failed",
                    "message": "Please provide a future date. Appointments cannot be booked for past dates."
                }

            date = appointment_date.strftime("%Y-%m-%d")

        except Exception:
            return {
                "status": "failed",
                "message": "Invalid date. Please provide a valid appointment date."
            }

        existing_appointment = Appointment.find_one({
            "doctor_id": doctor_id,
            "date": date,
            "time": time
        })

        if existing_appointment:
            return {
                "status": "failed",
                "message": f"Dr. {doctor_name} already has an appointment at {time} on {date}. Please choose another time."
            }

        appointment_data = {
            "patient_id": patient_id,
            "patient_name": patient_name,
            "doctor_id": doctor_id,
            "doctor_name": doctor_name,
            "date": date,
            "time": time,
            "status": "Booked",
            "created_at": datetime.utcnow().isoformat()
        }

        result = Appointment.insert_one(appointment_data)

        return {
            "status": "success",
            "appointment_id": str(result.inserted_id),
            "message": "Appointment booked successfully.",
            "appointment": {
                "patient_id": patient_id,
                "patient_name": patient_name,
                "doctor_name": doctor_name,
                "date": date,
                "time": time
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }