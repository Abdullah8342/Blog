from django.db import models
from django.conf import settings

# Create your models here.


class MembershipPlan(models.Model):
    '''Membership Plan'''
    PLAN_TYPE_CHOICES = [
        # ('free','FREE'),
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
    '''User Membership'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    membdership = models.ForeignKey(MembershipPlan,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.membdership}"
