from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border'}))
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
