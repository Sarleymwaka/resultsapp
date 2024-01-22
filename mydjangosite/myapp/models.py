from django.db import models
import calculation

class Result(models.Model):
    name = models.CharField( max_length=50,null=True)
    maths = models.CharField(max_length=50,null=True)
    english = models.CharField(max_length=50,null=True)
    science = models.CharField(max_length=50,null=True)
    average = models.CharField(max_length=50,null=True)


def __str__(self):
    return self.name

