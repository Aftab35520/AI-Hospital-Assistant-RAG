from langchain.tools import tool
from datetime import datetime, timedelta
from dateutil import parser
import json
@tool
def validate_appointment_date(date: str):
    """
    Validate appointment date.
    Booking is allowed only from tomorrow up to the next 3 days.
    """

    try:
        appointment_date = parser.parse(date).date()

        today = datetime.today().date()
        min_date = today + timedelta(days=1)
        max_date = today + timedelta(days=3)

        if appointment_date < min_date:
            return json.dumps({
                "status": "failed",
                "message": f"Appointments can only be booked from {min_date} onwards."
            })

        if appointment_date > max_date:
            return json.dumps({
                "status": "failed",
                "message": f"Appointments can only be booked up to {max_date}."
            })

        return json.dumps({
            "status": "success",
            "date": appointment_date.strftime("%Y-%m-%d"),
            "message": "Date is valid."
        })

    except Exception:
        return {
            "status": "failed",
            "message": "Invalid date. Please provide a valid appointment date."
        }