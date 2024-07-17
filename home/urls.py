from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('testinggoogle', views.testinggoogle, name='testinggoogle')
]