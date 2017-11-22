"""GOIAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'', include('apps.user.urls')),
	url(r'^administrador/', include('apps.administrador.urls')),
    url(r'^arquitecto/', include('apps.arquitecto.urls')),
    url(r'^contador/', include('apps.contador.urls')),
    url(r'^empleado/', include('apps.empleado.urls')),
    url(r'^ingeniero/', include('apps.ingeniero.urls')),
    url(r'^inversionista/', include('apps.inversionista.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)