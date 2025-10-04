from django.contrib import admin
from django.urls import path, include
from dashboard.views import *


urlpatterns=[
    path("",Dashboard,name="Dashboard")


]