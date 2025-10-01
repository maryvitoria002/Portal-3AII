from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('calendario/', views.calendario, name='calendario'),
    path('', views.calendario, name='calendario'),
]