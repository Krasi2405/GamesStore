"""games_store URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(('store.urls', 'store'), namespace = 'store')),
    re_path(r'^users/', include(('users.urls', 'users'), namespace = 'users')),
    re_path(r'^library/', include(('library.urls', 'library'), namespace = 'library')),
    re_path(r'^api/', include(('api.urls', 'api'), namespace = 'api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns