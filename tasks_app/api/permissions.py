from xmlrpc.client import Boolean
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj.user

class OnlyDelete (BasePermission):
    def has_permission(self, request, view):
        if request.method != "DELETE":
            return False
        return request.user.is_authenticated
        
    
    def has_object_permission(self, request, view, obj):
        if request.method != "DELETE":
            return False
        return True