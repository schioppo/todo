from django.urls import path
from .views import TodoApiDetail, TodoApiList

urlpatterns = [
    path('<int:pk>/', TodoApiDetail.as_view()),
    path('', TodoApiList.as_view()),
]