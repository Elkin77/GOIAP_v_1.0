from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil, Asignaciones
from apps.obra.models import Obra
from apps.documentos.models import Documento_contable
from apps.facturas.models import Factura
from datetime import datetime

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