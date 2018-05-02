from django.conf.urls import url

import loginModule
from loginModule.views import HomeView
from loginModule.views import Home
from loginModule.views import Navbar
from loginModule.views import CreateBill
from loginModule.views import AddStocks
from loginModule.views import Error
from loginModule.views import ShowStock
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', Home, name='home'),
    #url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^navbar/$', Navbar, name='navbar'),
    url(r'^create_bill/$', CreateBill, name='create_bill'),
    url(r'^add_stock/$', AddStocks, name='add_stock'),
    url(r'^error/$', Error, name='error'),
    url(r'^show_stock/$', ShowStock, name='show_stock'),
]
