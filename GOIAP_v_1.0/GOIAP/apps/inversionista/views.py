from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from apps.user.models import Perfil
from .models import Inversionista

# Create your views here.
def indexInversionista(request):
	context=None
	return render(request,'inversionista/IndexInversionista.html', context)