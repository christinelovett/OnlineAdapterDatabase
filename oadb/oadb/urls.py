"""oadb URL Configuration

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
from .views import *
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from graphene_django.views import GraphQLView
from .schema import schema


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'adaptor', AdaptorViewSet)
router.register(r'kit', KitViewSet)
router.register(r'database', DatabaseViewSet)
router.register(r'run', RunViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='AdapterBase API')),
    url(r'^graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]