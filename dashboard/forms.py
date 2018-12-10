from django import forms
from .models import Bot



class createBot(forms.ModelForm):
    
    class Meta:
        model = Bot
        fields = ['Name']
       