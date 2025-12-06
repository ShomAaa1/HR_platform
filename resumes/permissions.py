from rest_framework.permissions import BasePermission, SAFE_METHODS


class ResumePermissions(BasePermission):
    """
    Разграничивает доступ:
    - Кандидат: CRUD только над своими резюме
    - HR: только просмотр всех резюме
    - Админ: полный доступ ко всему
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        # Админ — полный доступ
        if user.role == 'admin':
            return True

        # HR — только чтение
        if user.role == 'hr':
            return request.method in SAFE_METHODS

        # Кандидат — создание резюме и чтение/изменение только своих
        if user.role == 'candidate':
            if request.method in ["POST", "GET"]:
                return True
            # PUT, PATCH, DELETE проверяются в has_object_permission
            return True

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Администратор — всё может
        if user.role == 'admin':
            return True

        # HR — только чтение
        if user.role == 'hr':
            return request.method in SAFE_METHODS

        # Кандидат — только свои резюме
        if user.role == 'candidate':
            return obj.user == user

        return False
