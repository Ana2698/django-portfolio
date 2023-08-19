from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()
# Create your models here.
