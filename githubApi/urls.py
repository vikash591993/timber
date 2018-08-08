from django.conf.urls import url
from githubApi.views import Home
from githubApi.views import GithubLogin
from githubApi.views import GeneratePDF
from . import views
from githubApi.views import NewUser


urlpatterns = [
    url(r'^$', GithubLogin, name='GithubLogin'),
    url(r'^showdetail/$', Home, name='showdetail'),
    url(r'^generateReport/$', GeneratePDF , name='generateReport'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^newuser/$', NewUser, name='newuser'),
]