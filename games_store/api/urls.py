from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'platforms', views.PlatformViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'games/(?P<pk>\d+)/thumbnail/$', views.thumbnail_image, name = "thumbnail_image"),
    path('', include(router.urls)),
]