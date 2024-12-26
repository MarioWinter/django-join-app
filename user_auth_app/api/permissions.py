from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Permission class that grants access to authenticated users who are either the owner of the object or a superuser.

    This class provides fine-grained permission checks for object-level operations.

    Methods:
        has_permission(self, request, view):
            Checks if the user is authenticated.
            Returns:
                bool: True if the user is authenticated, False otherwise.

        has_object_permission(self, request, view, obj):
            Checks if the user has permission to perform actions on the specific object.
            Returns:
                bool: True if the user is a superuser or the owner of the object, False otherwise.
                
    Notes:
        - For objects with a 'user' attribute, ownership is determined by comparing user IDs.
        - For objects without a 'user' attribute, a direct comparison with the request user is performed.
    """
    
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if hasattr(obj, 'user'):
            return request.user.id == obj.user.id
        return request.user == obj


class ProfilePermission(BasePermission):
    """
    ProfilePermission is a custom permission class that extends BasePermission.
    
    This class provides permission checks for user profile related operations.

    Methods:
        has_permission(self, request, view):
            Checks if the user is authenticated.
        has_object_permission(self, request, view, obj):
            Checks if the user has permission to perform actions on the object.
            - Allows DELETE method only for superusers.
            - For other methods, allows access only if the user's ID matches the object's ID.
    """
    
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user.is_superuser
        return request.user.id == obj.id

