import datetime


def time_until_event(event_time_str):
    """
    Ushbu funksiya berilgan vaqtni hozirgi vaqt bilan solishtirib,
    oradagi kunlar va soatlar farqini hisoblaydi.

    event_time_str: str
        Vaqtni o'z ichiga olgan satr, format: "YYYY-MM-DD HH:MM"

    Returns:
        dict: Kunlar va soatlar farqini o'z ichiga olgan lug'at.
    """
    current_time = datetime.datetime.now()
    event_time = datetime.datetime.strptime(event_time_str, "%Y-%m-%d %H:%M")
    time_difference = event_time - current_time

    if time_difference.total_seconds() < 0:
        return {"days": 0, "hours": 0, "minutes": 0, "status": "past"}

    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60

    return {"days": days, "hours": hours, "minutes": minutes, "status": "future"}


# Misol vaqt
event_time_str = "2024-09-01 10:00"

# Vaqt farqini hisoblash
time_difference = time_until_event(event_time_str)
print(
    f"Oradagi kunlar: {time_difference['days']}, soatlar: {time_difference['hours']}, daqiqalar: {time_difference['minutes']}")
