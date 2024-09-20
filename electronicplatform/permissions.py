from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    message = 'Доступно только действующим сотрудникам'

    def has_permission(self, request, view):
        if not request.user.is_active:
            return False
        return True



