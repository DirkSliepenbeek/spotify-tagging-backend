"""spotify_tagging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework import routers, serializers, viewsets
from django.urls import path, include
import spotify_tagging.views as views
from rest_framework.authtoken.views import obtain_auth_token

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'tags', views.TagViewSet, basename='tags')
router.register(r'tracks', views.TrackViewSet, basename='tracks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
