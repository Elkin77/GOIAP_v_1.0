from django import forms
from apps.user.models import Perfil
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [

				'username',
				'first_name',
				'last_name',
				'email',
		]
		labels = {
				'username': 'Usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo'	,	


		}
