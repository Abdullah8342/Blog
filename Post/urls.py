from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView,create_comment,PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("details/<int:pk>/", PostDetailView.as_view(), name="details"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="update"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("details/<int:article_id>/comment",create_comment, name="create_comment"),
    path("delete/<int:article_id>/",PostDeleteView, name="delete"),
]
