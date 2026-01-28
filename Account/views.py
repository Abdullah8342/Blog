from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

class UserSignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'Account/signup_page.html'
    success_url = reverse_lazy('login')
    context_object_name = 'form'

def CustomLogOutView(request):
    logout(request)
    print(request.user)
    return redirect('login')

