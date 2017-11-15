from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from apps.administrador.forms import RegistroForm

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


def registrarUsuario_view(request):
    if request.method == "POST":
               
        perfil=Perfil()
      
        try:
            nombreusuario = request.POST['username']
            email=request.POST['email']
            password = request.POST['password1']
            firstName = request.POST['first_name']
            lastName = request.POST['last_name']

            user = User.objects.create_user(username=nombreusuario,
                                            email=email,
                                            password=password,
                                            first_name=firstName,
                                            last_name=lastName)

            user.is_staff = True
            user.save()
           
            nameuser =User.objects.filter(username=request.POST['username'])
            usuario1 = User.objects.get(pk=nameuser[0].id)
            perfil.fk_authUser=usuario1 
            perfil.rol= request.POST['rol']
            perfil.save()
            return render(request,"administrador/registrar_usuarios.html")   
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"administrador/registrar_usuarios.html")
    

    return render(request,'administrador/registrar_usuarios.html')



def listaUsuarios_view(request):
    usuarios= User.objects.all()
    contexto = {'listUsuarios':usuarios}
    return render(request,'administrador/lista_usuarios.html', contexto)


def eliminarUsuario_view(request, usuario_id):
    user=User.objects.get(pk=usuario_id)
    perfil = Perfil.objects.get(fk_authUser=usuario_id)
    user.delete()
    perfil.delete()
    return redirect("listaUsuarios")


def editarUsuario_view(request, usuario_id):
 
    message=None
    
    usuarios=User.objects.get(pk=usuario_id)
    perfiles = Perfil.objects.get(fk_authUser = usuario_id)



    if request.method=="POST":

        userU = request.POST['username']
        firstName= request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']

        usuarios.username = userU
        usuarios.first_name = firstName
        usuarios.last_name = lastName
        usuarios.email = email

        usuarios.save()

        perfiles.rol=request.POST['rol']
        perfiles.save()
        context={'perfiles':perfiles,'message':message}
       	return redirect("listaUsuarios")

    else:
        context={'usuarios':usuarios}
        return render(request,'administrador/editar_usuarios.html',context)
