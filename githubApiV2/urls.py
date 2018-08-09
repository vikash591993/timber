from django.conf.urls import url
from githubApiV2.views import Home
from githubApiV2.views import GithubLogin
from githubApiV2.views import GeneratePDF
from . import views
from githubApiV2.views import NewUser


urlpatterns = [
    url(r'^$', GithubLogin, name='GithubLogin'),
    url(r'^showdetail/$', Home, name='showdetail'),
    url(r'^generateReport/$', GeneratePDF , name='generateReport'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^newuser/$', NewUser, name='newuser'),
]