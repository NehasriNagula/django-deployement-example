from django.urls import re_path
from django.urls import path,include
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path(r'^relative/',views.relative,name='relative'),
    path(r'^other/',views.other,name='other'),
]
