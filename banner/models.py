from django.db import models

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banner')
    text_one = models.CharField(max_length=20)
    text_two = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.text_one
