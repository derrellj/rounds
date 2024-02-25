from django.db import models


class Loc(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)

    def __str__(self):
        return self.text[:50]
