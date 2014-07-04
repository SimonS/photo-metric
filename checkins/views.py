from django.shortcuts import render

from checkins.models import Checkin

def index(request):
    return render(request, 'index.html', {'checkins': Checkin.objects.all()})
