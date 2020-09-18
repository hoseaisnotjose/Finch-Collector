from django.shortcuts import render, redirect
from .models import Finch

# Create your views here.
from django.http import HttpResponse


# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome to Finch Collector!</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })
