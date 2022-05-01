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
    cont = {}
    return render(request, 'practice.html')

def profile(request):
    return render(request, 'profile.html')

def tut1(request):
    return render(request,'tut1.html')    
def tut2(request):
    return render(request,'tut2.html')
def tut3(request):
    return render(request,'tut3.html')    
def tut4(request):
    return render(request,'tut4.html')    
def tut5(request):
    return render(request,'tut5.html')    
def tut6(request):
    return render(request,'tut6.html')    
def tut7(request):
    return render(request,'tut7.html')    
def tut8(request):
    return render(request,'tut8.html')    
def tut9(request):
    return render(request,'tut9.html')    
def tut10(request):
    return render(request,'tut10.html')    
def tut11(request):
    return render(request,'tut11.html')    
def tut12(request):
    return render(request,'tut12.html')    
def tut13(request):
    return render(request,'tut13.html')    
def tut14(request):
    return render(request,'tut14.html')    
def tut15(request):
    return render(request,'tut15.html')    

def level1(request):
    return render(request,'level1.html')
def level2(request):
    return render(request,'level2.html')
def level3(request):
    return render(request,'level3.html')
def level4(request):
    return render(request,'level4.html')
def level5(request):
    return render(request,'level5.html')
def level6(request):
    return render(request,'level6.html')
def level7(request):
    return render(request,'level7.html')
def level8(request):
    return render(request,'level8.html')
def level9(request):
    return render(request,'level9.html')
def level10(request):
    return render(request,'level10.html')
def level11(request):
    return render(request,'level11.html')
def level12(request):
    return render(request,'level12.html')
def level13(request):
    return render(request,'level13.html')
def level14(request):
    return render(request,'level14.html')
def level15(request):
    return render(request,'level15.html')
def level16(request):
    return render(request,'level16.html')
