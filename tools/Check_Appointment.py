from langchain.tools import tool
from db.connection import Appointment
import json
@tool
def Check_patient_Appointment(patient_id):
    """Check patient appointments using patient id"""

    appointments = list(
        Appointment.find(
            {"patient_id": patient_id},
            {"_id": 0}
        )
    )

    return json.dumps(appointments) 