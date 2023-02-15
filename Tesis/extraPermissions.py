from rest_framework.permissions import BasePermission


class IsProvinceSpecialist(BasePermission):
    """
    Allows access only to Province Specialist users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.isProvinceSpecialist)
