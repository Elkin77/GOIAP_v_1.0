from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil


# Create your views here.
@login_required
def indexAdmin(request):
	if validarSesion(request):
		return render(request,'administrador/IndexAdmin.html')
	else:
		logout(request)
		return redirect('index')



def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Administrador'):
		return False
	else:
		return True

