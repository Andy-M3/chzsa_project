from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='client').exists()

class IsServiceCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='service_company').exists()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager').exists()
