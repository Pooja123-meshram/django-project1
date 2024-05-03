# user_roles/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Role, UserRole
from .serializers import UserSerializer, RoleSerializer, UserRoleSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(detail=True, methods=['post'])
    def add_role(self, request, pk=None):
        user = self.get_object()
        role_id = request.data.get('role_id')
        if not role_id:
            return Response({'error': 'Role ID is required'}, status=400)
        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return Response({'error': 'Role not found'}, status=404)
        UserRole.objects.create(user=user, role=role)
        return Response({'message': 'Role added successfully'}, status=200)

    @action(detail=True, methods=['post'])
    def disable(self, request, pk=None):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'message': 'User disabled successfully'}, status=200)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return (user, None)
            else:
                raise AuthenticationFailed('Invalid username or password.')
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid username or password.')

class LogoutViewSet(viewsets.ViewSet):
    def create(self, request):
        logout(request)
        return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
