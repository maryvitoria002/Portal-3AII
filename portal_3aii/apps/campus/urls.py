from django.urls import path
from . import views

app_name = 'campus'

urlpatterns = [
    path('', views.vida_campus, name='vida_campus'),
]
