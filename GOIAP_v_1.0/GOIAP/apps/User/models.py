from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Perfil(models.Model):
    fk_authUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rol=models.CharField(max_length=100)
