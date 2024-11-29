from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'laboratorio'

urlpatterns = [    
    path('list/', views.laboratorio_list, name="laboratorio_list"),
    path('nuevo/', views.laboratorio_create, name='laboratorio_create'),
    path('editar/<int:id>/', views.laboratorio_update, name='laboratorio_update'),
    path('eliminar/<int:id>/', views.laboratorio_delete, name='laboratorio_delete'),
]