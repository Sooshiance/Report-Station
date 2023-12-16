from django.shortcuts import render

from .models import AllRerport
from .tasks import *


def allReports(request):
    daily = AllRerport.objects.all().filter(report_type=1)
    weekly = AllRerport.objects.all().filter(report_type=2)
    monthly = AllRerport.objects.all().filter(report_type=3)
    context = {
        'daily': daily,
        'weekly': weekly,
        'monthly': monthly,
    }
    return render(request, 'index.html', context=context)


def dailyReports(request):
    daily = AllRerport.objects.all().filter(report_type=1)
    context = {'daily':daily}
    archiving_Daily_Reports_as_Weekly()
    return render(request, 'daily.html', context=context)


def weeklyReports(request):
    weekly = AllRerport.objects.all().filter(report_type=2)
    context = {'weekly':weekly}
    archiving_Weekly_Reports_as_Monthly()
    return render(request, 'weekly.html', context=context)


def monthlyReports(request):
    monthly = AllRerport.objects.all().filter(report_type=3)
    context = {'monthly':monthly}
    return render(request, 'monthly.html', context=context)
