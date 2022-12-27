from datacenter.models import Passcard, Visit
from datacenter.models import format_duration
from datacenter.models import get_duration
from datacenter.models import is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get_object_or_404(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    passcard_visits_serialized = []  
    for passcard_visit in passcard_visits:
        entered_at = localtime(passcard_visit.entered_at)
        duration = format_duration(get_duration(passcard_visit))
        is_strange = is_visit_long(passcard_visit)
        visit = {
            "entered_at": entered_at,
            "duration": duration,
            "is_strange": is_strange,
        }
        passcard_visits_serialized.append(visit)
    context = {
        "passcard": passcard,
        "this_passcard_visits": passcard_visits_serialized,
    }
    return render(request, "passcard_info.html", context)
