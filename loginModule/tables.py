import django_tables2 as tables
from loginModule.models import SupplierDetail


class SupplierTable(tables.Table):
    class Meta:
        model = SupplierDetail
        template_name = 'django_tables2/semantic.html'