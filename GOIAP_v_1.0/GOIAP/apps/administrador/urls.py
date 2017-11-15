from django.conf.urls import url
from . import views
from apps.administrador.views import registrarUsuario_view, listaUsuarios_view

urlpatterns = [
    url(r'^$',views.indexAdmin, name='indexAdmin'),
    url(r'^registrarUsuarios/$',views.registrarUsuario_view, name='registrarUsuarios'),
    url(r'^listaUsuarios/$',views.listaUsuarios_view, name='listaUsuarios'),
    url(r'(?P<usuario_id>[0-9]+)/eliminarUsuarios$',views.eliminarUsuario_view,name='eliminarUsuarios'),
    url(r'(?P<usuario_id>[0-9]+)/editarUsuarios$',views.editarUsuario_view,name='editarUsuarios'),
]