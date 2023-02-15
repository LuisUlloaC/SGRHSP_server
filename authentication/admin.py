from django.contrib import admin
from django.contrib.auth.models import Permission

from authentication.models import CustomUser

admin.site.register(Permission)

admin.site.register(CustomUser)
