from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import File
from .forms import AddFileForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views import View


def add_files(request):
    if request.method == 'POST':
        form = AddFileForm(request.POST,initial={"name": request.user.username}, user=request.user)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/files/')
    else:
        form = AddFileForm(initial={"name": request.user.username}, user=request.user)

    return render(request, "file_form.html", {'form': form})

def homepage(request):
    if request.user.is_authenticated:
        return redirect('/' + request.user.username + '/')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignUpForm(data=request.POST)
                if signupform.is_valid():
                    data = signupform.cleaned_data
                    user = User.objects.create_user(username=data['username'], password=data['password'])
                    login(request, user)
                    return redirect('/')
            else:
                signinform = SignInForm(data=request.POST)
                signupform = SignUpForm()
        
                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')
        else:
            signupform = SignUpForm()
            signinform = SignInForm()
  
    return render(request, 'homepage.html', {'signupform': signupform, 'signinform': signinform})

class profile(View):
    def get(self, request, *args, **kwargs):
        tree = ''

        try:
            tree = File.objects.get(name=request.user.username).get_descendants(include_self=True)
        except:
            print('This user does not have a tree yet')

        return render(request, 'profile.html', {'files': tree})

def logout_request(request):
    logout(request)
    print('hello')
    return redirect('/')




