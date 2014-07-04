from django import forms

from checkins.models import Checkin

class CheckinForm(forms.ModelForm):

    weight = forms.DecimalField(label='Weight')
    photo = forms.ImageField(
        label='Checkin Photo'
    )

    class Meta:
        model = Checkin