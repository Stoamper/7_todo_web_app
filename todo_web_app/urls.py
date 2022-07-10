"""todo_web_app URL Configuration

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
import imp
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from authnapp.views import UserModelViewSet, UserCustomViewSet
from .views import ProjectModelViewSet, TodoModelViewSet
# from .views import ProjectCreateAPIView
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
# router.register('users', UserModelViewSet) Первоначальная модель User
router.register('users', UserCustomViewSet)
router.register('projects', ProjectModelViewSet)
router.register('TODO', TodoModelViewSet)
# router.register('TestProject', TestProjectViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="TODO_WEB_APP",
        default_version='0.1',
        description='Documentation to our project',
        contact=openapi.Contact(email='stomp911@yandex.ru'),
        license=openapi.License(name='Geek_License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    # URLPAthVersioning
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UserCustomViewSet.as_view({'get': 'list'})),
    # NamespaceVersioning (но почему-то версия также после api, а не после users)
    path('api/0.1/users/', include('authnapp.urls', namespace='0.1')),
    path('api/0.2/users/', include('authnapp.urls', namespace='0.2')),
    path('api/0.3/users/', include('authnapp.urls', namespace='0.3')),
    # Swagger
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
    name='schema-redoc'),
]