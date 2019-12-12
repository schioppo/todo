from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy, reverse
from .forms import CustomCreateForm, CustomUpdateForm
# Create your views here.


class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    ordering = ['-done']


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    form_class = CustomCreateForm


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_edit.html'
    form_class = CustomUpdateForm


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')

