from django.db import models

# Create your models here.

class Students(models.Model):
    student_Number=models.PositiveIntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    fiels_of_study=models.CharField(max_length=50)
    gpa=models.FloatField()


    def __str__(self):
          return f'Students: {self.first_name} {self.last_name}'
