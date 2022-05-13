import pytz

from datetime import datetime


def is_visit_long(duration):
    expected_duration = 60*60
    return duration > expected_duration


def format_duration(total_seconds):
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    if hours < 10:
        hours = f"0{hours}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{hours}:{minutes}:{seconds}"


def get_duration(leave_time, enter_time):
    if not leave_time:
        leave_time = datetime.now(pytz.utc)
    delta = leave_time - enter_time
    return delta.total_seconds()
