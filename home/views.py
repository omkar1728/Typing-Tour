from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
  

def dashboard(request):
    return render(request, 'dashboard.html')

def keyboard(request):
    return render(request,'keyboard.html')
    
def result(request):
    return render(request,'result.html')

def levels(request):
    return render(request, 'level_selection.html')

def pracitce(request):
    return render(request, 'practice.html')

def profile(request):
    return render(request, 'profile.html')