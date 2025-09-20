
from django.contrib import admin
from Membership.models import MembershipPlan,UserMembership

from .models import (
    Category,
    Post,
    Tag,
    Comment
)

admin.site.register(MembershipPlan)
admin.site.register(UserMembership)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
