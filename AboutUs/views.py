from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def about_us(request):
    return HttpResponse("This will become the about us page")