from django.db import models


# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13,null=True)
    project = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class about(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic')
    def __str__(self):
        return f'{self.title}'

class address(models.Model):
    location = models.CharField(max_length=100)
    email = models.EmailField()
    nationality = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,null=True)
    site = models.CharField(max_length=100,null=True)
    def __str__(self):
        return f'{self.location}'

