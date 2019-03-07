from random import randint
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    num = randint(0, 100000)
    context = {
        "html_var": "contect variable from views :)",
        "num_var": num
    }
    return render(request, "base.html", context)

def home1(request):
    return render(request, 'home1.html', {})

def home2(request):
    return render(request, 'home2.html', {})