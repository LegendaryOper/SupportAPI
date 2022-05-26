from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to see/edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers of an object to see/edit it.
    """
    def has_permission(self, request, view):
        # Returns is there a user in the group 'manager'
        return request.user.groups.filter(name='manager').exists()


class IsOwnerOrManagerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow managers/admins/owners of an object to see/edit it.
    """
    def has_object_permission(self, request, view, obj):
        return (IsManager.has_permission(self, request, view) or
                    IsOwner.has_object_permission(self, request, view, obj) or
                    permissions.IsAdminUser.has_permission(self, request, view))


class IsManagerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow managers of an object to see/edit it.
    """
    def has_permission(*args):
        return bool(IsManager.has_permission(*args) or
                    permissions.IsAdminUser.has_permission(*args))

