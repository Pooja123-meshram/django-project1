from rest_framework import serializers
from .models import User, Role, UserRole
from django.core.exceptions import ValidationError

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'roles',"is_active","password"]

    def validate_email(self, value):
        if not value:
            raise ValidationError("Email is required")
        if '@' not in value:
            raise ValidationError("Invalid email address. Must contain '@'.")
        return value

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'
