from django.conf.urls import url
from . import views
from apps.administrador import views as admin_views
from apps.arquitecto import views as arquitecto_views
from apps.contador import views as contador_views
from apps.empleado import views as empleado_views
from apps.ingeniero import views as ingeniero_views
from apps.inversionista import views as inversionista_views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'administrador/$',admin_views.indexAdmin, name='indexAdmin'),
	url(r'contador/$',contador_views.indexContador, name='indexContador'),
	url(r'empleado/$',empleado_views.indexEmpleado, name='indexEmpleado'),
	url(r'ingeniero/$',ingeniero_views.indexIngeniero, name='indexIngeniero'),
	url(r'inversionista/$',inversionista_views.indexInversionista, name='indexInversionista'),
]