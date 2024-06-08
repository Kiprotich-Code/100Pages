from django import forms
from .models import Posts, Comment, UserFeedback
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Row, Column


# Create forms here 
class AddPostForm(forms.ModelForm):
    post = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Posts
        fields = ('title', 'avatar', 'post',)

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('title', 'avatar', css_class='col-md-4'),
                Column('post', css_class='col-md-8'),
            ),
            Submit('submit', u'Add Poem', css_class='btn btn-primary'),
        )             


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Subject'}),
            'message': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Message'}),
        }



