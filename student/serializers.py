from django.core import serializers
from rest_framework import serializers
from .models import Student, LessonInfo, Lesson, Enrolment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonInfo
        fields = '__all__'
        
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        
class EnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolment
        fields = '__all__'