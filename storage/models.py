from django.db import models
from django.db.models.expressions import Value

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'<School {self.name}>'
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'<Student {self.name}>'
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'<Subject {self.name}>'
class Exam(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'<Exam {self.name}>'
class Marks(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    value = models.FloatField()
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    def __str__(self):
        return f'<Marks {self.value}>'


