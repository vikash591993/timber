from django.core.validators import RegexValidator
from django.db import models
import datetime

# Create your models here.
import psycopg2


from django.utils.translation import pgettext_lazy


class UserDetail(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class ClientDetail(models.Model):
    client_name = models.CharField(max_length=50)
    client_gst = models.CharField(max_length=50)
    client_address = models.CharField(max_length=100)
    client_phone = models.CharField( max_length=17)  # validators should be a list
    client_id = models.CharField(max_length=50)
    client_id_number = models.CharField(max_length=50)
    last_updated_time = models.DateTimeField(default=django.utils.timezone.now)


class Bills(models.Model):
    bill_number = models.CharField(max_length=50)
    total_amount = models.FloatField(max_length=50, default=0)
    date = models.DateTimeField()
    client_detail = models.ForeignKey(ClientDetail)
    last_updated_time = models.DateTimeField(default=django.utils.timezone.now)


class BillsDescriptions(models.Model):
    bill_id = models.ForeignKey(Bills)
    wood = models.CharField(max_length=20)
    wood_code = models.CharField(max_length=40,default="")
    rate = models.FloatField(max_length=50, default=0)
    volume = models.FloatField(max_length=50, default=0)
    total = models.FloatField(max_length=50, default=0)
    gst_tax = models.FloatField(max_length=2,default=0)
    last_updated_time = models.DateTimeField(default=django.utils.timezone.now)


class SupplierDetail(models.Model):
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    vehicle_number = models.CharField(max_length=50)
    date_of_supply = models.DateField()
    sender_name = models.CharField(max_length=50)
    sender_address = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=10, default=0)
    sender_gstin = models.CharField(max_length=100)
    total_amount_before_tax = models.FloatField(max_length=50, default=0)
    tax_type = models.CharField(max_length=2,default=0)
    tax_amount = models.FloatField(max_length=50, default=0)
    total_amount_after_tax = models.FloatField(max_length=50, default=0)


class SupplierWoodDescriptions( models.Model ):
    invoice_id = models.ForeignKey( SupplierDetail )
    wood = models.CharField( max_length=20 )
    wood_code = models.CharField( max_length=40, default="" )
    rate = models.FloatField( max_length=50, default=0 )
    volume = models.FloatField( max_length=50, default=0 )
    total = models.FloatField( max_length=50, default=0 )
    gst_tax = models.FloatField( max_length=2, default=0 )
    last_updated_time = models.DateTimeField( default=django.utils.timezone.now)