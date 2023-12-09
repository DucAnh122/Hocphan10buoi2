from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registration
# Create your views here.
def store(request):
    return render(request, 'store.html',{})

def register(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'register.html', {'form': form})    

