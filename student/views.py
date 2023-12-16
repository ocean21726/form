from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

class SignUpAPI(APIView):
    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data)
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SignInAPI(APIView):
    def post(self, request):
        data = request.data
        search_id = data['user_id']
        obj = Student.objects.get(user_id=search_id)
        
        if data['user_password'] == obj.user_password:
            return Response('로그인 성공', status=200)
        else:
            return Response('로그인 실패', status=400)