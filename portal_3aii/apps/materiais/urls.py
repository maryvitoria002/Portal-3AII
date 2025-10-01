from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    path('', views.lista, name='lista'),
]
