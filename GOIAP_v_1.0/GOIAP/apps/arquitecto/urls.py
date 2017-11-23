from django.conf.urls import url
from . import views
from apps.user import views as user_views

urlpatterns = [
    url(r'^$',views.indexArquitecto, name='indexArquitecto'),
    url(r'cargarDocumento/', views.cargarDocumento_view, name="cargarDocumento"),
    url(r'gestionarDocumentos/', views.gestionarDocumentos_view, name="gestionarDocumentos"),
    url(r'logout/$',user_views.logout_view, name='logout'),
]