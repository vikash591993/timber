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
from loginModule.models import ClientDetail
from loginModule.models import Bills
from loginModule.models import BillsDescriptions
from loginModule.models import SupplierWoodDescriptions
from io import BytesIO
from django.http import HttpResponse

from xhtml2pdf import pisa
from django.template.loader import get_template


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
        print (request.POST)

        if form.is_valid():
            clientName = request.POST['client_name']
            clientGst = request.POST['client_gst']
            clientAddress = request.POST['client_address']
            clientPhone = request.POST['client_phone']
            clientProofId = request.POST['client_id']
            clientIdNumber = request.POST['client_id_number']
            billGeneratedDate = request.POST['invoice_date']

            soldWoodType = request.POST.getlist('woodType[]')
            soldWoodCode = request.POST.getlist( 'woodCode[]' )
            soldWoodVolume = request.POST.getlist( 'volume[]' )
            soldWoodRate = request.POST.getlist( 'rate[]' )
            soldWoodTax = request.POST.getlist('gstTax[]')
            soldWoodTotal = request.POST.getlist( 'total[]' )
            form.save()
            clientDetailObject = ClientDetail.objects.get(client_name=clientName, client_phone=clientPhone)
            clientDetailId = clientDetailObject.pk

            #total amount of the bill generated
            totalAmount = 0
            for i in soldWoodTotal:
                totalAmount = totalAmount + float(i)

            #Number of bills created till now.
            totalNumberOfBillsCreated = Bills.objects.all().count()
            newBillNumber = totalNumberOfBillsCreated + 1
            newInvoiceNumer = 'BT' + str(newBillNumber)
            print (newInvoiceNumer)

            # insert into bill table
            billsModelObject = Bills(bill_number=newInvoiceNumer, total_amount=totalAmount, date = billGeneratedDate, client_detail_id = clientDetailId)
            billsModelObject.save()

            #Get the generated bill id
            billsObject = Bills.objects.get(bill_number=newInvoiceNumer, total_amount=totalAmount, date = billGeneratedDate, client_detail_id = clientDetailId)
            billsObjectId = billsObject.pk

            #Insert all the woods_description in the billsdescription table
            for row in range(len(soldWoodType)):
                billsDesprictionObject = BillsDescriptions(wood=soldWoodType[row], rate=soldWoodRate[row],gst_tax = soldWoodTax[row], total=soldWoodTotal[row], volume=soldWoodVolume[row], bill_id_id=billsObjectId, wood_code=soldWoodCode[row])
                billsDesprictionObject.save()
                print( soldWoodType[row], "---", soldWoodCode[row], "----", soldWoodVolume[row], "-----", soldWoodTax[row],"-----",soldWoodRate[row],"----",soldWoodTotal[row] )

            billsDesprictionObjectArray = BillsDescriptions.objects.all().filter(bill_id_id=billsObjectId)
            #Create context dict
            context = {
                'clientName' : clientName,
                'clientGst' : clientGst,
                'clientAddress' : clientAddress,
                'clientPhone': clientPhone,
                'clientProofId': clientProofId,
                'clientIdNumber' : clientIdNumber,
                'billGeneratedDate': billGeneratedDate,
                'newInvoiceNumer': newInvoiceNumer,
                'totalAmount': totalAmount,
                'billObjectsArray' :billsDesprictionObjectArray,
            }
            pdf = render_to_pdf( 'invoice.html', context )
            if pdf:
                response = HttpResponse( pdf, content_type='application/pdf' )
                filename = "Invoice_%s.pdf" % (newInvoiceNumer)
                content = "inline; filename='%s'" % (filename)
                download = request.GET.get( "download" )
                if download:
                    content = "attachment; filename='%s'" % (filename)
                response['Content-Disposition'] = content
                return response

            #message = 'Stocks Added Successfully'
            #return render( request, succes_template_name, {'message': message} )
            return render(request, 'invoice1.html', context)

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

        if form.is_valid():
            invoiceNumber = request.POST['invoice_number']
            vehicleNumber = request.POST['vehicle_number']
            print (vehicleNumber)
            purchasedWoodType = request.POST.getlist( 'woodType[]' )
            purchasedWoodCode = request.POST.getlist( 'woodCode[]' )
            purchasedWoodVolume = request.POST.getlist( 'volume[]' )
            purchasedWoodRate = request.POST.getlist( 'rate[]' )
            purchasedWoodTax = request.POST.getlist( 'gstTax[]' )
            purchasedWoodTotal = request.POST.getlist( 'total[]' )
            form.save()
            supplierDetailObject = SupplierDetail.objects.get( invoice_number=invoiceNumber, vehicle_number=vehicleNumber )
            supplierDetailId = supplierDetailObject.pk

            #store in the table SupplierWoodDescriptions
            for row in range(len(purchasedWoodType)):
                #print( purchasedWoodType[row], "---", purchasedWoodCode[row], "----", purchasedWoodVolume[row], "-----", purchasedWoodTax[row], "-----", purchasedWoodRate[row], "----", purchasedWoodTotal[row] )
                supplierDesprictionObject = SupplierWoodDescriptions(wood=purchasedWoodType[row], rate=purchasedWoodRate[row],gst_tax = purchasedWoodTax[row], total=purchasedWoodTotal[row], volume=purchasedWoodVolume[row], invoice_id_id = supplierDetailId, wood_code=purchasedWoodCode[row])
                supplierDesprictionObject.save()
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
def GeneratePDF(request, *args, **kwargs):
    template = get_template('invoice1.html')

    if request.method == 'GET':
        context = {
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        #return HttpResponse(pdf, content_type='application/pdf')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("123213")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")


@login_required()
def GenerateInvoice(request):
    templateName = 'invoice.html'
    if request.method == 'GET':
        return render(request, templateName, {})


def render_to_pdf(template_src, context_dict={}):
    template = get_template( template_src )
    html = template.render( context_dict )
    result = BytesIO()
    pdf = pisa.pisaDocument( BytesIO( html.encode( "ISO-8859-1" ) ), result )
    if not pdf.err:
        return HttpResponse( result.getvalue(), content_type='application/pdf' )
    return None


@login_required()
def Error(request):
    template_name = 'error.html'
    return render(request, template_name, {})