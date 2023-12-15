from django import forms
from .models import Posts

# Create forms here 
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'