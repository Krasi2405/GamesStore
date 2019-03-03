
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views


urlpatterns = [
	re_path(r'^$', views.index, name = "index"),
	re_path(r'^game/(?P<pk>\d+)/$', views.detail, name = "detail")	
]