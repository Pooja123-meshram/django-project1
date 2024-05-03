# user_roles/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, UserRoleViewSet,LogoutViewSet,LoginViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('roles', RoleViewSet)
router.register('user-roles', UserRoleViewSet)
router.register(r'login', LoginViewSet, basename='login')
router.register(r'logout', LogoutViewSet, basename='logout')


urlpatterns = [
    path('', include(router.urls)),
]
