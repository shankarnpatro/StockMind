from rest_framework.permissions import BasePermission


class IsModificationAllowed(BasePermission):

    def has_permission(self, request, view):
        if int(view.kwargs['pk']) == request.user.id or request.user.is_staff or request.user.is_superuser:
            return request.user and True
