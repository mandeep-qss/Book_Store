from django.db import models
from django.conf import settings
from Author.models import User

# Create your models here.
class Book(models.Model):
    author=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=200,null=True)
    Price=models.IntegerField()
    Edition=models.IntegerField()

    class Meta:
        db_table = 'book'