from django.urls import path

from .views import UserSignUpView,CustomLogOutView
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',UserSignUpView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',CustomLogOutView,name='logout'),
]
