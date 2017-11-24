from django.conf.urls import url
from . import views
from apps.user import views as user_views

urlpatterns = [
    url(r'^$',views.indexContador, name='indexContador'),
    url(r'cargarDocumento/', views.cargarDocumento, name="cargarDocumentoContador"),
    url(r'(?P<documento_id>[0-9]+)/eliminarDocumento$',views.eliminarDocumento,name='eliminarDocumentoContador'),
    url(r'(?P<documento_id>[0-9]+)/editarDocumento$',views.editarDocumento,name='editarDocumentoContador'),
    url(r'gestionarDocumentos/', views.gestionarDocumentos, name="gestionarDocumentosContador"),
    url(r'consultarObservaciones/', views.consultarObservaciones, name="consultarObservacionesContador"),
    url(r'logout/$',user_views.logout_view, name='logout'),
]