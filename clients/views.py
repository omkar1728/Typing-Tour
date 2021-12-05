from django.core.checks import messages
from django.shortcuts import render

from clients.models import clients_model

# Create your views here.

def login_page(request):
    username = request.POST.get('Username')
    password = request.POST.get('Password')  
    return render(request, 'login.html')

def register_page(request):
    username = request.POST.get('Username')
    password = request.POST.get('Password')  
    user = clients_model(username = username, password  = password, globalScore = 0,  hoursPracticed = 0)
    user.save()
    return render(request, 'register.html', {'username':username})