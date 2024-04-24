# views.py
from django.shortcuts import render
from .models import Profile
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    profile = Profile.objects.first()  # Assuming you have only one profile
    return render(request, 'projects.html', {'profile': profile})

# Add more views as needed
def index(request):
    return render(request, "home.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def projects(request):
    return render(request,"projects.html")