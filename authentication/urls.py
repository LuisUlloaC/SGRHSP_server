from django.urls import path, include
from rest_framework import routers

from .views import *
# View Sets
from .viewsets import userViewSet as userViews
from .viewsets.permissionsViewset import PermissionViewSet

router = routers.DefaultRouter()
router.register(r'users', userViews.UserViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='loginView'),
    path('profile/update/', userViews.updateUserProfile, name='updateUserProfile'),
    path('changePassword/profile/', userViews.updateUserPassword, name='updateUserPassword'),
    path('profile/', userViews.getAuthenticatedUserProfile, name='getAuthenticatedUserProfile'),
]