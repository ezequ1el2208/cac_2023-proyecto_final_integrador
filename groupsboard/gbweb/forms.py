from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout  import Submit


class CreateUserForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('create_user')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Crear usuario'))
    
    nombre = forms.CharField(label = "Nombre:", required=True, max_length=100)
    apellido = forms.CharField(label = "Apellido:", required=True, max_length=100)
    email = forms.EmailField(label = "Email", required=True)
    dni = forms.IntegerField(label = "DNI", required=True)
    username = forms.CharField(label = "Nombre para mostrar", required=True, max_length=50)
    password = forms.CharField(label = "Contraseña", max_length=50, widget=forms.PasswordInput)
   
class CreateGroupForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('create_group')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-group'
        self.helper.add_input(Submit('submit', 'Crear grupo'))

    groupname = forms.CharField(
        label = "Nombre del grupo",
        required=True,
        max_length=50,
    )

    grouptype = forms.ChoiceField(
        label="Tipo de grupo",
        required=True,
        choices=[('1','Público'),('2','Privado')],
    )

    grouptheme = forms.CharField(
        label = "Tema del grupo",
        required=True,
        max_length=200,
    )

    groupdescription = forms.CharField(
        label = "Descripción del grupo",
        required=True,
        max_length=200,
    )

    next_meeting = forms.DateField(
        label = "Próxima reunión",
        required=True,
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().strftime('%Y-%m-%d')}
        )
    )

