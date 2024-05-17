from django import forms
from .models import EmissionCalculation

class EmissionCalculationForm(forms.ModelForm):
    class Meta:
        model = EmissionCalculation
        fields = ['transport_type', 'distance', 'passengers']
