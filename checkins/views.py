from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from checkins.models import Checkin
from checkins.forms import CheckinForm

@login_required
def index(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST, request.FILES)
        if form.is_valid():
            date = form.cleaned_data['date']
            weight = form.cleaned_data['weight']
            checkin = Checkin(date=date,weight=weight,photo=request.FILES['photo'])
            checkin.save()
            return HttpResponseRedirect('/')
    else:
        form = CheckinForm()

    return render(request, 'index.html', {'checkins': Checkin.objects.all(), 'form': form})
