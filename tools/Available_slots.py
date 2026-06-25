from langchain.tools import tool
from db.connection import Appointment
from datetime import datetime, timedelta
import json
@tool
def get_available_slots(
    doctor_id: str,
    date: str
):
    """
    Get available appointment slots for a doctor on a given date.

    Working hours: 10:00 AM to 5:00 PM.
    Slot duration: 1 hour.
    """

    booked = Appointment.find(
        {
            "doctor_id": doctor_id,
            "date": date
        },
        {
            "_id": 0,
            "time": 1
        }
    )

    booked_times = {doc["time"] for doc in booked}

    start_time = datetime.strptime("10:00", "%H:%M")
    end_time = datetime.strptime("17:00", "%H:%M")

    available_slots = []

    current = start_time

    while current < end_time:
        slot = current.strftime("%H:%M")

        if slot not in booked_times:
            available_slots.append(slot)

        current += timedelta(hours=1)

    return json.dumps({
        "doctor_id": doctor_id,
        "date": date,
        "available_slots": available_slots
    })