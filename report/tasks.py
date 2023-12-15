from celery import shared_task
from django.utils.timezone import get_current_timezone


@shared_task()
def archivingReports(report):
    pass 
