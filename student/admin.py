from django.contrib import admin
from student.models import Student, LessonInfo, Lesson, Enrolment

# Register your models here.

admin.site.register(Student)
admin.site.register(LessonInfo)
admin.site.register(Lesson)
admin.site.register(Enrolment)