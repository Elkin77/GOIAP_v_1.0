from django import forms
from apps.user.models import Perfil
from apps.obra.models import Obra
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class ObraForm(forms.ModelForm):
	class Meta:
		model = Obra
		fields = [
				'nombre',
				'direccion',
				'tipo',
				'estado',
				'nroApartamentos',

		]
		labels = {
				'nombre': 'Nombre de Obra',
				'direccion': 'Direccion',
				'tipo': 'Tipo de Obra',
				'estado': 'Estado de Obra',
				'nroApartamentos': 'Nro Apartamentos',
		}

		widgets = {
				'nombre': forms.TextInput(attrs={'class':'form-control'}),
				'direccion': forms.TextInput(attrs={'class':'form-control'}),
				'tipo': forms.TextInput(attrs={'class':'form-control'}),
				'estado': forms.TextInput(attrs={'class':'form-control'}),
				'nroApartamentos': forms.NumberInput(attrs={'class':'form-control'})
		}
