from django.urls import path
from .views import SignupViews

urlpatterns = [
    path('signup/', SignupViews.as_view(), name='signup'),
]