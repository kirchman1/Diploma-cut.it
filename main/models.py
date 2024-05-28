from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Link(models.Model):
    slug = models.SlugField('Unique word for this link', unique=True)
    link = models.CharField('Full link', max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('links')

    def __str__(self):
        return self.slug + ' --- ' + self.link
