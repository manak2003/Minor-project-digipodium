from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    
    user =  models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(unique=True)
    company_number_of_employees = models.IntegerField()
    your_first_and_last_name = models.CharField(max_length=100)
    are_you_a_hiring_manager = models.CharField(max_length=100)
    your_phone_number = models.IntegerField(unique=True)
    how_you_heard_about_us = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    where_will_an_employee_report_to_work = models.CharField(max_length=100)
    what_is_the_job_type = models.CharField(max_length=100, default=True)
    how_quickly_do_you_need_to_hire = models.CharField(default=True,max_length=100)
    what_is_the_schedule_for_this_job = models.CharField(max_length=100,default=True)
    is_there_a_planned_start_date_for_this_job = models.CharField(max_length=100,default=True)
    what_is_the_pay =models.IntegerField(default=True)
    job_description = models.CharField(max_length=1000,default=True)
    job_benefits = models.CharField(max_length=1000 ,default=True)
    job_requirements = models.CharField(max_length=1000 , default=True)
    
    def __str__(self):
        return self.user.email
    
    
    
class Application(models.Model):
    username = models.CharField(max_length=200,default=True)
    full_name = models.CharField(max_length=200,default=True) 
    email =  models.EmailField(max_length=200,default=True)
    phone_number = models.IntegerField(default=True)
    percentage_10th = models.IntegerField(default=True)
    percentage_12th = models.IntegerField(default=True)
    percentage_graduation = models.IntegerField(default=True)
    what_types_of_job_interests_you = models.CharField(max_length=200,default=True)
    what_skills_you_have_that_are_relevant_to_the_position_you_applied_for = models.CharField(max_length=200,default=True)
    do_you_have_any_previous_work_experience = models.CharField(max_length=200,default=True)
    work_references = models.CharField(max_length=200,default=True)
    
    def __str__(self):
        return self.email
    
    
    

    
