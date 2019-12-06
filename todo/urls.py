from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('<int:pk>/delete', TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/edit', TodoUpdateView.as_view(), name='todo_edit'),
    path('new/', TodoCreateView.as_view(), name='todo_new'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('', TodoListView.as_view(), name='todo_list'),
]