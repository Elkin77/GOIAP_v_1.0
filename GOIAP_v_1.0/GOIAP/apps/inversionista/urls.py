from django.conf.urls import url
from . import views
from apps.user import views as user_views

urlpatterns = [
    url(r'^$',views.indexInversionista, name='indexInversionista'),
    url(r'logout/$',user_views.logout_view, name='logout'),
    url(r'^obrasAsignadas/$',views.obrasAsignadas_view, name='obrasAsignadas'),
    url(r'(?P<obra_id>[0-9]+)/informacionObra$',views.infoObra_view,name='informacionObra'),
]