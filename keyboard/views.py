from django.shortcuts import render

# Create your views here.
def keyboard(request):
    return render(request,'keyboard.html')

def result(request):
    return render(request,'result.html')