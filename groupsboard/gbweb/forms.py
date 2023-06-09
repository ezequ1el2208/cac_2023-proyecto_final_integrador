
from django import forms
from django.forms import ModelForm, Textarea

from django.contrib.auth.forms import UserCreationForm

from .models import *

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

   
class CreateGroupForm(ModelForm):
    
    class Meta:
        model = Grupo
        fields = '__all__'


class Create_Task(ModelForm):
    
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'description':Textarea(attrs={'cols':20,'rows': 10}),
        }


