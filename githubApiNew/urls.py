from django.conf.urls import url
from githubApiNew.views import Home
from githubApiNew.views import GithubLogin
from githubApiNew.views import GeneratePDF
from . import views
from githubApiNew.views import NewUser


urlpatterns = [
    url(r'^$', GithubLogin, name='GithubLogin'),
    url(r'^showdetail/$', Home, name='showdetail'),
    url(r'^generateReport/$', GeneratePDF , name='generateReport'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^newuser/$', NewUser, name='newuser'),
]