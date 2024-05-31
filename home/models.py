from django.db import models

# Create your models here.
class Project(models.Model):
    projectimg=models.ImageField(upload_to='media', null=True, blank=True)
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    message=models.TextField(max_length=700,null=True)
    def __str__(self):
        return self.name
    