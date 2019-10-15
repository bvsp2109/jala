from django.db import models

# Create your models here.
class JALAModel(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email_id  = models.EmailField()
    Location = models.CharField(max_length=30)
    Massage = models.CharField(max_length=100)


    search_fields = ['title', 'body']
