from __future__ import unicode_literals
from .models import UsersEmails
from django import forms

from django.db import models



class EmailsForm(forms.ModelForm):
	class Meta :
		model=UsersEmails
		fields = '__all__'
		widgets = {
            'user_email': forms.TextInput(attrs={'class': 'form-control'}),
        }
		
		