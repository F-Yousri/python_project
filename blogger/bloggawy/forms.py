from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
   
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


	

# class ModelName(forms.ModelForm):
#     class Meta:
#         model = ModelName  # modify
#         fields = ('fieldname', 'fieldname', 'fieldname', 'fieldname')
#         widgets = {
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#         }

