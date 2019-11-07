from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'Name: {self.name} Course: {self.course}'


class Course(models.Model):
    name = models.CharField(max_length=100)
     
    def __str__(self):
        return self.name