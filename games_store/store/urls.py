
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
	re_path(r'^$', views.index, name = "index"),
	re_path(r'^game/(?P<pk>\d+)/$', views.detail, name = "detail"),
	re_path(r'^search/$', views.search, name = "search"),
	re_path(r'^buy/(?P<game_pk>\d+)/$', views.buy, name = "buy")
]