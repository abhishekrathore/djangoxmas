from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200,unique=True)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name+"("+str(self.age)+")"
