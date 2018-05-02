from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from loginModule.forms import HomeForm
from loginModule.forms import SupplierForm
from loginModule.models import UserDetail
from loginModule.models import SupplierDetail
from django.contrib.auth.decorators import login_required
from loginModule.tables import SupplierTable
from django_tables2 import RequestConfig
from django.contrib.auth import logout
from loginModule.forms import ClientForm


class HomeView( TemplateView ):
    template_name = 'login/index.html'

    def get(self, request):
        form = HomeForm()
        userdetail = UserDetail.objects.all()
        args = {'form': form, 'userdetail': userdetail}
        return render( request, self.template_name, args )

    def post(self, request):
        form = HomeForm( request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form = HomeForm()
            return redirect('/loginModule')

        args = {'form': form, 'username': username, 'password': password}
        return render( request, self.template_name, args )


@login_required()
def Home(request):
    template_name = 'login/home.html'
    if request.method == 'GET':
        return render(request, template_name, {})

    if request.method == 'POST':
        logout(request)
        return redirect('/loginModule/login')


@login_required()
def Navbar(request):
    template_name = 'navbar.html'
    if request.method == 'GET':
        return render(request, template_name, {})


@login_required()
def CreateBill(request):
    template_name = 'create_bill.html'
    error_template_name = 'error.html'
    succes_template_name = 'success.html'

    if request.method == 'GET':
        form = ClientForm()
        return render( request, template_name, {'form':form})

    if request.method == 'POST':
        form = ClientForm(request.POST)

        for key in request.POST:
            print( key )
            value = request.POST[key]
            print( value )

        print ("inside post functioon")
        if form.is_valid():
            print ("inside is valid")
            print ("before sold wood table value")
            soldWoodTableValue = request.POST['nameSoldWoodTableCopy']
            print ("type is " ,type(soldWoodTableValue))
            print ("after sold wood table value")
            form.save()
            form = ClientForm()
            message = 'Stocks Added Successfully'
            return render( request, succes_template_name, {'message': message} )

    message = 'Something went wrong. Please try again'
    return render( request, error_template_name, {'message': message} )


@login_required()
def AddStocks(request):
    template_name = 'add_stock.html'
    error_template_name = 'error.html'
    succes_template_name = 'success.html'

    if request.method == 'GET':
        form = SupplierForm()
        return render(request, template_name, {'form': form})

    if request.method == 'POST':
        form = SupplierForm(request.POST)
        print ("inside poost functon")
        if form.is_valid():
            print ("insdie form valid")
            form.save()
            form = SupplierForm()
            message = 'Stocks Added Successfully'
            return render( request, succes_template_name, {'message': message} )

    message = 'Something went wrong. Please try again'
    return render( request, error_template_name, {'message': message} )


@login_required()
def ShowStock(request):
    templateName = 'show_stock.html'
    supplierDetail = SupplierDetail.objects.all()
    supplierTable = SupplierTable(supplierDetail)
    RequestConfig( request ).configure( supplierTable )
    return render(request, templateName, {'supplierTable': supplierTable})



@login_required()
def Error(request):
    template_name = 'error.html'
    return render(request, template_name, {})