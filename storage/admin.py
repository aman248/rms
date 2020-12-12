from django.contrib import admin
from .models import Student,School,Marks,Exam,Subject

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(Exam)
admin.site.register(Subject)
