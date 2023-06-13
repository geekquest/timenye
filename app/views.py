from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, template_name='landing.html')

def login(request):
    return render(request, template_name='auth/login.html')

def signup(request):
    return render(request, template_name='auth/signup.html')

def for_you(request):
    return render(request, template_name='discover/fyp.html')

def sports(request):
    return render(request, template_name='sports.html')

def sport_home(request, sport_name):
    return render(request, template_name='sport/index.html', context={
        'sport_name': sport_name,
    })

def teams(request):
    return render(request, template_name='teams/index.html')

def register_team(request):
    return render(request, template_name='teams/register.html')