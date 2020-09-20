from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.EmailField(max_length=20,blank=True)
    name=models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.name