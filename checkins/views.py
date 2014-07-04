from django.http import HttpResponseRedirect
from django.shortcuts import render

from checkins.models import Checkin
from checkins.forms import CheckinForm

def index(request):
    if request.method == 'GET':
        form = CheckinForm()
    else:
        form = CheckinForm(request.POST, request.FILES)
        if form.is_valid():
            date = form.cleaned_data['date']
            weight = form.cleaned_data['weight']
            checkin = Checkin(date=date,weight=weight,photo=request.FILES['photo'])
            checkin.save()
            return HttpResponseRedirect('/')

    return render(request, 'index.html', {'checkins': Checkin.objects.all(), 'form': form})
