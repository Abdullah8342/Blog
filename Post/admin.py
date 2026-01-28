from django.contrib import admin
from .models import Article,Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['user','title']
    search_fields = ['title']


admin.site.register(Article,ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','description','article']

admin.site.register(Comment,CommentAdmin)
