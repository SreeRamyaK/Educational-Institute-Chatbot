from django.contrib.auth.models import AbstractUser
from django.db import models

class custom_user(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class user_personal_model(models.Model):
    user = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    registration_flag = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}, Age: {self.age}, User: {self.user.username}"


class staff_database(models.Model):
    user = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True)
    post = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    imagefile = models.ImageField(upload_to='images/')
    registration_flag = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.post} at {self.school}"

