from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toy
from .forms import FeedingForm


from django.http import HttpResponse
# Create your views here.
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']
    
class FinchUpdate(UpdateView):
    model = Finch
        # we don't want to "update" finch name so we exclude it from name field!
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


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
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form
        })
    
def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in the request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

