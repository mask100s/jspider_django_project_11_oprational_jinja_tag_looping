from django.urls import path
from app1.views import *

app_name='forloop'

urlpatterns = [
    path('looping/',looping,name='looping'),
]
