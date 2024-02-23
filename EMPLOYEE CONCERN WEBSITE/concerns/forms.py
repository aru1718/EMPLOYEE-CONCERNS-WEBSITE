from django import forms
from .models import Concern

class ConcernForm(forms.ModelForm):
    class Meta:
        model = Concern
        fields = ['title', 'description', 'employee_name']
