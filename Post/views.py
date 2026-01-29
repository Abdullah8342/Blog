from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.


class PostCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "Post/article_create.html"
    success_url = reverse_lazy("post")
    context_object_name = "form"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Article
    template_name = "Post/article_list.html"
    context_object_name = "ArticleList"

    def get_queryset(self):
        try:
            if self.request.GET['q']:
                articles_list = Article.objects.filter(
                    title__icontains=self.request.GET['q']
                )
                return articles_list
            return super().get_queryset()
        except:
            return super().get_queryset()


class PostDetailView(DetailView):
    model = Article
    template_name = "Post/article_details.html"
    context_object_name = "Article"


class PostUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "Post/article_update.html"
    context_object_name = "form"
    success_url = reverse_lazy("post")


def PostDeleteView(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        if article.user == request.user:
            article.delete()
            return redirect("post")
        return HttpResponse("You Not Have Permission for Deleting This Post")
    return render(request, "Post/article_delete.html", {"article": article})


def create_comment(request, article_id):
    try:
        if request.method == "POST":
            form = CommentForm(request.POST)
            article = get_object_or_404(Article, id=article_id)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.article = article
                form.save()
                return redirect(reverse("details", kwargs={"pk": article_id}))
            return HttpResponse("Form is Not Valid")
        form = CommentForm()
        return render(request, "Post/comment_create.html", {"form": form})
    except:
        return redirect("login")
