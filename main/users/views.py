from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            raise ValueError('User is none')

    else: 
        return render(request, "users/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, "users/register.html", context)

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('posts')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)

def view_profile(request, id):
    userprof = User.objects.get(pk=id)
    context = {
        'userprof': userprof
    }

    return render(request, 'users/view_profile.html', context)

# views to display specific profiles details 
# Not the best way, get better and come fix this.
def profile_posts(request, id):
    userprof = User.objects.get(pk=id)
    context = {
        'userprof': userprof
    }

    return render(request, 'users/profile_posts.html', context)

def profile_upvotes(request, id):
    userprof = User.objects.get(pk=id)
    context = {
        'userprof': userprof
    }

    return render(request, 'users/profile_upvotes.html', context)


def profile_downvotes(request, id):
    userprof = User.objects.get(pk=id)
    context = {
        'userprof': userprof
    }

    return render(request, 'users/profile_downvotes.html', context)