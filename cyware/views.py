from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from cyware.models import UserInfo
from cyware.models import ApiLog
import requests
from django.views.generic import ListView
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO

from django.http import HttpResponse
from .filter import UserFilter
from django.utils import timezone
import datetime


# Create your views here.
def Home(request):
    if request.method == 'POST':
        username = request.POST['username']
        response = requests.get( 'https://api.github.com/users/'+username)
        print ('https://api.github.com/users/'+username)
        userdata = response.json()
        # create a userdetail object
        userDetailObject = UserInfo(username=userdata['login'], user_id=userdata['id'], email = userdata['email'], public_repos = userdata['public_repos'],
                                      avatar_url=userdata['avatar_url'], created_at=userdata['created_at'], last_updated_at=userdata['updated_at'])

        values = UserInfo.objects.all().filter( username=userdata['login'] ).count()
        if(values!=0):
            UserInfo.objects.all().filter( username=username ).update( public_repos = userdata['public_repos'],email=userdata['email'],
                                      avatar_url=userdata['avatar_url'], last_updated_at=userdata['updated_at'])
        else:
            userDetailObject.save()

        #get the user id
        userDetailObject = UserInfo.objects.get( username=userdata['login'])
        userDetailObjectId = userDetailObject.pk

        # store in the ApiLogDetail
        apiLogDetail = ApiLog(url=userdata['url'], user_id_id=userDetailObjectId)
        apiLogDetail.save()
        userDetail = UserInfo.objects.all()
        return render(request, 'home.html', {"userDetail":userDetail,})

    if request.method == 'GET':
        userDetail = UserInfo.objects.all()
        return render( request, 'home.html', {"userDetail": userDetail, } )


def GithubLogin(request):
    template_name = 'github_login.html'
    if request.method == 'GET':
        return render(request, template_name, {})


def NewUser(request):
    template_name = 'github_login.html'
    if request.method == 'GET':
        return render(request, template_name, {})


def GeneratePDF(request, *args, **kwargs):
    todayBack = timezone.now()
    oneDayBack = timezone.now() - timezone.timedelta(days=1)
    oneWeekBack = timezone.now() - timezone.timedelta(days=7)
    oneMonthBack = timezone.now() - timezone.timedelta(days=30)

    oneDayUser = UserInfo.objects.all().filter( created_at__range=(oneDayBack, todayBack) ).count()
    oneWeekUser = UserInfo.objects.all().filter( created_at__range=(oneWeekBack, todayBack) ).count()
    oneMonthUser = UserInfo.objects.all().filter( created_at__range=(oneMonthBack, todayBack) ).count()

    oneDayApi = ApiLog.objects.all().filter( inserted_at__range=(oneDayBack, todayBack) ).count()
    oneWeekApi = ApiLog.objects.all().filter( inserted_at__range=(oneWeekBack, todayBack) ).count()
    oneMonthApi = ApiLog.objects.all().filter( inserted_at__range=(oneMonthBack, todayBack) ).count()

    context = {
        'oneDayUser': oneDayUser,
        'oneWeekUser': oneWeekUser,
        'oneMonthUser': oneMonthUser,
        'oneDayApi': oneDayApi,
        'oneWeekApi': oneWeekApi,
        'oneMonthApi': oneMonthApi,
    }

    pdf = render_to_pdf( 'invoice.html', context )
    if pdf:
        response = HttpResponse( pdf, content_type='application/pdf' )
        filename = "Invoice_%s.pdf" % ("12")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get( "download" )
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return render( request, 'invoice1.html', context )


def render_to_pdf(template_src, context_dict={}):
    template = get_template( template_src )
    html = template.render( context_dict )
    result = BytesIO()
    pdf = pisa.pisaDocument( BytesIO( html.encode( "ISO-8859-1" ) ), result )
    if not pdf.err:
        return HttpResponse( result.getvalue(), content_type='application/pdf' )
    return None


class Search(ListView):
    template_name = 'search.html'
    model = UserInfo

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['filter'] = UserFilter(self.request.GET, queryset=self.get_queryset())
        return context
    #if request.method == 'GET':
     #   return render(request, template_name, {})