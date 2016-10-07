from django.forms import ModelForm, Textarea
from django import forms
from django.forms import extras
from app.models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(ModelForm):
    # choices = ('yes','no')
    # all_day = forms.ChoiceField(choices=choices)
    class Meta:
        model = Event
        fields = ['title','attachment','start','end']
        widgets = {
            'title': forms.TextInput(attrs={'required':False,'placeholder': 'title, name, or topic'}),
            'start': DateInput(),
            'end': DateInput()
        }