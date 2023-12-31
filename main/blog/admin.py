from django.contrib import admin
from .models import Posts, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('commenter', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Posts, PostsAdmin)