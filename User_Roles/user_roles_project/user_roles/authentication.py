from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class BasicAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Extract username and password from the request
        username = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')

        if not username or not password:
            return None

        # Authenticate the user
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return (user, None)
            else:
                raise AuthenticationFailed('Invalid username or password.')
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid username or password.')

    def authenticate_header(self, request):
        return 'Basic realm="User Visible Realm", charset="UTF-8"'
