'''Admin Panel of LifeStories'''
from django.contrib import admin
from .models import Profile,Post,Categories,Comment
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Comment)
