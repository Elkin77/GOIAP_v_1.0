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
    url(r'cargarFactura/', views.cargarFactura, name="cargarFacturaContador"),
    url(r'(?P<factura_id>[0-9]+)/eliminarFactura$',views.eliminarFactura,name='eliminarFacturaContador'),
    url(r'(?P<factura_id>[0-9]+)/editarFactura$',views.editarFactura,name='editarFacturaContador'),
    url(r'gestionarFacturas/', views.gestionarFacturas, name="gestionarFacturasContador"),
    url(r'logout/$',user_views.logout_view, name='logout'),
    url(r'^listaObrasNomina/$',views.listaObrasNomina_view, name='listaObrasNomina'),
    url(r'(?P<obra_id>[0-9]+)/listaTrabajadoresNomina$',views.listaTrabajadoresNomina_view,name='listaTrabajadoresNomina'),
    url(r'(?P<trabajador_id>[0-9]+)/formularioNomina$',views.formularioNomina_view,name='formularioNomina'),
    url(r'(?P<trabajador_id>[0-9]+)/nominasGeneradas$',views.nominasGeneradas_view,name='nominasGeneradas'),
    url(r'(?P<nomina_id>[0-9]+)/informacionNomina$',views.informacionNomina_view,name='informacionNomina'),
    url(r'(?P<nomina_id>[0-9]+)/eliminarNomina$',views.eliminarRegistroNomina,name='eliminarNomina'),
]