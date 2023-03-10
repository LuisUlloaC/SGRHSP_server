from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Api router
router = routers.DefaultRouter()

urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),

    # Api routes
    path('api/auth/', include('authentication.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/server/', include('server.urls')),
]