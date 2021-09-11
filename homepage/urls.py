from django.urls import path
from django.conf.urls import url
from .views import *

app_name = 'homepage'

urlpatterns = [
    # homepage
    path('', IndexView.as_view(), name='index'),

    # /photoId/
    url(r'^(?P<pk>[0-9]+)/$', DetailedView.as_view(), name='detail'),
]