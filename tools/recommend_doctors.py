from langchain.tools import tool
from db.connection import Doctor
import json
@tool
def recommend_doctors(condition: str):
    """
    Recommend up to 3 doctors for a patient's disease, condition, or symptoms.
    Returns doctor name, specialization, and about information.
    """

    doctors = list(
        Doctor.find(
            {
                "diseases_treated": {
                    "$regex": condition,
                    "$options": "i"
                }
            },
            {
                "_id": 0,
                "doctor_id": 1,
                "name": 1,
                "specialization": 1,
                "about": 1
            }
        ).limit(3)
    )
    if not doctors or len(doctors) == 0:
            return json.dumps({
                "status": "not_found",
                "message": f"No doctors found for condition: {condition}",
                "doctors": []
            })

    return  json.dumps(doctors)