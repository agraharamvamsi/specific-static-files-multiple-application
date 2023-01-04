from django.urls import path
from app1.views import *
app_name='venkatesh'
urlpatterns=[
    path('venkatesh/',venkatesh,name='venkatesh'),
]