
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all()
    return render(request, 'myfirst.html', {'mymembers': mymembers})


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())



def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('var.html')
  context = {
    'num':5,
    'names':['Alice', 'Bob', 'Charlie', 'David'],
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Chevrolet',
        'model': 'Camaro',
        'year': '1966',
      },
      {
        'brand': 'Dodge',
        'model': 'Charger',
        'year': '1968',
      }
    ],
  
  }
  return HttpResponse(template.render(context, request))





