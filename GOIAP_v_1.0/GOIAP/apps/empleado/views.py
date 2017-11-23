from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from apps.user.models import Perfil, Asignaciones
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
				return redirect('indexEmpleado')	
			except KeyError:
				datosUser=KeyError
				context={'datosUser':datosUser}
				return render(request,"empleado/cargar_reporte.html",context)

		else:
			asignation = Asignaciones.objects.filter(perfil = request.session["id"])	
			
			obra_mixed=[]
			for i in range(len(asignation)):
				obra=Obra.objects.get(pk=asignation[i].id_obra)
				aux={'id':asignation[i].id_obra,'nombre':obra.nombre}
				obra_mixed.append(aux)

			context={'listObras':obra_mixed}
			return render(request,'empleado/cargar_reporte.html',context)
		

	else:
		logout(request)
		return redirect('index')		