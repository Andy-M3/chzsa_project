from django.urls import path
from . import views

urlpatterns = [
    path('', views.machine_list, name='machine_list'),
    path('maintenances/', views.maintenance_list, name='maintenance_list'),
    path('claims/', views.claim_list, name='claim_list'),
]
