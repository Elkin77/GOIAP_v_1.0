from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil, Asignaciones
from apps.obra.models import Obra
from apps.documentos.models import Reporte
from apps.empleado.models import EmpleadoUser


# Create your views here.
@login_required
def indexInversionista(request):
	if validarSesion(request):
		return render(request,'inversionista/IndexInversionista.html')
	else:
		logout(request)
		return redirect('index')

def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Inversionista'):
		return False
	else:
		return True


@login_required
def obrasAsignadas_view(request):
    if validarSesion(request):
        asignation = Asignaciones.objects.filter(perfil = request.session["id"])
        
        usuario_mixed=[]
        for i in range(len(asignation)):
            obra=Obra.objects.get(pk=asignation[i].id_obra)
            aux={'id':asignation[i].id,'fecha_solicitud':asignation[i].fecha_solicitud,'id_obra':asignation[i].id_obra,'descripcion':asignation[i].descripcion,'nombreObra':obra.nombre,'imagen':obra.imagen}
            usuario_mixed.append(aux)

        contexto = {'listObras':usuario_mixed}
        return render(request,'inversionista/obras_asignadas.html', contexto)

    else:
        logout(request)
        return redirect('index')

@login_required
def infoObra_view(request, obra_id):
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
                aux2={'imagen':reportes[i].imagen,'id':reportes[i].id,'nombre':reportes[i].nombre,'tipo_reporte':reportes[i].tipo_reporte,'fecha_carga':reportes[i].fecha_carga,'horas_empleadas':reportes[i].horas_empleadas,'descripcion':reportes[i].descripcion,'fk_empleado_id':user.username}
                reportes_mixed2.append(aux2)

        contexto = {'listObras':usuario_mixed, 'listEmpleados':empleados, 'listReportes':reportes_mixed2}
        return render(request,'inversionista/info_obra.html', contexto)

    else:
        logout(request)
        return redirect('index')