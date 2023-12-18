from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'common/home.html')

def register(request):
    return render(request,'common/register.html')

def login(request):
    return render(request,'common/login.html')
