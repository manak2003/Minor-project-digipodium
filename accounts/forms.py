from django import forms
from django.contrib.auth.models import User


INVALID_USERNAMES = ['admin','administrator','root']

# login form
class CompanyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return username

# login form
class StudentLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return username

# register form
class CompanyRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(help_text='Enter a valid email address')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    company_name = forms.CharField(label="Name")
    company_address = forms.CharField()
    company_website = forms.CharField()
    company_description = forms.CharField()
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is not available!")
        if username.lower() in INVALID_USERNAMES:
            raise forms.ValidationError("Username is invalid")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email
# register form

class StudentRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(help_text='Enter a valid email address')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    college = forms.CharField(help_text='Enter your college name')
    course = forms.CharField(help_text='Enter your course')
    stream = forms.CharField(help_text='Enter your stream')
    roll_no = forms.IntegerField(help_text='Enter your Roll no.')
    phone = forms.IntegerField(help_text='Contact No.')
    city = forms.CharField(help_text='Enter your city')
    passing_year = forms.IntegerField() 

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is not available!")
        if username.lower() in INVALID_USERNAMES:
            raise forms.ValidationError("Username is invalid")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email
    
