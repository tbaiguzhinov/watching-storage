from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.storage_information_view import get_duration, format_duration, is_visit_long

def passcard_info_view(request, passcode):
  passcard = Passcard.objects.filter(passcode=passcode).get()
  
  this_passcard_visits_serialized = []
  this_passcard_visits = Visit.objects.filter(passcard=passcard.id)
  for visit in this_passcard_visits:
    duration = get_duration(visit.leaved_at, visit.entered_at)
    visit_details = {'entered_at': localtime(visit.entered_at),
                     'duration': format_duration(duration),
                     'is_strange': is_visit_long(duration)}
    this_passcard_visits_serialized.append(visit_details)

  context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_serialized
    }
  return render(request, 'passcard_info.html', context)
