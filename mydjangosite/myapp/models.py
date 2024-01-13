from django.db import models

class Result(models.Model):
    name = models.CharField(max_length=50)
    math = models.CharField(max_length=50)
    english = models.CharField(max_length=50)
    science = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.name