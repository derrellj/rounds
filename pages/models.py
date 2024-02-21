from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100, blank=True)
    about = models.TextField()
    image = models.ImageField(upload_to="uploads")

    def __str__(self):
        return self.name[:50]
