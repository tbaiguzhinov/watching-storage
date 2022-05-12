import pytz

from datetime import datetime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

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

def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits_serialized = []
    for visit in non_closed_visits:
      duration = get_duration(visit.leaved_at, visit.entered_at)
      visit_information = {'who_entered': visit.passcard,
                     'entered_at': localtime(visit.entered_at),
                     'duration': format_duration(duration),
                    'is_strange':
                    is_visit_long(duration)}
      non_closed_visits_serialized.append(visit_information)
    context = {
        'non_closed_visits': non_closed_visits_serialized,
    }
    return render(request, 'storage_information.html', context)
