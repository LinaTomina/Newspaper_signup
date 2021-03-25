from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length = 255, unique = True)
    subscriber = models.ForeignKey(User, default = None, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.category_name.title()}'

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique = True, verbose_name = 'Наименование категории')