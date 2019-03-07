from random import randint
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    num = randint(0, 100000)
    return render(request, "base.html", {"html_var": "contect variable from views :)", "num_var": num})