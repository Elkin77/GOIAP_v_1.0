from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil
from .models import Arquitecto

# Create your views here.
@login_required
def indexArquitecto(request):
	if validarSesion(request):
		return render(request,'arquitecto/IndexArquitecto.html')
	else:
		logout(request)
		return redirect('index')


def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Arquitecto'):
		return False
	else:
		return True