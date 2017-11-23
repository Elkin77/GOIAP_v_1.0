from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil, Asignaciones
from apps.obra.models import Obra
from apps.documentos.models import Documento_ingenieria
from datetime import datetime


# Create your views here.
@login_required
def indexIngeniero(request):
	if validarSesion(request):
		return render(request,'ingeniero/IndexIngeniero.html')
	else:
		logout(request)
		return redirect('index')

def validarSesion(request):
	user=User.objects.get(pk=request.session["id"])
	perfil=Perfil.objects.get(fk_authUser=user)
	if(perfil.rol != 'Ingeniero'):
		return False
	else:
		return True

@login_required
def cargarDocumento(request):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		if request.method == 'POST':
			documentoIngenieria=Documento_ingenieria()
			try:
				documentoIngenieria.nombre=request.POST['nombre']
				documentoIngenieria.tipo_doc=request.POST['tipoDoc']
				documentoIngenieria.fecha_carga=datetime.now()
				documentoIngenieria.archivo=request.FILES['archivo']
				documentoIngenieria.nro_paginas=request.POST['nroPag']
				documentoIngenieria.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoIngenieria.fk_obra=obra
				documentoIngenieria.fk_arquitecto= perfil

				documentoIngenieria.save()
				message="Ok, Documento Cargado!"
				context = {'message':message}
				return render(request,'ingeniero/IndexIngeniero.html',context)
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
			return render(request,'ingeniero/cargarDocumento.html',context)
	else:
		logout(request)
		return redirect('index')

@login_required
def gestionarDocumentos(request):
	if validarSesion(request):
		documentoIngenieria=Documento_ingenieria.objects.filter(fk_ingeniero=request.session['id'])
		context={'listDocumentos':documentoIngenieria}
		return render(request,'ingeniero/gestionarDocumentos.html',context)
	else:
		logout(request)
		return redirect('index')
	
@login_required
def editarDocumento(request, documento_id):
	if validarSesion(request):
		user=User.objects.get(pk=request.session["id"])
		perfil=Perfil.objects.get(fk_authUser=user)
		documentoIngenieria=Documento_ingenieria.objects.get(pk=documento_id)
		if request.method == 'POST':
			try:
				documentoIngenieria.nombre=request.POST['nombre']
				documentoIngenieria.tipo_doc=request.POST['tipoDoc']
				documentoIngenieria.fecha_carga=datetime.now()
				documentoIngenieria.archivo=request.FILES['archivo']
				documentoIngenieria.nro_paginas=request.POST['nroPag']
				documentoIngenieria.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoIngenieria.fk_obra=obra
				documentoIngenieria.fk_arquitecto= perfil

				documentoIngenieria.save()
				return redirect('gestionarDocumentos')
			except KeyError:
				documentoIngenieria.nombre=request.POST['nombre']
				documentoIngenieria.tipo_doc=request.POST['tipoDoc']
				documentoIngenieria.fecha_carga=datetime.now()
				documentoIngenieria.nro_paginas=request.POST['nroPag']
				documentoIngenieria.descripcion=request.POST['descripcion']
				obra=Obra.objects.get(pk=request.POST['obra'])
				documentoIngenieria.fk_obra=obra
				documentoIngenieria.fk_arquitecto= perfil

				documentoIngenieria.save()
				return redirect('gestionarDocumentos')
		else:
			asignaciones=Asignaciones.objects.filter(perfil=perfil)
			obraPerfil=[]
			context=None
			for i in range(len(asignaciones)):
				obra=Obra.objects.get(pk=asignaciones[i].id_obra)
				obraPerfil.append(obra)
			context={'documentoIngenieria':documentoIngenieria,'listObras':obraPerfil}
			return render(request,'ingeniero/editarDocumento.html', context)
	else:
		logout(request)
		return redirect('index')

@login_required
def eliminarDocumento(request, documento_id):
	if validarSesion(request):
		documentoIngenieria=Documento_ingenieria.objects.get(pk=documento_id)
		documentoIngenieria.delete()
		return redirect('gestionarDocumentos')
	else:
		logout(request)
		return redirect('index')

@login_required
def consultarObservaciones(request):
	if validarSesion(request):
		documentoIngenieria=Documento_ingenieria.objects.filter(fk_ingeniero=request.session['id'])
		context={'listDocumentos':documentoIngenieria}
		return render(request,'ingeniero/consultarObservaciones.html',context)
	else:
		logout(request)
		return redirect('index')