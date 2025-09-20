'''Routers'''
from rest_framework_nested import routers
from django.urls import path,include
from . import views

router = routers.SimpleRouter()
router.register('blog',views.BlogsViewset)
comment_router = routers.NestedSimpleRouter(router,'blog',lookup = 'blog')
comment_router.register('comment',views.CommentViewset,basename='comments')


urlpatterns = [
#     blogs
    path('',include(router.urls)),
    path('',include(comment_router.urls)),


#     profile
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
    path("edit_profile/", views.EditProfile.as_view(), name="edit_profile"),
]
