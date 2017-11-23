from django.conf.urls import url
from . import views
from apps.user import views as user_views

urlpatterns = [
    url(r'^$',views.indexArquitecto, name='indexArquitecto'),
    url(r'cargarDocumento/', views.cargarDocumento, name="cargarDocumento"),
    url(r'(?P<documento_id>[0-9]+)/eliminarDocumento$',views.eliminarDocumento,name='eliminarDocumento'),
    url(r'(?P<documento_id>[0-9]+)/editarDocumento$',views.editarDocumento,name='editarDocumento'),
    url(r'gestionarDocumentos/', views.gestionarDocumentos, name="gestionarDocumentos"),
    url(r'logout/$',user_views.logout_view, name='logout'),
]