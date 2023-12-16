from django.contrib import admin
from .models import Posts
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostsAdmin(SummernoteModelAdmin):
    summernote_fields = ('post',)


admin.site.register(Posts, PostsAdmin)