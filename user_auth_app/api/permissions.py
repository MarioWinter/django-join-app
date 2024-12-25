from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Permission class that grants access to authenticated users who are either the owner of the object or a superuser.
    Methods:
        has_permission(request, view):
            Returns True if the user is authenticated.
        has_object_permission(request, view, obj):
            Returns True if the user is a superuser or the owner of the object.
    """
    
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj.user


class ProfilePermission(BasePermission):
    """
    ProfilePermission is a custom permission class that extends BasePermission.
    Methods:
        has_permission(self, request, view):
            Checks if the user is authenticated.
        has_object_permission(self, request, view, obj):
            Checks if the user has permission to perform actions on the object.
            - Allows DELETE method only for superusers.
            - Allows other methods if the user is the owner of the object.
    """
    
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user.is_superuser
        return request.user == obj.user
