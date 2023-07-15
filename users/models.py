from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class VerifyLogin(models.Model):
    username = models.CharField(max_length=255)
    verifying = models.CharField(max_length=255)
