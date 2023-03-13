from django.db import models


# Create your models here.
class Posts(models.Model):
    text = models.TextField(max_length=50, null=True)
    desc = models.TextField(max_length=255, null=True)
    blog_image = models.ImageField(
        upload_to="files/covers",
        null=True,
    )
    author_image = models.ImageField(
        upload_to="files/covers",
        null=True,
    )
    author = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):  # this function to show the 50 first letter
        return self.text[:50]
