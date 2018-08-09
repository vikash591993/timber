import django_filters
from .models import UserInfo


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = UserInfo
        fields = ('username', 'email')
