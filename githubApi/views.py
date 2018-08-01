from django.shortcuts import render
from githubApi.models import UserDetail
from githubApi.models import ApiLogDetail
import requests
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse


# Create your views here.
def Home(request):
    if request.method == 'POST':
        username = request.POST['username']

        response = requests.get( 'https://api.github.com/users/'+username)
        print ('https://api.github.com/users/'+username)
        userdata = response.json()
        print (userdata)
        print (userdata['email'])
        # create a userdetail object
        userDetailObject = UserDetail(username=userdata['login'], user_id=userdata['id'], email = userdata['email'], public_repos = userdata['public_repos'],
                                      avatar_url=userdata['avatar_url'], created_at=userdata['created_at'], last_updated_at=userdata['updated_at'])

        values = UserDetail.objects.all().filter( username=userdata['login'] ).count()
        if(values!=0):
            UserDetail.objects.all().filter( username=username ).update( public_repos = userdata['public_repos'],
                                      avatar_url=userdata['avatar_url'], last_updated_at=userdata['updated_at'])
        else:
            userDetailObject.save()

        #get the user id
        userDetailObject = UserDetail.objects.get( username=userdata['login'])
        userDetailObjectId = userDetailObject.pk

        # store in the ApiLogDetail
        apiLogDetail = ApiLogDetail(url=userdata['url'], user_id_id=userDetailObjectId)
        apiLogDetail.save()
        userDetail = UserDetail.objects.all()
        return render(request, 'home.html', {"userDetail":userDetail,})


def GithubLogin(request):
    template_name = 'github_login.html'
    if request.method == 'GET':
        return render(request, template_name, {})



def GeneratePDF(request, *args, **kwargs):
    userDetail = UserDetail.objects.all()
    context = {
        'userDetail':userDetail,
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
