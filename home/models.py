from distutils.command.upload import upload
import email
from email.mime import image
from unicodedata import name
from django.db import models

class Project(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    code = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + '-' + self.email