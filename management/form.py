from django import forms
from django.forms import fields

from .models import patient

class PatientForm(forms.ModelForm):
    patient_name = forms.CharField(max_length=25)
    status = forms.CharField(max_length=50)
    illness = forms.CharField()
    doctor_select = forms.CharField()

    class Meta:
        model = patient
        fields = [
            'patient_name',
            'status',
            'illness',
            'doctor_select'
        ]