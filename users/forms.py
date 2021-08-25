from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginFrom(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')