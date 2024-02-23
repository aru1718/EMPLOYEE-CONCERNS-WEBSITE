from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ConcernForm
from .models import Concern


def concerns_list(request):
    concerns = Concern.objects.all().order_by('-date_posted')
    return render(request, 'concerns/concerns_list.html', {'concerns': concerns})

def create_concern(request):
    if request.method == 'POST':
        form = ConcernForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('concerns_list')
    else:
        form = ConcernForm()
    return render(request, 'concerns/create_concern.html', {'form': form})

def delete_concern(request, pk):
    concern = Concern.objects.get(pk=pk)
    if request.method == 'POST':
        concern.delete()
        return redirect('concerns_list')
    return render(request, 'concerns/concerns_list.html')
