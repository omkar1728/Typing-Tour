from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
  

def base(request):
    return render(request,'base.html')

def keyboard(request):
    return render(request,'keyboard.html')
    
def result(request):
    return render(request,'result.html')
