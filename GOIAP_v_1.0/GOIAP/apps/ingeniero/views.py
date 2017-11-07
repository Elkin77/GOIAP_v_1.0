from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from apps.user.models import Perfil
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required
def indexIngeniero(request):
	if validarSesion(request):
		return render(request,'ingeniero/IndexIngeniero.html')
	else:
		logout(request)
		return redirect('index')

def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Ingeniero'):
		return False
	else:
		return True