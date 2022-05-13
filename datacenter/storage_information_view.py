from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.visit_duration import is_visit_long, \
    format_duration, get_duration


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits_serialized = []
    for visit in non_closed_visits:
        duration = get_duration(visit.leaved_at, visit.entered_at)
        visit_information = {'who_entered': visit.passcard,
                             'entered_at': localtime(visit.entered_at),
                             'duration': format_duration(duration),
                             'is_strange': is_visit_long(duration)}
        non_closed_visits_serialized.append(visit_information)
        context = {
          'non_closed_visits': non_closed_visits_serialized,
          }
    return render(request, 'storage_information.html', context)
