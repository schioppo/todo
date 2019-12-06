from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy, reverse

# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = ('title', 'description', 'author')

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_edit.html'
    fields = ('title', 'description', 'done')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')
    





