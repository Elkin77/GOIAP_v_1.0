from django.conf.urls import url
from . import views
from apps.user import views as user_views



urlpatterns = [
    url(r'^$',views.indexAdmin, name='indexAdmin'),
    url(r'logout/$',user_views.logout_view, name='logout'),
    url(r'^registrarUsuarios/$',views.registrarUsuario_view, name='registrarUsuarios'),
    url(r'^registrarObras/$',views.registrarObra_view, name='registrarObras'),
    url(r'^listaUsuarios/$',views.listaUsuarios_view, name='listaUsuarios'),
    url(r'(?P<usuario_id>[0-9]+)/eliminarUsuarios$',views.eliminarUsuario_view,name='eliminarUsuarios'),
    url(r'(?P<usuario_id>[0-9]+)/editarUsuarios$',views.editarUsuario_view,name='editarUsuarios'),
    url(r'^listaObras/$',views.listaObras_view, name='listaObras'),
    url(r'(?P<obra_id>[0-9]+)/verObras$',views.verObra_view,name='verObras'),
    url(r'(?P<obra_id>[0-9]+)/eliminarObras$',views.eliminarObra_view,name='eliminarObras'),
    url(r'(?P<obra_id>[0-9]+)/editarObras$',views.editarObra_view,name='editarObras'),
    url(r'(?P<obra_id>[0-9]+)/registrarEmpleados$',views.registrarEmpleados_view,name='registrarEmpleados'),
    url(r'(?P<user_id>[0-9]+)/asignarObras$',views.asignarObras_view,name='asignarObras'),
    url(r'(?P<user_id>[0-9]+)/eliminarAsignacion$',views.eliminarAsignacion_view,name='eliminarAsignacion'),
    url(r'(?P<reporte_id>[0-9]+)/eliminarReporte$',views.eliminarReporte_view, name='eliminarReporte'),
]

