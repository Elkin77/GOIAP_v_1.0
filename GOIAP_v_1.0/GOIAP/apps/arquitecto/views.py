from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil, Asignaciones
from apps.obra.models import Obra
from apps.documentos.models import Documento_arquitectura
from apps.inventario.models import Inventario
from datetime import datetime


# Create your views here.
@login_required
def indexArquitecto(request):
	if validarSesion(request):
		return render(request,'arquitecto/IndexArquitecto.html')
	else:
		logout(request)
		return redirect('index')


def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Arquitecto'):
		return False
	else:
		return True

@login_required
def cargarDocumento(request):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		if request.method == 'POST':
			documentoArquitectura=Documento_arquitectura()
			try:
				documentoArquitectura.nombre=request.POST['nombre']
				documentoArquitectura.tipo_doc=request.POST['tipoDoc']
				documentoArquitectura.fecha_carga=datetime.now()
				documentoArquitectura.archivo=request.FILES['archivo']
				documentoArquitectura.nro_paginas=request.POST['nroPag']
				documentoArquitectura.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoArquitectura.fk_obra=obra
				documentoArquitectura.fk_arquitecto= perfil
				documentoArquitectura.estado='Por Revisar'
				documentoArquitectura.observacion=''

				documentoArquitectura.save()
				message="Ok, Documento Cargado!"
				context = {'message':message}
				return render(request,'arquitecto/cargarDocumento.html',context)
			except KeyError:
				datosUser=KeyError
				context={'datosUser':datosUser}
				return redirect('cargarDocumento')
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			if (len(obraPerfil)>0):
				context={'listObras':obraPerfil}
			return render(request,'arquitecto/cargarDocumento.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def gestionarDocumentos(request):
	if validarSesion(request):
		documentoArquitectura=Documento_arquitectura.objects.filter(fk_arquitecto=request.session['id'])
		context={'listDocumentos':documentoArquitectura}
		return render(request,'arquitecto/gestionarDocumentos.html',context)
	else:
		logout(request)
		return redirect('index')
	
@login_required
def editarDocumento(request, documento_id):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		documentoArquitectura=Documento_arquitectura.objects.get(pk=documento_id)
		if request.method == 'POST':
			try:
				documentoArquitectura.nombre=request.POST['nombre']
				documentoArquitectura.tipo_doc=request.POST['tipoDoc']
				documentoArquitectura.fecha_carga=datetime.now()
				documentoArquitectura.archivo=request.FILES['archivo']
				documentoArquitectura.nro_paginas=request.POST['nroPag']
				documentoArquitectura.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoArquitectura.fk_obra=obra
				documentoArquitectura.fk_arquitecto= perfil
				documentoArquitectura.estado='Por Revisar'
				documentoArquitectura.observacion=''

				documentoArquitectura.save()
				return redirect('gestionarDocumentos')
			except KeyError:
				documentoArquitectura.nombre=request.POST['nombre']
				documentoArquitectura.tipo_doc=request.POST['tipoDoc']
				documentoArquitectura.fecha_carga=datetime.now()
				documentoArquitectura.nro_paginas=request.POST['nroPag']
				documentoArquitectura.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoArquitectura.fk_obra=obra
				documentoArquitectura.fk_arquitecto= perfil
				documentoArquitectura.estado='Por Revisar'
				documentoArquitectura.observacion=''

				documentoArquitectura.save()
				return redirect('gestionarDocumentos')
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			context={'documentoArquitectura':documentoArquitectura,'listObras':obraPerfil}
			return render(request,'arquitecto/editarDocumento.html', context)
	else:
		logout(request)
		return redirect('index')

@login_required
def eliminarDocumento(request, documento_id):
	if validarSesion(request):
		documentoArquitectura=Documento_arquitectura.objects.get(pk=documento_id)
		documentoArquitectura.delete()
		return redirect('gestionarDocumentos')
	else:
		logout(request)
		return redirect('index')

@login_required
def consultarObservaciones(request):
	if validarSesion(request):
		documentoArquitectura=Documento_arquitectura.objects.filter(fk_arquitecto=request.session['id'])
		context={'listDocumentos':documentoArquitectura}
		return render(request,'arquitecto/consultarObservaciones.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def crearInventario(request):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		if request.method=='POST':
			inventario=Inventario()
			inventario.nombre=request.POST['nombre']
			inventario.tipo_inventario=request.POST['tipoInventario']
			inventario.fecha_creacion=datetime.now()
			inventario.estado=request.POST['estado']
			inventario.descripcion=request.POST['descripcion']
			inventario.nro_articulos=request.POST['nroArticulos']
			obra=Obra.objects.get(pk=request.POST['obra'])
			inventario.fk_obra=obra

			inventario.save()
			message="Ok, Inventario Creado!"
			context = {'message':message}
			return render(request,'arquitecto/crearInventario.html',context)
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			context={'listObras':obraPerfil}
			return render(request,'arquitecto/crearInventario.html', context)
	else:
		logout(request)
		return redirect('index')

@login_required
def gestionarInventario(request):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		asignaciones=Asignaciones.objects.filter(perfil=perfil)
		inventarios=[]
		context=None
		for i in range(len(asignaciones)):
			inventario=Inventario.objects.filter(fk_obra=asignaciones[i].id_obra)
			for j in range(len(inventario)):
				inventarios.append(inventario[j])
		context={'listInventarios':inventarios}
		return render(request,'arquitecto/gestionarInventario.html',context)
	else:
		logout(request)
		return redirect('index')


@login_required
def editarInventario(request, inventario_id):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		inventario=Inventario.objects.get(pk=inventario_id)
		if request.method=='POST':
			inventario.nombre=request.POST['nombre']
			inventario.tipo_inventario=request.POST['tipoInventario']
			inventario.fecha_creacion=datetime.now()
			inventario.estado=request.POST['estado']
			inventario.descripcion=request.POST['descripcion']
			inventario.nro_articulos=request.POST['nroArticulos']
			obra=Obra.objects.get(pk=request.POST['obra'])
			inventario.fk_obra=obra

			inventario.save()
			return redirect('gestionarInventarioArquitecto')
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			context={'inventario':inventario,'listObras':obraPerfil}
			return render(request,'arquitecto/editarInventario.html', context)
	else:
		logout(request)
		return redirect('index')

@login_required
def eliminarInventario(request, inventario_id):
	if validarSesion(request):
		inventario=Inventario.objects.get(pk=inventario_id)
		inventario.delete()
		return redirect('gestionarInventarioArquitecto')
	else:
		logout(request)
		return redirect('index')


