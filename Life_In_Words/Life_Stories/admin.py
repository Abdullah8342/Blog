
from django.contrib import admin

from .models import (
    MembershipPlan,
    UserMembership,
    Profile,
    Category,
    Series,
    Post,
    Tag,
    Comment
)

admin.site.register(MembershipPlan)
admin.site.register(UserMembership)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Series)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
