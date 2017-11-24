from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil, Asignaciones
from apps.obra.models import Obra
from apps.documentos.models import Reporte
from apps.empleado.models import EmpleadoUser
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
                perfil=Perfil.objects.get(fk_authUser=user.id)

                obraNew.fk_administrador_id = perfil
                obraNew.imagen = request.FILES['imagen']
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
def registrarEmpleados_view(request, obra_id):
    if validarSesion(request):
        message=None
        if request.method == "POST":
                   
            empleados=EmpleadoUser()
          
            try:
                empleados.nombre = request.POST['nombre']
                empleados.cargo=request.POST['cargo']
                empleados.documento = request.POST['documento']
                empleados.salario = request.POST['salario']
                empleados.fecha_ingreso = request.POST['fecha']
                empleados.telefono = request.POST['telefono']
                empleados.rh = request.POST['rh']
                empleados.correo = request.POST['correo']
                obra=Obra.objects.get(pk=obra_id)
                empleados.fk_obra_id=obra.id
                empleados.save()
                message="Ok, Usuario Registrado!"
                context = {'message':message}
                return render(request,'administrador/registrar_empleados.html', context)
                return redirect('registrarEmpleados')  
            except KeyError:
                datosUser=KeyError
                context={'datosUser':datosUser}
                return render(request,"administrador/registrar_empleados.html")
        return render(request,'administrador/registrar_empleados.html')

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
def listaObras_view(request):
    if validarSesion(request):
        obras = Obra.objects.all()
        
        usuario_mixed=[]
        for i in range(len(obras)):
            users=User.objects.get(username=obras[i].fk_administrador_id.fk_authUser)
            
            aux={'id':obras[i].id,'nombre':obras[i].nombre,'direccion':obras[i].direccion,'tipo':obras[i].tipo,'estado':obras[i].estado,'nroApartamentos':obras[i].nroApartamentos,'fechaInicio':obras[i].fechaInicio, 'fechaFin':obras[i].fechaFin, 'imagen':obras[i].imagen, 'fk_administrador_id':users.username}
            usuario_mixed.append(aux)

        contexto = {'listObras':usuario_mixed}
        return render(request,'administrador/lista_obras.html', contexto)

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
def eliminarObra_view(request, obra_id):
    if validarSesion(request):
        obra=Obra.objects.get(pk=obra_id)
        obra.delete()
        return redirect("listaObras")
    else:
        logout(request)
        return redirect('index')


@login_required
def eliminarAsignacion_view(request, user_id):
    if validarSesion(request):
        asignation=Asignaciones.objects.get(pk=user_id)
        asignation.delete()
        return redirect("listaUsuarios")
    else:
        logout(request)
        return redirect('index')


@login_required
def eliminarReporte_view(request, reporte_id):
    if validarSesion(request):
        reportes=Reporte.objects.get(pk=reporte_id)
        reportes.delete()
        return redirect("listaObras")
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

@login_required
def editarObra_view(request, obra_id):
    if validarSesion(request):
        message=None
        obras=Obra.objects.get(pk=obra_id)
        
        if request.method=="POST":

            nombreObra = request.POST['nombre']
            direccionObra= request.POST['direccion']
            tipoObra= request.POST['tipo']
            estadoObra= request.POST['estado']
            apartamentosObra = request.POST['nroApartamentos']
            fechaFinObra = request.POST['fechaFin']

            obras.nombre = nombreObra
            obras.direccion = direccionObra
            obras.tipo = tipoObra
            obras.estado = estadoObra
            obras.nroApartamentos = apartamentosObra
            obras.fechaFin = fechaFinObra
            obras.save()

            context={'message':message}
            return redirect("listaObras")

        else:
            context={'obras':obras}
            return render(request,'administrador/editar_obras.html',context)
    else:
        logout(request)
        return redirect('index')


@login_required
def verObra_view(request, obra_id):
    if validarSesion(request):
        reportes = Reporte.objects.filter(fk_obra_id = obra_id)
        obras = Obra.objects.get(pk=obra_id)
        users=User.objects.get(username=obras.fk_administrador_id.fk_authUser)
        empleados = EmpleadoUser.objects.filter(fk_obra_id = obra_id)
        usuario_mixed=[]
        reportes_mixed2=[]
        aux={'id':obras.id,'nombre':obras.nombre,'direccion':obras.direccion,'tipo':obras.tipo,'estado':obras.estado,'nroApartamentos':obras.nroApartamentos,'fechaInicio':obras.fechaInicio, 'fechaFin':obras.fechaFin, 'imagen':obras.imagen, 'fk_administrador_id':users.username}
        usuario_mixed.append(aux)

        for i in range(len(reportes)):
                user=User.objects.get(pk=reportes[i].fk_empleado_id)
                print(reportes[i].tipo_reporte)
                print("**************")
                print("**************")
                aux2={'imagen':reportes[i].imagen,'id':reportes[i].id,'nombre':reportes[i].nombre,'tipo_reporte':reportes[i].tipo_reporte,'fecha_carga':reportes[i].fecha_carga,'horas_empleadas':reportes[i].horas_empleadas,'descripcion':reportes[i].descripcion,'fk_empleado_id':user.username}
                reportes_mixed2.append(aux2)

        contexto = {'listObras':usuario_mixed, 'listEmpleados':empleados, 'listReportes':reportes_mixed2}
        return render(request,'administrador/ver_obra.html', contexto)

    else:
        logout(request)
        return redirect('index')



@login_required
def asignarObras_view(request, user_id):
    if validarSesion(request):
        message=None
        if request.method == "POST":
            asignacion=Asignaciones()
            try:
                asignacion.fecha_solicitud = datetime.now()
                asignacion.descripcion = request.POST['descripcion']
                usuario=Perfil.objects.get(pk=user_id)
                asignacion.perfil=usuario
                asignacion.id_obra=request.POST['obra']
                asignacion.save()
                message="Ok, Usuario Registrado!"
                context = {'message':message}
                return redirect('listaUsuarios')    
            except KeyError:
                datosUser=KeyError
                context={'datosUser':datosUser}
                return render(request,"administrador/asignar_obras.html",context)

        else:
            asignation = Asignaciones.objects.filter(perfil = user_id)
            obra_mixed=[]
            for i in range(len(asignation)):
                obra=Obra.objects.get(pk=asignation[i].id_obra)
                aux={'id':asignation[i].id,'fecha_solicitud':asignation[i].fecha_solicitud,'id_obra':obra.nombre,'descripcion':asignation[i].descripcion}
                obra_mixed.append(aux)
            users = User.objects.get(pk=user_id)
            obras = Obra.objects.all()
            context={'listAsignaciones':obra_mixed, 'listUsuarios':users, 'listObras':obras}
            return render(request,'administrador/asignar_obras.html',context)
        

    else:
        logout(request)
        return redirect('index')        