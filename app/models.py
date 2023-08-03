from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Plan(models.Model):
    title = models.CharField(max_length=255, verbose_name="Reja nomi")
    limit = models.DateTimeField(verbose_name="Tugash vaqti")

    def __str__(self):
        return self.title