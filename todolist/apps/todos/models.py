from django.db import models


class Todos(models.Model):
    user = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    priority = models.SmallIntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
