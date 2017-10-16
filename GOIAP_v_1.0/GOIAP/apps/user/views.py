from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Perfil

# Create your views here.
def index(request):
	context=None
	return render(request,'user/Index.html', context)