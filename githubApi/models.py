# Create your models here.
import django
from django.db import models


# Create your models here.
class UserDetail(models.Model):
    username = models.CharField( max_length=100 )
    user_id = models.CharField(max_length=50)
    email = models.CharField( max_length=100, null=True )
    public_repos = models.CharField( max_length=50,null=True )
    avatar_url = models.CharField( max_length=100 )
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    last_updated_at = models.DateTimeField(default=django.utils.timezone.now)
    inserted_at = models.DateTimeField(default=django.utils.timezone.now)


class ApiLogDetail(models.Model):
    url = models.CharField(max_length = 100)
    user_id = models.ForeignKey(UserDetail)
    inserted_at = models.DateTimeField( default=django.utils.timezone.now )