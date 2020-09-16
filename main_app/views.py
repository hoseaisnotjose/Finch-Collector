from django.shortcuts import render
# from .models import Finch

# Create your views here.
from django.http import HttpResponse

class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name,
        self.breed = breed,
        self.description = description,
        self.age = age
        
finches = [
    Finch('Kiwi', 'Firetail', 'Aussie', '2'),
    Finch('Pierre', 'Bramling', 'Euro', '3'),
    Finch('Skittles', 'Gold', 'bling', '1')
]

# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome to Finch Collector!</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })
