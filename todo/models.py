from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])

