from django.conf.urls import url
from . import views
from apps.user import views as user_views

urlpatterns = [
    url(r'^$',views.indexArquitecto, name='indexArquitecto'),
    url(r'cargarDocumento/', views.cargarDocumento, name="cargarDocumentoArquitecto"),
    url(r'(?P<documento_id>[0-9]+)/eliminarDocumento$',views.eliminarDocumento,name='eliminarDocumentoArquitecto'),
    url(r'(?P<documento_id>[0-9]+)/editarDocumento$',views.editarDocumento,name='editarDocumentoArquitecto'),
    url(r'gestionarDocumentos/', views.gestionarDocumentos, name="gestionarDocumentosArquitecto"),
    url(r'consultarObservaciones/', views.consultarObservaciones, name="consultarObservacionesArquitecto"),
    url(r'crearInventario/', views.crearInventario, name="crearInventarioArquitecto"),
    url(r'(?P<inventario_id>[0-9]+)/eliminarInventario$',views.eliminarInventario,name='eliminarInventarioArquitecto'),
    url(r'(?P<inventario_id>[0-9]+)/editarInventario$',views.editarInventario,name='editarInventarioArquitecto'),
    url(r'gestionarInventario/', views.gestionarInventario, name="gestionarInventarioArquitecto"),
    url(r'logout/$',user_views.logout_view, name='logout'),
]