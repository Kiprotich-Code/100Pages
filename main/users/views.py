from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from blog.models import Posts

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
    userprof = User.objects.get(id=id)
   

    context = {
        'userprof': userprof,
    }

    return render(request, 'users/view_profile.html', context)


# views to display specific profiles details 
# Not the best way, get better and come fix this.
def profile_posts(request, user_id):
    userprof = get_object_or_404(User, id=user_id)
    my_posts = Posts.objects.filter(author=userprof)

    context = {
        'userprof': userprof,
        'my_posts': my_posts,
    }

    return render(request, 'users/profile_posts.html', context)

def profile_upvotes(request, id):
    userprof = get_object_or_404(User, id=id)
    context = {
        'userprof': userprof
    }

    return render(request, 'users/profile_upvotes.html', context)


def profile_downvotes(request, id):
    userprof = get_object_or_404(User, id=id)
    context = {
        'userprof': userprof
    }

    return render(request, 'users/profile_downvotes.html', context)

def author_profile(request, user_id):
    author = get_object_or_404(User, id=user_id)
    my_posts = Posts.objects.filter(author=author)
    return render(request, 'users/author_profile.html', {'author': author, 'my_posts': my_posts})