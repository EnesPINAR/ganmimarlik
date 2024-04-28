from django.urls import path
from . import views

urlpatterns = [
    path('architecture', views.architecture, name='architecture services'),
    path('interior', views.interior, name='interior services')
]