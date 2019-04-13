from django.conf.urls import url, include
from django.urls import path, re_path

from . import views


urlpatterns = [
	re_path(r'^$', views.index, name = "index"),
	re_path(r'^download/(?P<pk>\d+)/$', views.download, name = "download")
]