from django.contrib import admin
from .models import TagModel
# Register your models here.

class TagModelAdmin(admin.ModelAdmin):
    list_display = ['user','title']


admin.site.register(TagModel,TagModelAdmin)
