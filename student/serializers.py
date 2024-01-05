from django.core import serializers
from rest_framework import serializers
from .models import Student, LessonInfo, Lesson

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