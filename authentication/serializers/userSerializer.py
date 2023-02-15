from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


class UserMiniSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    rol = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'name', 'email', 'rol', 'isAdmin']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        return obj.get_full_name()

    def get_email(self, obj):
        return obj.email if obj.email != '' else 'No registrado'

    def get_isProvinceSpecialist(self, obj):
        return obj.isProvinceSpecialist

    def get_rol(self, obj):
        if self.get_isAdmin(obj):
            return 'Administrador'
        if self.get_isProvinceSpecialist(obj):
            return 'Especialista de salud provincial'
        return 'Usuario'


class UserSerializer(UserMiniSerializer):
    permissions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'rol', 'isAdmin', 'isProvinceSpecialist',
                  'date_joined', 'last_login', 'permissions']

    def get_permissions(self, obj):
        permissions = obj.get_user_permissions()
        return permissions


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'name', 'isAdmin', 'isProvinceSpecialist', 'rol', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
