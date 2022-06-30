from django.db import models

# Create your models here.

class ReachUp(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    class Meta:
        db_table = "ReachUp"