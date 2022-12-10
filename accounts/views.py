from django.shortcuts import render
# import login
from django.contrib.auth import login,  authenticate, logout
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Company
from base.models import Job
from .forms import CompanyLoginForm,CompanyRegisterForm,StudentLoginForm,StudentRegisterForm
from django.contrib import messages

def select_login(request):
    ctx = {
        
        'title': 'Login | Select'
    } 
    return render(request, "accounts/select_login.html", ctx)
    
def company_register_view(request):
    form=CompanyRegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        email =form.cleaned_data.get('email')
        company_name =form.cleaned_data.get('company_name')
        company_address =form.cleaned_data.get('company_address')
        company_website =form.cleaned_data.get('company_website')
        company_description =form.cleaned_data.get('company_description')
        
        if password == password2:
            user = User.objects.create_user(username=username, password=password2, email=email)
            user.save()
            company = Company(user=user, company_name=company_name,company_email=email,company_address=company_address,company_website=company_website, company_description=company_description)
            company.save()
        
        
            if User is not None:
                login(request, user)
                request.session['is_company'] = True
                messages.success(request, 'Register Successful')
                return redirect('company_home')
            else:
                messages.error(request,'Wrong Credentials')
                return redirect('company_register.html')
            
    ctx = {
        'form': form,
        'title': 'Register | Company'
    }
    return render(request, "accounts/company_register.html", ctx)

def student_register_view(request):
    form=StudentRegisterForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        college = request.POST['college']
        course = request.POST['course']
        stream = request.POST['stream']
        roll_no = request.POST['roll_no']
        phone = request.POST['phone']
        city = request.POST['city']
        passing_year = request.POST['passing_year']
        # first create a new user
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'student_register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'student_register.html' )
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                student = Student(user=user,college=college,course=course,stream=stream,roll_no=roll_no,phone=phone,city=city,passing_year=passing_year)
                student.save()
                
            if User is not None:
                login(request, user)
                request.session['is_student'] = True
                messages.success(request, 'Register Successful')
                return redirect('student_home')               
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'student_register.html' )
    ctx = {
        'form': form,
        'title':'Register | Student'}
    return render(request, "accounts/student_register.html", ctx)

        
def student_home(request):
    companies = Company.objects.all()
    jobs = Job.objects.all()
    ctx = {'companies': companies, 'jobs':jobs}
    
    return render(request, 'accounts/student_home.html', ctx)

def student_login_view(request):
    form=StudentLoginForm(request.POST or None)
    if form.is_valid():
        uname = form.cleaned_data.get('username')
        pwd = form.cleaned_data.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            request.session['is_student'] = True
            login(request,user)
            messages.success(request, 'Login Successful')
            return redirect('student_home')
        else:
            messages.error(request,'Wrong Credentials')
            
    ctx = {
        'form': form,
        'title': 'Login | Student'
    } 
    return render(request, "accounts/student_login.html", ctx)

def company_login_view(request):
    form=CompanyLoginForm(request.POST or None)
    if form.is_valid():
        uname = form.cleaned_data.get('username')
        pwd = form.cleaned_data.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request,user)
            request.session['is_company'] = True
            messages.success(request, 'Login Successful')
            return redirect('company_home')
        else:
            messages.error(request,'Wrong Credentials')
            
    ctx = {
        'form': form,
        'title': 'Login | Company'
    } 
    return render(request, "accounts/company_login.html", ctx)

def company_home(request):
    student = Student.objects.all()
    ctx = {'student': student}
    return render(request, 'accounts/company_home.html', ctx)

def logout_view(request):
    request.session.clear()
    logout(request)
    return redirect('/')