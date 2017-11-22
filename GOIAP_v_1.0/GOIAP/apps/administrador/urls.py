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
]