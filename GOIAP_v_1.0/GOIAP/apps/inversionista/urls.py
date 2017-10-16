from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.indexInversionista, name='indexInversionista'),
]