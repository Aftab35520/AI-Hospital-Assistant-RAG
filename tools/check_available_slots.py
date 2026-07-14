
from db.connection import Appointment

from datetime import datetime, timedelta
from langchain.tools import tool

ALL_SLOTS = [
    "09:00 AM",
    "10:00 AM",
    "11:00 AM",
    "12:00 PM",
    "02:00 PM",
    "03:00 PM",
    "04:00 PM"
]

@tool
def check_available_slots(doctor_id: str):
    """
    Return available slots for the next 3 days for a doctor.
    """

    today = datetime.today().date()

    availability = []

    for i in range(3):

        day = today + timedelta(days=i)

        booked = Appointment.find(
            {
                "doctor_id": doctor_id,
                "date": str(day),
                "status": "Booked"
            },
            {"time": 1, "_id": 0}
        )

        booked_slots = {x["time"] for x in booked}

        free_slots = [
            slot
            for slot in ALL_SLOTS
            if slot not in booked_slots
        ]

        availability.append({
            "date": str(day),
            "available_slots": free_slots
        })

    return availability