from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    '''Category'''
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    '''Post'''
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,blank=True,
        related_name='posts'
    )
    order = models.PositiveIntegerField(null=True,blank=True)
    cover_image = models.ImageField(upload_to='post_images/',null=True,blank=True)
    is_published = models.BooleanField(default=True)
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    '''Tag'''
    label = models.CharField(max_length=50,unique=True)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return f"{self.label}"


class Comment(models.Model):
    '''Comment'''
    STARS = [
        ('5','Five Stars'),
        ('4','Four Stars'),
        ('3','Three Stars'),
        ('2','Two Stars'),
        ('1','One Star'),
    ]
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(max_length=100,choices=STARS,default='5')


    def __str__(self):
        return f"{self.user}"
