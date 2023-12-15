from django.urls import path

from .views import *


urlpatterns = [
    path('', allReports, name='all-reports'),
]
