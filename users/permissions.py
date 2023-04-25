from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "USER":
            return super().has_permission(request, view)
        return False
