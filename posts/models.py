from django.db import models

# Create your models here.
class Posts(models.Model):
    text = models.TextField(max_length=50, null=True)
    desc = models.TextField(max_length=255, null=True)

    def __str__(self):  # this function to show the 50 first letter
        return self.text[:50]
