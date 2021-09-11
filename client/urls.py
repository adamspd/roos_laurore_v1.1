from django.urls import path
from django.conf.urls import url
from .views import *

app_name = 'client'

urlpatterns = [
    # client/
    path('', login_page, name='login'),

    # client/register/
    path('register/', register_page, name='register'),

    # client/clientID/
    path('user/', index, name='client_homepage'),

    # client/clientID/
    path('logout/', logout_user, name='logout'),

    # favorite
    path('favorite/', favorite, name='favorite'),
]