from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.title}'

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.article.title} - {self.description}'
