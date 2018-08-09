import django_filters
from .models import UserDetail1


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = UserDetail1
        fields = ('username', 'email')
