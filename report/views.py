from django.shortcuts import render

from .models import AllRerport


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
