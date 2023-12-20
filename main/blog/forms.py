from django import forms
from .models import Posts, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Create forms here 
class AddPostForm(forms.ModelForm):
    post = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Posts
        fields = ('title', 'avatar', 'author', 'post',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
