from django.db import models
# Create your models here.

class UsersDetail(models.Model):
    Name = models.TextField()
    Gender = models.CharField(max_length=2)
    Birthtown = models.TextField()
    birth_date = models.CharField(max_length=255)
    Street = models.TextField()
    Hometown = models.TextField()
    Class = models.TextField()
    start_date = models.DateField()
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.Name