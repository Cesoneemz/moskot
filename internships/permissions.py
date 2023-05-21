from rest_framework.permissions import BasePermission


class IsTestingUserAndAuthenticatedPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        if not request.user.is_authenticated:
            return False

        if request.user.current_stage != "Тестирование":
            return False

        return True
