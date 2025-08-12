from django.db import models
from django.conf import settings

# Create your models here.


class MembershipPlan(models.Model):
    '''Membership'''
    PLAN_TYPE_CHOICES = [
        ('basic','BASIC'),
        ('premium','PREMIUM'),
    ]
    DURATION_TYPE_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
    name = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=100,choices=PLAN_TYPE_CHOICES)
    duration_type = models.CharField(max_length=100,choices=DURATION_TYPE_CHOICES)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"


class UserMembership(models.Model):
    '''Membership'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    membdership = models.ForeignKey(MembershipPlan,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.membdership}"


class Profile(models.Model):
    '''Profile'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11,null=True,blank=True)
    location = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images/',null=True,blank=True)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} { self.last_name}"

class Category(models.Model):
    '''Category'''
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"



class Series(models.Model):
    '''Series'''
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    created_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.title}"



class Post(models.Model):
    '''Post'''
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts')
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
    series = models.ForeignKey(Series,on_delete=models.SET_NULL,null=True,blank=True)
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
