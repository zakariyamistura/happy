from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 150)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Met:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
