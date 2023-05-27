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

    email = forms.EmailField(label = "Correo electrónico", required=True)
    showname = forms.CharField(label = "Nombre para mostrar", required=True, max_length=50)
    username = forms.CharField(label = "Nombre de usuario", required=True, max_length=50)
    password = forms.CharField(label = "Contraseña", required=True, max_length=50, widget=forms.PasswordInput)
    profilepic = forms.ImageField(label = "Foto de perfil", required=False)

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
    
    # groupdays = forms.MultipleChoiceField(
    #     label = "Días de reunión",
    #     required=True,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[('1','Lunes'),('2','Martes'),('3','Miércoles'),('4','Jueves'),('5','Viernes'),('6','Sábado'),('7','Domingo')],
    # )

    next_meeting = forms.DateField(
        label = "Próxima reunión",
        required=True,
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().strftime('%Y-%m-%d')}
        )
    )

    # grouppic = forms.ImageField(
    #     label = "Foto del grupo",
    #     required=False,
    # )