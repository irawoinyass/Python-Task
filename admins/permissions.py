from rest_framework import generics, permissions


class IsSuperUser(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsSuperUserTwo(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser is True:
            return super().has_permission(request, view)
        return False
