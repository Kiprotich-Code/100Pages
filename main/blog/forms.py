from django import forms
from .models import Posts, Comment, UserFeedback
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Create forms here 
class AddPostForm(forms.ModelForm):
    post = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Posts
        fields = ('title', 'avatar', 'post',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = '__all__'

