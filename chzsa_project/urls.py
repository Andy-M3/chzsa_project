from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chzsa_app import api_views
from chzsa_app.views import home, search_machine
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'machines', api_views.MachineViewSet)
router.register(r'maintenances', api_views.MaintenanceViewSet)
router.register(r'claims', api_views.ClaimViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('machines/', include('chzsa_app.urls')),
    path('maintenances/', include('chzsa_app.urls')),
    path('claims/', include('chzsa_app.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', search_machine, name='search_machine'),
]
