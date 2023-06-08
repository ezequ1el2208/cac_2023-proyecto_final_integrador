from datetime import datetime

from django import forms
from django.forms import ModelForm, Textarea

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout  import Submit

from .models import Tarea, User

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

   
class CreateGroupForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('create_group')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('submit', 'Crear grupo'))

    nombre = forms.CharField(label = "Nombre del grupo", required=True, max_length=50)
    tipo = forms.ChoiceField(label="Tipo de grupo", required=True, choices=[('Público','Público'),('Privado','Privado')])
    tema = forms.CharField( label = "Tema del grupo", required=True, max_length=200)
    descripcion = forms.CharField(label = "Descripción del grupo", required=True, max_length=200)
    proximo_encuentro = forms.DateField(label = "Próxima reunión", required=True, widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().strftime('%Y-%m-%d')}))
    

class Create_Task(ModelForm):
    
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'description':Textarea(attrs={'cols':20,'rows': 10}),
        }


