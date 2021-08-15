from rest_framework import permissions


class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Если метод не GET, то проверим авторизован ли пользователь
        if request.method != 'GET':
            return request.user.is_authenticated
        return True
