from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255)
    fulltime = models.BooleanField()
    level = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(decimal_places=2, max_digits=5)
    deadline = models.DateField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title

class CV(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    cv = models.FileField()
    cover_letter = models.FileField()
    date = models.DateField()

