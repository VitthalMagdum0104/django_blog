from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
import datetime


class Blog(models.Model):
    serial_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.SlugField(max_length=10)
    timeStamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title + " by " + self.author.username
