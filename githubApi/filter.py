import django_filters
from .models import UserDetail


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = UserDetail
        fields = ('username', 'email')
