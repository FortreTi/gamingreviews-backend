from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=124)
    name = models.CharField(max_length=124)
    password = models.CharField(max_length=124)

    class Meta:
        managed = True
        db_table = 'user'
        unique_together = (('email', 'name', 'password'),)





