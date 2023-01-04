from django.urls import path
from app2.views import *
app_name='isha'
urlpatterns=[
    path('isha/',isha,name='isha'),
]