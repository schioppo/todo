from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class SignupViews(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('todo_list')
    template_name = 'signup.html'
    