from django.shortcuts import render
# import login
from django.contrib.auth import login,  authenticate
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job , Application
from .forms import JobForm, ApplicationForm
from django.contrib import messages

# Create your views here.
def index(request):
    ctx = {}
    ctx['title'] = 'Home'
    return render(request, 'base/index.html')

def about(request):
    ctx = {
        
        'title': 'About | Alquiler'
    } 
    return render(request, "base/about.html", ctx)

def why(request):
    ctx= {
        'title' : 'Why | Alquiler'
    }
    return render(request, "base/why.html",ctx)

def solutions(request):
    ctx= {
        'title' : 'Solutions | Alquiler'
    }
    return render(request, "base/solutions.html",ctx)


def services(request):
    ctx= {
        'title' : 'Services | Alquiler'
    }
    return render(request, "base/services.html",ctx)

def recruitment(request):
    ctx= {
        'title' : 'Recruitment | Alquiler'
    }
    return render(request, "base/recruitment.html",ctx)


def job_view(request):
    form =JobForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get ('username')
        company_name = form.cleaned_data.get ('company_name')
        company_email = form.cleaned_data.get ('company_email')
        company_number_of_employees = form.cleaned_data.get ('company_number_of_employees')
        your_first_and_last_name = form.cleaned_data.get ('your_first_and_last_name')
        are_you_a_hiring_manager = form.cleaned_data.get ('are_you_a_hiring_manager')
        your_phone_number = form.cleaned_data.get ('your_phone_number')
        how_you_heard_about_us = form.cleaned_data.get ('how_you_heard_about_us')
        job_title = form.cleaned_data.get ('job_title')
        where_will_an_employee_report_to_work = form.cleaned_data.get ('where_will_an_employee_report_to_work')
        what_is_the_job_type = form.cleaned_data.get ('what_is_the_job_type')
        how_quickly_do_you_need_to_hire = form.cleaned_data.get ('how_quickly_do_you_need_to_hire')
        what_is_the_schedule_for_this_job =form.cleaned_data.get ('what_is_the_schedule_for_this_job')
        is_there_a_planned_start_date_for_this_job = form.cleaned_data.get ('is_there_a_planned_start_date_for_this_job')
        what_is_the_pay = form.cleaned_data.get ('what_is_the_pay')
        job_description = form.cleaned_data.get ('job_description') 
        job_benefits = form.cleaned_data.get ('job_benefits')
        job_requirements = form.cleaned_data.get ('job_requirements')   
        
        user = User.objects.create_user(username=username)
        user.save()
        job = Job(user=user,company_name=company_name,company_email=company_email,company_number_of_employees=company_number_of_employees,your_first_and_last_name=your_first_and_last_name,are_you_a_hiring_manager=are_you_a_hiring_manager,your_phone_number=your_phone_number,how_you_heard_about_us=how_you_heard_about_us,job_title=job_title,where_will_an_employee_report_to_work=where_will_an_employee_report_to_work,what_is_the_job_type=what_is_the_job_type,what_is_the_schedule_for_this_job=what_is_the_schedule_for_this_job,is_there_a_planned_start_date_for_this_job=is_there_a_planned_start_date_for_this_job,how_quickly_do_you_need_to_hire=how_quickly_do_you_need_to_hire,what_is_the_pay=what_is_the_pay,job_description=job_description, job_requirements=job_requirements,job_benefits=job_benefits)
        job.save()
        
        if User is not None:
            login(request,user)
            request.session['is_company'] = True
            messages.success(request,'Job Posted')
            return redirect('company_home')
        else:
            messages.error(request,'Wrong Information')
            return redirect('job.html')
        
    ctx= {
        'form':form,
        'title' : 'Job | Alquiler'
    }
    return render(request, "base/job.html",ctx)

def application_view(request):
    form =ApplicationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        full_name = form.cleaned_data.get ('full_name')
        email = form.cleaned_data.get ('email')
        phone_number = form.cleaned_data.get ('phone_number')
        percentage_10th = form.cleaned_data.get ('percentage_10th')
        percentage_12th = form.cleaned_data.get ('percentage_12th')
        percentage_graduation = form.cleaned_data.get ('percentage_graduation')
        what_types_of_job_interests_you = form.cleaned_data.get ('what_types_of_job_interests_you')
        what_skills_you_have_that_are_relevant_to_the_position_you_applied_for = form.cleaned_data.get ('what_skills_you_have_that_are_relevant_to_the_position_you_applied_for')
        do_you_have_any_previous_work_experience = form.cleaned_data.get ('do_you_have_any_previous_work_experience')
        work_references = form.cleaned_data.get ('work_references')
        
        user = User.objects.create_user(username=username)
        user.save()
        application = Application(username=username,full_name= full_name,email=email,phone_number=phone_number,percentage_10th=percentage_10th,percentage_12th=percentage_12th,percentage_graduation=percentage_graduation,what_types_of_job_interests_you=what_types_of_job_interests_you,what_skills_you_have_that_are_relevant_to_the_position_you_applied_for=what_skills_you_have_that_are_relevant_to_the_position_you_applied_for,do_you_have_any_previous_work_experience=do_you_have_any_previous_work_experience,work_references=work_references)
        application.save()
        
        if User is not None:
            login(request,user)
            request.session['is_student'] = True
            messages.success(request,'Apllied Successfully')
            return redirect('student_home')
        else:
            messages.error(request,'You cannot apply for the job')
            return redirect('application.html')   

    ctx = {
        'form' : form,
        'title' : 'Job Applied | Alquiler'
    }
    return render(request, "base/application.html",ctx)

    
