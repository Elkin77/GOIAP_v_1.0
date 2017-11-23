from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.user.models import Perfil, Asignaciones
from apps.obra.models import Obra
from apps.documentos.models import Documento_arquitectura
from datetime import datetime
import os


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