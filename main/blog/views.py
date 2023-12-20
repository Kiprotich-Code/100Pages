from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from .forms import AddPostForm, CommentForm

# Create your views here.
# Listview for posts 
def post_list(request):
    posts = Posts.objects.all().order_by('-upvotes', 'downvotes')
    latest_post = Posts.objects.order_by('-created_on')[0:3]
    trending_post = Posts.objects.order_by('-upvotes', 'downvotes')[0:3]

    context = {
        'posts': posts,
        'latest_post': latest_post,
        'trending_post': trending_post
    }
    return render(request, 'blog/posts.html', context)


def add_posts(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
        else:
            raise ValueError('Invalid Form')
        
    else:
        form = AddPostForm()

    context = {'form': form}    
    return render(request, 'blog/add_post.html', context)


# Detail view for post 
def post_detail(request, id):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Posts, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None # Posted Comment
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create a comment object but don't save it to the database 
            new_comment = comment_form.save(commit=False)
            # Assign current post to the comment 
            new_comment.post = post
            # Save the comment to the database 
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form':comment_form, 
    }
    return render(request, template_name, context)


def upvote_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.upvotes += 1
    post.save()
    return redirect('posts')

def downvote_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.downvotes += 1
    post.save()
    return redirect('posts')
    