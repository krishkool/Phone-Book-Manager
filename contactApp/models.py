from django.db import models


# Create your models here.
class ContactBook(models.Model):
    Name = models.CharField(max_length=20)
    Contact = models.CharField(max_length=15)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
