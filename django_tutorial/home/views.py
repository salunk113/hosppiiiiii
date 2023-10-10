from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    person = {
        'name': 'saalu',
        'age': 30,
        'place': 'calicut',
        
    }
    numbers = {
        'num1': 0,
    }
    num = {
        'num' : [1,2,3,4,5,6,7,8,9],
    }
    return render(request, 'index.html',num,)

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html')