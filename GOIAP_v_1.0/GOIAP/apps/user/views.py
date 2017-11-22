from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Perfil
from .forms import login_form
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	message=""
	context=None
	if request.method=='POST':
		form=login_form(request.POST)
		if form.is_valid():
			usernameLlega=request.POST['user']
			passwordLlega=request.POST['password']
			user=authenticate(username=usernameLlega, password= passwordLlega)
			if user is not None:
				if user.is_active:
					login(request,user)
					usuario = User.objects.get(username=request.POST['user'])
					perfil=Perfil.objects.get(fk_authUser=usuario.pk)
					if perfil.rol == "Administrador":
						request.session['id']=usuario.pk
						return redirect('indexAdmin')
					else:
						if perfil.rol == "Arquitecto":
							request.session['id']=usuario.pk
							return redirect('indexArquitecto')
						else:
							if perfil.rol == "Contador":
								request.session['id']=usuario.pk
								return redirect('indexContador')
							else:
								if perfil.rol == "Empleado":
									request.session['id']=usuario.pk
									return redirect('indexEmpleado')
								else:
									if perfil.rol == "Ingeniero":
										request.session['id']=usuario.pk
										return redirect('indexIngeniero')
									else:
										if perfil.rol == "Inversionista":
											request.session['id']=usuario.pk
											return redirect('indexInversionista')
				else:
					message="Tu usuario esta inactivo"
					context = {'message':message}
					return render(request,'user/Index.html', context)
			else:
				message="Id usuario y so contraseña incorrecta2"
				context = {'message':message,}
				return render(request,'user/Index.html', context)
		else:
			message="Id usuario y/o contraseña incorrecta3"
			context = {'message':message}
			return render(request,'user/Index.html', context)
	else:#debo mostrar mi sistema de noticias
		return render(request,'user/Index.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')