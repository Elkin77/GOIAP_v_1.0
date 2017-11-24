from django.conf.urls import url
from . import views
from apps.user import views as user_views

urlpatterns = [
    url(r'^$',views.indexIngeniero, name='indexIngeniero'),
    url(r'cargarDocumento/', views.cargarDocumento, name="cargarDocumentoIngeniero"),
    url(r'(?P<documento_id>[0-9]+)/eliminarDocumento$',views.eliminarDocumento,name='eliminarDocumentoIngeniero'),
    url(r'(?P<documento_id>[0-9]+)/editarDocumento$',views.editarDocumento,name='editarDocumentoIngeniero'),
    url(r'gestionarDocumentos/', views.gestionarDocumentos, name="gestionarDocumentosIngeniero"),
    url(r'consultarObservaciones/', views.consultarObservaciones, name="consultarObservacionesIngeniero"),
    url(r'logout/$',user_views.logout_view, name='logout'),
]