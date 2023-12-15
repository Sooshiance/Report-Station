from celery import shared_task
from django.utils.timezone import timedelta

from .models import AllRerport


@shared_task()
def archiving_Daily_Reports_as_Weekly():
    daily = AllRerport.objects.all().filter(report_type=1)
    for i in daily:
        if i.created_at > timedelta(days=7, hours=0, minutes=0, seconds=0):
            i.report_type = 2


@shared_task()
def archiving_Weekly_Reports_as_Monthly():
    weekly = AllRerport.objects.all().filter(report_type=2)
    for i in weekly:
        if i.created_at > timedelta(days=30, hours=0, minutes=0, seconds=0):
            i.report_type = 3
