from django import forms
from .models import Flow,FlowEndFlag





class createFlow(forms.ModelForm):
    
    class Meta:
        model = Flow
        fields = ['FlowName','Question','Answers','order','words']
        widgets = {'order': forms.HiddenInput()}
        
class markEnd(forms.ModelForm):

    class Meta:
        model = FlowEndFlag
        fields = ['end']






        