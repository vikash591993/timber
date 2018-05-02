from django import forms
from . models import UserDetail
from . models import ClientDetail
from . models import SupplierDetail


class HomeForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetail
        fields = ('username','password')


ID_CHOICES = (
    ('Id Proof','Id Proof'),
    ('Dl', 'Driving Licence'),
    ('Pan', 'PAN'),
    ('Aadhar', 'Aadhar Card'),
    ('Voter', 'Voter Id'),
)

class ClientForm(forms.ModelForm):
    client_name = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'id':'clientName','class':"form-control"}) )
    client_gst = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'id':'clientGst','class':"form-control"}) )
    client_address = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'id':'clientAddress','class':"form-control"}) )
    client_phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'clientPhone','class':"form-control"}))
    client_id = forms.CharField( label="Client Id",widget=forms.Select( choices=ID_CHOICES, attrs={'id': 'clientId', 'class': "form-control"} ) )
    client_id_number = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'id':'clientIdNumber','class':"form-control"}) )

    class Meta:
        model = ClientDetail
        fields = ('client_name', 'client_gst', 'client_address', 'client_phone', 'client_id', 'client_id_number')


class DateInput(forms.DateInput):
    input_type = 'date'


TAX_CHOICES = (
    ('Tax Type','Tax Type'),
    ('IGST','IGST'),
    ('CGST & SGST','CGST & SGST'),
)


class SupplierForm(forms.ModelForm):
    invoice_number = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'id':'invoiceNumber','class':"form-control"}))
    vehicle_number = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'id':'vehicleNumber','class':"form-control"}))
    sender_name = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'id':'senderName','class':"form-control"}))
    sender_address = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'id':'senderAddress','class':"form-control"}))
    sender_gstin = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'id':'senderGstin','class':"form-control"}))
    total_amount_before_tax = forms.FloatField(widget=forms.TextInput(attrs={'id':'taxAmountBeforeTax','class':"form-control"}))
    tax_amount = forms.FloatField( widget=forms.TextInput(attrs={'id':'taxAmount','class':"form-control"}))
    total_amount_after_tax = forms.FloatField( widget=forms.TextInput(attrs={'id':'taxAmountAfterTax','class':"form-control"}))
    invoice_date = forms.DateField(widget=DateInput(attrs={'id':'invoiceDate','class':"form-control"}))
    date_of_supply = forms.DateField(widget=DateInput(attrs={'id':'dateOfSupply','class':"form-control"}))
    tax_type = forms.CharField( label="Tax Type", widget=forms.Select( choices=TAX_CHOICES, attrs={'id':'taxType','class':"form-control"}))

    class Meta:
        model = SupplierDetail
        fields = {'invoice_number', 'invoice_date', 'vehicle_number', 'date_of_supply','sender_name','sender_address', 'sender_gstin','tax_type','total_amount_after_tax','total_amount_before_tax','tax_amount'}