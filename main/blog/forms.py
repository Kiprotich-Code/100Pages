from django import forms
from .models import Posts
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Create forms here 
class AddPostForm(forms.ModelForm):
    post = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Posts
        fields = ('title', 'author', 'post',)

