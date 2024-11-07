from django import forms
from .models import *


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('fullname', 'age', 'image', 'phone', 'email', 'password')

class WorkForm(forms.ModelForm):
    
    class Meta:
        model = Work
        fields = ('title', 'description', 'category', 'image', 'video', 'user', 'region', 'address')

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = ('user', 'message', 'price', 'duration', 'status')
