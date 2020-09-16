from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome to Finch Collector!</h1>')

def about(request):
    return HttpResponse('<h1>About the Finch Collector</h1>')
