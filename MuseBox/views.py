from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SelectionChansons

def index(request):
    if request.method == 'POST':
        form = request.POST
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SelectionChansons()

    return render(request, 'index.html', {'form': form})