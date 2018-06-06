from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  user_name = models.CharField(max_length=101)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

