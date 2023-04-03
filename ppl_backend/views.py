from django.http import HttpResponse
from django.shortcuts import render
from .models import Job

def index(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'home.html',context)

def about(request):
       return render(request, 'about.html')

def services(request):
       return render(request, 'services.html')

def clients(request):
       return render(request, 'clients.html')

def contact(request):
       return render(request, 'home.html')

def not_found(request):
       return render(request, '404.html')

def submit(request):
       return render(request, 'submit.html')

def contact(request):
       return render(request, 'contact.html')

def signup(request):
       return render(request, 'signup.html')

def login(request):
       return render(request, 'login.html')

def forgot(request):
       return render(request, 'forgot.html')

def jobs(request):
       return render(request, 'jobs.html')

def programmes(request):
       return render(request, 'programmes.html')
