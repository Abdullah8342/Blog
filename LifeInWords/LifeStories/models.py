'''LifeStories'''
from django.utils.timezone import now
from django.conf import settings
from django.urls import reverse
from django.db import models
# Create your models here.


class Profile(models.Model):
    '''
    Profile
    '''
    user = models.OneToOneField (
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)



class Categories(models.Model):
    '''
    Categories
    '''
    title = models.CharField(max_length=150)

    def __str__(self):
        '''string'''
        return f"{self.title}"



class Post(models.Model):
    '''
    Post
    '''
    title=models.CharField(max_length=255)
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    content=models.TextField()
    categories = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        related_name='post'
    )
    image = models.ImageField(upload_to="post_images", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title

    def get_absolute_url(self):
        '''
        Unknown
        '''
        return reverse('blogs')


class Comment(models.Model):
    '''
    Comment
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment')
    content = models.TextField()
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username}  Comment: {self.content}"

