from django.shortcuts import render, redirect
from .models import Posts
from .forms import AddPostForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

# Listview for posts 
def post_list(request):
    context = {}
    posts = Posts.objects.all()

    context['posts'] = posts
    return render(request, 'blog/posts.html', context)


def add_posts(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
        else:
            raise ValueError('Invalid Form')
        
    else:
        form = AddPostForm()

    context = {'form': form}    
    return render(request, 'blog/add_post.html', context)