from django.contrib import admin
from student.models import Student, LessonInfo, Lesson

# Register your models here.

admin.site.register(Student)
admin.site.register(LessonInfo)
admin.site.register(Lesson)