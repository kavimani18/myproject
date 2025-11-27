from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gm_view(request):
    return HttpResponse('<h2> Good Morning </h2>')

def ga_view(request):
    return HttpResponse('<h2> Good Afternoon </h2>')

def ge_view(request):
    return HttpResponse('<h2> Good Evening </h2>')

def student_detail(request, id): 
   return HttpResponse(f"<h2>Student ID is {id}</h2>")