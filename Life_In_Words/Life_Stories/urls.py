from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('profile/',views.ProfileApiView.as_view(),name = 'profile'),
    path('profile/posts/',views.PostsApiView.as_view(),name = 'posts'),
    path('profile/post/<int:pk>/',views.PostApiView.as_view(),name = 'post'),
    path('posts/',views.ReaderPostsAPIView.as_view(),name = 'posts'),
    path('post/<int:pk>/',views.ReaderPostDetailAPIView.as_view(),name = 'postDetail'),
    path('comment/<int:pk>/',views.CommentApiView.as_view(),name='comment'),
    path('category/',views.CategoryApiView.as_view(),name = 'category'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
