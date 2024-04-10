# forms.py

from django import forms
from ..models import Staffdatamodel


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staffdatamodel
        fields = ['Staff_Firstname', 'Staff_Password']  # Add more fields as needed
