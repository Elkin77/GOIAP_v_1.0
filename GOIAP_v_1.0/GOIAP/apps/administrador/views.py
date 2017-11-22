from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil
from apps.obra.models import Obra
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from apps.administrador.forms import ObraForm
from itertools import chain
from django.db.models import F
from datetime import datetime
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

@login_required
def registrarUsuario_view(request):
    if validarSesion(request):
        message=None
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
                message="Ok, Usuario Registrado!"
                context = {'message':message}
                return render(request,'administrador/registrar_usuarios.html', context)
                return redirect('registrarUsuarios')  
            except KeyError:
                datosUser=KeyError
                context={'datosUser':datosUser}
                return render(request,"administrador/registrar_usuarios.html")
    

        return render(request,'administrador/registrar_usuarios.html')

    else:
        logout(request)
        return redirect('index')



@login_required
def registrarObra_view(request):
    if validarSesion(request):
        message=None
        if request.method == "POST":
                   
            obraNew=Obra()
          
            try:
                obraNew.nombre = request.POST['nombre']
                obraNew.direccion=request.POST['direccion']
                obraNew.tipo = request.POST['tipo']
                obraNew.estado = request.POST['estado']
                obraNew.nroApartamentos = request.POST['nroapartamentos']
                obraNew.fechaInicio = request.POST['fecha']
                user=User.objects.get(pk=request.session["id"])
                perfil=Perfil.objects.get(fk_authUser=user)
                obraNew.fk_administrador = perfil
                obraNew.save()
                message="Ok, Usuario Registrado!"
                context = {'message':message}
                return render(request,'administrador/registrar_obras.html', context)
                return redirect('registrarObras')  
            except KeyError:
                datosUser=KeyError
                context={'datosUser':datosUser}
                return render(request,"administrador/registrar_obras.html")
        return render(request,'administrador/registrar_obras.html')

    else:
        logout(request)
        return redirect('index')



@login_required
def listaUsuarios_view(request):
    if validarSesion(request):
        if request.method=="POST" and request.POST['rolfilter'] != 'Todos':
            perfiles = Perfil.objects.filter(rol = request.POST['rolfilter'])
            

            usuario_mixed=[]
            for i in range(len(perfiles)):
                usuarios=User.objects.get(username=perfiles[i].fk_authUser)
                aux={'id':usuarios.id,'username':usuarios.username,'first_name':usuarios.first_name,'last_name':usuarios.last_name,'email':usuarios.email,'is_active':usuarios.is_active,'rol':request.POST['rolfilter']}
                usuario_mixed.append(aux)

            contexto = {'listUsuarios':usuario_mixed}
            return render(request,'administrador/lista_usuarios.html', contexto)

        else:
            usuarios= User.objects.all()
            usuario_mixed=[]
            for i in range(len(usuarios)):
                user=User.objects.get(pk=usuarios[i].id)
                perfiles = Perfil.objects.get(fk_authUser = user)
                aux={'id':usuarios[i].id,'username':usuarios[i].username,'first_name':usuarios[i].first_name,'last_name':usuarios[i].last_name,'email':usuarios[i].email,'is_active':usuarios[i].is_active,'rol':perfiles.rol}
                usuario_mixed.append(aux)

            contexto = {'listUsuarios':usuario_mixed}
            return render(request,'administrador/lista_usuarios.html', contexto)
    else:
        logout(request)
        return redirect('index')


@login_required
def eliminarUsuario_view(request, usuario_id):
    if validarSesion(request):
        user=User.objects.get(pk=usuario_id)
        perfil = Perfil.objects.get(fk_authUser=usuario_id)
        user.delete()
        perfil.delete()
        return redirect("listaUsuarios")
    else:
        logout(request)
        return redirect('index')


@login_required
def editarUsuario_view(request, usuario_id):
    if validarSesion(request):
        message=None
        usuarios=User.objects.get(pk=usuario_id)
        perfiles = Perfil.objects.get(fk_authUser = usuario_id)
        if request.method=="POST":

            userU = request.POST['username']
            firstName= request.POST['first_name']
            lastName = request.POST['last_name']
            email = request.POST['email']
            activacion = request.POST['is_active']

            usuarios.username = userU
            usuarios.first_name = firstName
            usuarios.last_name = lastName
            usuarios.email = email
            usuarios.is_active = activacion

            usuarios.save()

            perfiles.rol=request.POST['rol']
            perfiles.save()
            context={'perfiles':perfiles,'message':message}
            return redirect("listaUsuarios")

        else:
            context={'usuarios':usuarios}
            return render(request,'administrador/editar_usuarios.html',context)
    else:
        logout(request)
        return redirect('index')

