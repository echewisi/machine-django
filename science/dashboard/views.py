from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data 

def index(request):
    if request.method == 'POST':
        form= DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashbrd-predictions')
    else:
        form= DataForm()
    context={
            'form':form
        }
    return render(request, 'dashbrd/index.html', context)

def predcitions(request):
    predicted_sports=  Data.objects.all()
    context={
        'predicted_sports': predicted_sports
    }
    return render(request, 'dashbrd/predictions.html', context)

# Create your views here.
