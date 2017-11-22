from django.conf.urls import url
from . import views
from apps.user import views as user_views

urlpatterns = [
    url(r'^$',views.indexIngeniero, name='indexIngeniero'),
    url(r'logout/$',user_views.logout_view, name='logout'),
]