from django import forms
from .models import Student, Track


class StudentForm(forms.ModelForm):
    class Meta:
        model = ModelName  # modify
        fields = ('fieldname', 'fieldname', 'fieldname', 'fieldname')
        widgets = {
            'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
            'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
            'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
        }
