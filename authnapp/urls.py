from django.urls import path, re_path
from .views import UserCustomViewSet

app_name = 'authnapp'
urlpatterns = [
    path('', UserCustomViewSet.as_view({'get': 'list'})),
]