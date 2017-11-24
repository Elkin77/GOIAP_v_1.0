from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil, Asignaciones
from apps.obra.models import Obra
from apps.documentos.models import Documento_contable, Reporte
from apps.facturas.models import Factura
from datetime import datetime
from apps.empleado.models import EmpleadoUser
from apps.contabilidad.models import Nomina

# Create your views here.
@login_required
def indexContador(request):
	if validarSesion(request):
		return render(request,'contador/IndexContador.html')
	else:
		logout(request)
		return redirect('index')
		
def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Contador'):
		return False
	else:
		return True

@login_required
def cargarDocumento(request):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		if request.method == 'POST':
			documentoContable=Documento_contable()
			try:
				documentoContable.nombre=request.POST['nombre']
				documentoContable.tipo_doc=request.POST['tipoDoc']
				documentoContable.fecha_carga=datetime.now()
				documentoContable.archivo=request.FILES['archivo']
				documentoContable.nro_paginas=request.POST['nroPag']
				documentoContable.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoContable.fk_obra=obra
				documentoContable.fk_contador= perfil
				documentoContable.estado='Por Revisar'
				documentoContable.observacion=''

				documentoContable.save()
				message="Ok, Documento Cargado!"
				context = {'message':message}
				return render(request,'contador/cargarDocumento.html',context)
			except KeyError:
				datosUser=KeyError
				context={'datosUser':datosUser}
				return redirect('cargarDocumentoContador')
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			if (len(obraPerfil)>0):
				context={'listObras':obraPerfil}
			return render(request,'contador/cargarDocumento.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def gestionarDocumentos(request):
	if validarSesion(request):
		documentoContable=Documento_contable.objects.filter(fk_contador=request.session['id'])
		context={'listDocumentos':documentoContable}
		return render(request,'contador/gestionarDocumentos.html',context)
	else:
		logout(request)
		return redirect('index')
	
@login_required
def editarDocumento(request, documento_id):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		documentoContable=Documento_contable.objects.get(pk=documento_id)
		if request.method == 'POST':
			try:
				documentoContable.nombre=request.POST['nombre']
				documentoContable.tipo_doc=request.POST['tipoDoc']
				documentoContable.fecha_carga=datetime.now()
				documentoContable.archivo=request.FILES['archivo']
				documentoContable.nro_paginas=request.POST['nroPag']
				documentoContable.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoContable.fk_obra=obra
				documentoContable.fk_contador= perfil
				documentoContable.estado='Por Revisar'
				documentoContable.observacion=''

				documentoContable.save()
				return redirect('gestionarDocumentosContador')
			except KeyError:
				documentoContable.nombre=request.POST['nombre']
				documentoContable.tipo_doc=request.POST['tipoDoc']
				documentoContable.fecha_carga=datetime.now()
				documentoContable.nro_paginas=request.POST['nroPag']
				documentoContable.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoContable.fk_obra=obra
				documentoContable.fk_contador= perfil
				documentoContable.estado='Por Revisar'
				documentoContable.observacion=''

				documentoContable.save()
				return redirect('gestionarDocumentosContador')
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			context={'documentoContable':documentoContable,'listObras':obraPerfil}
			return render(request,'contador/editarDocumento.html', context)
	else:
		logout(request)
		return redirect('index')

@login_required
def eliminarDocumento(request, documento_id):
	if validarSesion(request):
		documentoContable=Documento_contable.objects.get(pk=documento_id)
		documentoContable.delete()
		return redirect('gestionarDocumentosContador')
	else:
		logout(request)
		return redirect('index')

@login_required
def consultarObservaciones(request):
	if validarSesion(request):
		documentoContable=Documento_contable.objects.filter(fk_contador=request.session['id'])
		context={'listDocumentos':documentoContable}
		return render(request,'contador/consultarObservaciones.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def cargarFactura(request):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		if request.method=='POST':
			factura=Factura()
			factura.empresa=request.POST['empresa']
			factura.nit_empresa=request.POST['nitEmpresa']
			factura.codigo_factura=request.POST['codigo']
			factura.valor=request.POST['valor']
			factura.fecha=request.POST['fecha']
			factura.descripcion=request.POST['descripcion']
			factura.imagen=request.FILES['imagen']
			obra=Obra.objects.get(pk=request.POST['obra'])
			factura.fk_obra=obra
			factura.save()
			message="Ok, Factura Cargada!"
			context = {'message':message}
			return render(request,'contador/cargarFactura.html',context)
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			if (len(obraPerfil)>0):
				context={'listObras':obraPerfil}
			return render(request,'contador/cargarFactura.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def gestionarFacturas(request):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		asignaciones=Asignaciones.objects.filter(perfil=perfil)
		facturas=[]
		context=None
		for i in range(len(asignaciones)):
			factura=Factura.objects.filter(fk_obra=asignaciones[i].id_obra)
			for j in range(len(factura)):
				facturas.append(factura[j])
		context={'listFacturas':facturas}
		return render(request,'contador/gestionarFacturas.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def editarFactura(request, factura_id):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		factura=Factura.objects.get(pk=factura_id)
		if request.method=='POST':
			try:
				factura.empresa=request.POST['empresa']
				factura.nit_empresa=request.POST['nitEmpresa']
				factura.codigo_factura=request.POST['codigo']
				factura.valor=request.POST['valor']
				factura.fecha=request.POST['fecha']
				factura.descripcion=request.POST['descripcion']
				factura.imagen=request.FILES['imagen']
				obra=Obra.objects.get(pk=request.POST['obra'])
				factura.fk_obra=obra
				factura.save()
				return redirect('gestionarFacturasContador')
			except KeyError:
				factura.empresa=request.POST['empresa']
				factura.nit_empresa=request.POST['nitEmpresa']
				factura.codigo_factura=request.POST['codigo']
				factura.valor=request.POST['valor']
				factura.fecha=request.POST['fecha']
				factura.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				factura.fk_obra=obra
				factura.save()
				return redirect('gestionarFacturasContador')
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			if (len(obraPerfil)>0):
				context={'factura':factura,'listObras':obraPerfil}
			return render(request,'contador/editarFactura.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def eliminarFactura(request, factura_id):
	if validarSesion(request):
		factura=Factura.objects.get(pk=factura_id)
		factura.delete()
		return redirect('gestionarFacturasContador')
	else:
		logout(request)
		return redirect('index')


@login_required
def listaObrasNomina_view(request):
    if validarSesion(request):
        obras = Obra.objects.all()
        
        usuario_mixed=[]
        for i in range(len(obras)):
            users=User.objects.get(username=obras[i].fk_administrador_id.fk_authUser)
            
            aux={'id':obras[i].id,'nombre':obras[i].nombre,'direccion':obras[i].direccion,'tipo':obras[i].tipo,'estado':obras[i].estado,'nroApartamentos':obras[i].nroApartamentos,'fechaInicio':obras[i].fechaInicio, 'fechaFin':obras[i].fechaFin, 'imagen':obras[i].imagen, 'fk_administrador_id':users.username}
            usuario_mixed.append(aux)

        contexto = {'listObras':usuario_mixed}
        return render(request,'contador/listaObrasNomina.html', contexto)

    else:
        logout(request)
        return redirect('index')


@login_required
def listaTrabajadoresNomina_view(request, obra_id):
    if validarSesion(request):
        obras = Obra.objects.get(pk=obra_id)
        users=User.objects.get(username=obras.fk_administrador_id.fk_authUser)
        empleados = EmpleadoUser.objects.filter(fk_obra_id = obra_id)
        usuario_mixed=[]
        reportes_mixed2=[]
        aux={'id':obras.id,'nombre':obras.nombre,'direccion':obras.direccion,'tipo':obras.tipo,'estado':obras.estado,'nroApartamentos':obras.nroApartamentos,'fechaInicio':obras.fechaInicio, 'fechaFin':obras.fechaFin, 'imagen':obras.imagen, 'fk_administrador_id':users.username}
        usuario_mixed.append(aux)

        contexto = {'listObras':usuario_mixed, 'listEmpleados':empleados}
        return render(request,'contador/listaTrabajadoresNomina.html', contexto)

    else:
        logout(request)
        return redirect('index')


@login_required
def formularioNomina_view(request, trabajador_id):
	if validarSesion(request):
		if request.method=='POST':

			newNomina = Nomina()

			salario = request.POST['salario']
			dias_laboradosNew = request.POST['dias_laborados']
			nro_horas_diurnasNew = request.POST['nrohorasdiurnas']
			nro_horas_nocturnasNew = request.POST['nrohorasnocturnas']
			nro_horas_dominicalesNew = request.POST['nrohorasdominicales']
			aux_alimentacionNew = request.POST['auxalimentacion']
			bonificacionesNew = request.POST['bonificaciones']


			valor_dia = (int(dias_laboradosNew)/30)

			basicoNew = (int(salario)/30) * 15
			horas_extras_diurnas = (((int(salario) / 30) / 8) * 1.25) * int(nro_horas_diurnasNew);
			horas_extras_nocturnas = (((int(salario) / 30) / 8) * 1.75) * int(nro_horas_nocturnasNew);
			dominicales = (((int(salario) / 30) / 8) * 1.75) * int(nro_horas_dominicalesNew);

			if (int(salario) < 1475434):
				aux_transporteNew = (83140 / 30) * int(dias_laboradosNew)

			else:
				aux_transporteNew = 0;

			totalDevengado = float(basicoNew) + float(horas_extras_diurnas) + float(horas_extras_nocturnas) + float(dominicales) + float(aux_transporteNew) + float(aux_alimentacionNew)

            #DEDUCCIONES
            
			salud = (totalDevengado - aux_transporteNew) * 0.04
			pension = (totalDevengado - aux_transporteNew) * 0.04
			totalDeducciones = salud + pension
			netoPagar = totalDevengado - float(totalDeducciones) + float(aux_alimentacionNew) + float(bonificacionesNew)
	        

			newNomina.dias_laborados = dias_laboradosNew
			newNomina.basico = basicoNew
			newNomina.bonificaciones = bonificacionesNew
			newNomina.nro_horas_diurnas = nro_horas_diurnasNew
			newNomina.nro_horas_nocturnas = nro_horas_nocturnasNew
			newNomina.nro_horas_dominicales = nro_horas_dominicalesNew
			newNomina.valor_horas_diurnas = horas_extras_diurnas
			newNomina.valor_horas_nocturnas = horas_extras_nocturnas
			newNomina.valor_horas_dominicales = dominicales
			newNomina.aux_transporte = aux_transporteNew
			newNomina.aux_alimentacion = aux_alimentacionNew
			newNomina.aporte_salud = salud
			newNomina.aporte_pension = pension
			newNomina.retencion_fuente = 0
			newNomina.total_devengado = totalDevengado
			newNomina.total_deducciones = totalDeducciones
			newNomina.neto_pagar = netoPagar
			newNomina.fecha = datetime.now()

			empleado = EmpleadoUser.objects.get(pk=trabajador_id)
			newNomina.fk_empleado_id = empleado.id
			newNomina.save()
			return redirect('listaObrasNomina')
			
		else:
			trabajador = EmpleadoUser.objects.get(pk = trabajador_id)
			contexto = {'datosTrabajador':trabajador}
		return render(request,'contador/formularioNomina.html', contexto)
	else:
		logout(request)
		return redirect('index')


@login_required
def nominasGeneradas_view(request, trabajador_id):
    if validarSesion(request):
        nominas = Nomina.objects.filter(fk_empleado_id=trabajador_id)
        empleados = EmpleadoUser.objects.get(pk = trabajador_id)
        contexto = {'listNominas':nominas, 'trabajador':empleados}
        return render(request,'contador/nominasGeneradas.html', contexto)

    else:
        logout(request)
        return redirect('index')

@login_required
def eliminarRegistroNomina(request, nomina_id):
	if validarSesion(request):
		nomina=Nomina.objects.get(pk=nomina_id)
		nomina.delete()
		return redirect('listaObrasNomina')
	else:
		logout(request)
		return redirect('index')


@login_required
def informacionNomina_view(request, nomina_id):
	if validarSesion(request):
		if request.method=='POST':
			return redirect('listaObrasNomina')
			
		else:
			nomina = Nomina.objects.get(pk = nomina_id)
			trabajador = EmpleadoUser.objects.get(pk = nomina.fk_empleado_id)
			contexto = {'dataNomina':nomina, 'datosTrabajador':trabajador}
		return render(request,'contador/informacionNomina.html', contexto)
	else:
		logout(request)
		return redirect('index')