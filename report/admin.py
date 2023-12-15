from django.contrib import admin

from .models import AllRerport


@admin.register(AllRerport)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'report_type']
    prepopulated_fields = {'slug': ('title',)}
