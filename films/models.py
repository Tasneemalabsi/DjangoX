from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Film(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.CharField(max_length=4)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("film_detail", args=[str(self.id)])    
