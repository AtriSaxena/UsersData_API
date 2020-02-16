from django.db import models

# Create your models here.
class UsersData(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    email = models.EmailField(max_length=50)
    web = models.CharField(max_length=100)
    