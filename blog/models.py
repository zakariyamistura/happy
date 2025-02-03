from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Met:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
