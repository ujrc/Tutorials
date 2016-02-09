from django.db import models

# Create your models here.
class ListItem(models.Model):
    text=models.TextField(default='')
