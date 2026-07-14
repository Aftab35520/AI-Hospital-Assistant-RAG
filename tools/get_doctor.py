from langchain.tools import tool
from db.connection import Doctor
from rapidfuzz import fuzz
@tool
def search_doctor(query: str):
    """
    Search doctors by name, specialization, or disease.
    Returns the top 3 matching doctors.
    """

    query = query.lower().strip()

    doctors = list(Doctor.find({}, {"_id": 0}))

    matches = []

    for doctor in doctors:

        disease_score = max(
            fuzz.token_set_ratio(query, disease.lower())
            for disease in doctor["diseases_treated"]
        )

        score = max(
            fuzz.token_set_ratio(query, doctor["name"].lower()),
            fuzz.token_set_ratio(query, doctor["specialization"].lower()),
            disease_score,
        )

        if score >= 70:
            matches.append((score, doctor))

    # Sort by highest score
    matches.sort(key=lambda x: x[0], reverse=True)

    if not matches:
        return "Sorry, no doctor available."

    result = []

    for score, doctor in matches[:3]:
        result.append({
            "doctor_id": doctor["doctor_id"],
            "name": doctor["name"],
            "specialization": doctor["specialization"],
            "diseases_treated": doctor["diseases_treated"],
            "about": doctor["about"],
            "match_score": score
        })
    print(result)
    return result