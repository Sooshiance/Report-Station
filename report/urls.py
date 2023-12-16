from django.urls import path

from .views import *


urlpatterns = [
    path('', allReports, name='all-reports'),
    path('daily/', dailyReports, name='daily-reports'),
    path('weekly/', weeklyReports, name='weekly-reports'),
    path('monthly/', monthlyReports, name='monthly-reports'),
]
