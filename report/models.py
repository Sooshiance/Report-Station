from django.db import models


class ReportType:
    Daily = 1
    Weekly = 2
    Monthly = 3
    
    REPORTS = (
        ('Daily', Daily),
        ('Weekly', Weekly),
        ('Monthly', Monthly),
    )


class AllRerport(models.Model):
    title       = models.CharField(max_length=64, unique=True)
    slug        = models.SlugField(unique=True, primary_key=True, allow_unicode=True)
    report_type = models.PositiveSmallIntegerField(choices=ReportType.REPORTS, default=1)
    txt         = models.CharField(max_length=8000)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.title} {self.report_type}"
