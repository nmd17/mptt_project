from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import File
from .forms import AddFileForm


def show_files(request):
    return render(request, "homepage.html", {'files': File.objects.all()})

def add_files(request):
    if request.method == 'POST':
        form = AddFileForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/files/')
    else:
        form = AddFileForm()

    return render(request, "file_form.html", {'form': form})

