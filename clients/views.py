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

def leaderboard(request):
    users = clients_model.objects.all()
    temp_user_list = []
    for user in users:
        temp_user_list.append([user.globalScore, user.username])
    print('before sorting',temp_user_list)
    temp_user_list.sort()
    print('after sorting',temp_user_list)    
    temp_user_list.reverse()
    userlist = []
    for element in temp_user_list:
        temp = {'username':element[1],'score':element[0]}
        userlist.append(temp)
    return render(request,'leaderboard.html', {'user':userlist})    