from django.contrib import admin
from .models import Job
# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    '''Admin View for Job'''

    list_display = ('company_name','job_title','your_phone_number','job_description')
   