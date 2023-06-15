from django import forms

from .models import Thread, ThreadResponse

class ThreadForm(forms.ModelForm):
    class Meta:
        model= Thread
        fields={'subject', 'name', 'email', 'message', 'image'}

class ThreadResponseForm(forms.ModelForm):
    class Meta:
        model= ThreadResponse
        fields={'user', 'response'}