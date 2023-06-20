
from django import forms
from django.forms import ModelForm, Textarea

from django.contrib.auth.forms import UserCreationForm

from .models import *

from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Error!!! Ya hay un usuario inscripto con ese e-mail")

        return self.cleaned_data
   
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

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        help_texts = {
            'password': (''),
        }
        fields = ['username', 'first_name', 'last_name', 'email']
        
