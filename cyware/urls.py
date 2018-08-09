from django.conf.urls import url
from cyware.views import Home
from cyware.views import GithubLogin
from cyware.views import GeneratePDF
from . import views
from cyware.views import NewUser


urlpatterns = [
    url(r'^$', GithubLogin, name='GithubLogin'),
    url(r'^showdetail/$', Home, name='showdetail'),
    url(r'^generateReport/$', GeneratePDF , name='generateReport'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^newuser/$', NewUser, name='newuser'),
]