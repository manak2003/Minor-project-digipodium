from django import forms
from django.contrib.auth.models import User

class JobForm(forms.Form):
    username = forms.CharField()
    company_name = forms.CharField()
    company_email = forms.EmailField()
    company_number_of_employees = forms.IntegerField()
    your_first_and_last_name = forms.CharField()
    are_you_a_hiring_manager = forms.CharField(help_text='Yes or No ?') 
    your_phone_number = forms.IntegerField()
    how_you_heard_about_us = forms.CharField()
    job_title = forms.CharField()
    where_will_an_employee_report_to_work = forms.CharField()
    what_is_the_job_type = forms.CharField()
    how_quickly_do_you_need_to_hire = forms.CharField()
    what_is_the_schedule_for_this_job = forms.CharField()
    is_there_a_planned_start_date_for_this_job = forms.CharField()
    what_is_the_pay = forms.IntegerField()
    job_description = forms.CharField()
    job_benefits = forms.CharField()
    job_requirements = forms.CharField()
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is not available!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email
     
     
class ApplicationForm(forms.Form):
    username = forms.CharField()
    full_name =forms.CharField()
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    percentage_10th = forms.IntegerField()
    percentage_12th = forms.IntegerField()
    percentage_graduation = forms.IntegerField()
    what_types_of_job_interests_you = forms.CharField()
    what_skills_you_have_that_are_relevant_to_the_position_you_applied_for = forms.CharField()
    do_you_have_any_previous_work_experience = forms.CharField()
    work_references = forms.CharField()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email