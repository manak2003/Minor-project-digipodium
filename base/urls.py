from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.about, name='about'),
    path('why/',views.why, name='why'),
    path('solutions/',views.solutions, name='solutions'),
    path('services/',views.services, name='services'),
    path('postjob/',views.job_view, name='job'),
    path('recruitment/',views.recruitment, name='recruitment'),
    path('job application/',views.application_view, name='application'),
]