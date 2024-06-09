from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from blog.models import Posts
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from blog.forms import FeedbackForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('Login Successful'))
            return redirect('profile')

        else:
            messages.success(request, 'Enter valid login details and try again!')
            return redirect('login')

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
            messages.success(request, ('You\'ve successfully created an account!'))
            return redirect('login')
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, "users/register.html", context)


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            messages.success(request, ('Successfully updated profile!'))
            u_form.save()
            p_form.save()

            return redirect('posts')
        
        else:
            return redirect('posts')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


@login_required()
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
    paginator = Paginator(my_posts, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'userprof': userprof,
        'my_posts': my_posts,
        'page_obj': page_obj,
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


# follow and unfollow user 
@login_required()
def follow_user(request, user_id):
    user_to_follow =get_object_or_404(User, id=user_id)
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    user_profile.followers.add(user_to_follow)
    return redirect('author_profile', id=user_id)


@login_required()
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    user_profile = Profile.objects.get(user=request.user)
    user_profile.followers.remove(user_to_unfollow)
    return redirect('author_profile', id=user_id)