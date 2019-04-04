
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
	re_path(r'^register/$', views.register, name = "register"),
	re_path(r'^login/$', views.login_view, name = "login"),
	re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name="users/logout.html"), name = "logout"),
	re_path(r'^profile/(?P<pk>\d+)$', views.profile, name = "profile")
]