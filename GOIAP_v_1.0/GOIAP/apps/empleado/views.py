from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from apps.user.models import Perfil
from apps.obra.models import Obra
from apps.documentos.models import Reporte
from django.contrib.auth import authenticate, login, logout
from .models import EmpleadoUser
from datetime import datetime

# Create your views here.
@login_required
def indexEmpleado(request):
	if validarSesion(request):	
		return render(request,'empleado/IndexEmpleado.html')
	else:
		logout(request)
		return redirect('index')

def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Empleado'):
		return False
	else:
		return True


@login_required
def cargarReporte_view(request):
	if validarSesion(request):
		message=None
		if request.method == "POST":
			reporte=Reporte()
			try:
				reporte.nombre = request.POST['nombre']
				reporte.tipo_reporte=request.POST['tipo']
				reporte.fecha_carga = datetime.now()

				reporte.imagen = request.FILES['imagen']
				reporte.horas_empleadas = request.POST['hrempleadas']
				reporte.descripcion = request.POST['descripcion']

				user=User.objects.get(pk=request.session["id"])
				perfil=Perfil.objects.get(fk_authUser=user.id)
				reporte.fk_empleado = perfil
				reporte_id = Obra.objects.get(pk=request.POST['obra'])
				reporte.fk_obra=reporte_id
				reporte.save()
				message="Ok, Usuario Registrado!"
				context = {'message':message}
				return render(request,'empleado/cargar_reporte.html', context)
				return redirect('cargarReporte')	
			except KeyError:
				datosUser=KeyError
				context={'datosUser':datosUser}
				return render(request,"empleado/cargar_reporte.html",context)

		else:
			obras = Obra.objects.all()
			context={'listObras':obras}
			return render(request,'empleado/cargar_reporte.html',context)
		

	else:
		logout(request)
		return redirect('index')		