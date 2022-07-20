from pyexpat import model
from django.db import models

# Create your models here.
class destination(models.Model):
    img = models.ImageField(upload_to='pics') 
    title = models.CharField(max_length=100)
    desc = models.TextField()

class Products(models.Model):
    img = models.ImageField(upload_to='pics') 
    title = models.CharField(max_length=100)
    desc = models.TextField()
    def __str__(self):
        return self.title


class Contact(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email_address = models.EmailField(max_length = 150)
	message = models.TextField(max_length = 2000)
