from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StudentSerializer, LessonInfoSerializer, LessonSerializer
from .models import Student, LessonInfo, Lesson

# 회원가입
class SignUpAPI(APIView):
    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data)
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

# 로그인
class SignInAPI(APIView):
    def post(self, request):
        data = request.data
        search_id = data['user_id']
        obj = Student.objects.get(user_id=search_id)
        
        if data['user_password'] == obj.user_password:
            return Response('로그인 성공', status=200)
        else:
            return Response('로그인 실패', status=400)
    
# 수업 유형 목록 가져오기    
class LessonInfoListAPI(APIView):
    def get(self, request):
        list = LessonInfo.objects.all()
        serializer = LessonInfoSerializer(list, many=True)
        return Response(serializer.data)

# 수업 유형 생성하기  
class LessonInfoCreateAPI(APIView):
    def post(self, request):
        info = LessonInfoSerializer(data=request.data)
        if info.is_valid():
            info.save()
            return Response(info.data)
        return Response(info.errors, status=400)

# 수업 일정 등록하기
class LessonCreateAPI(APIView):
    def post(self, request):
        data = request.data
        info = LessonInfo.objects.filter(idx=data['type_idx']).exists()
        if info:
            lesson = LessonSerializer(data=data)
            if lesson.is_valid():
                lesson.save()
                return Response('수업 일정이 등록되었습니다.', status=200)
            else:
                return Response('수업 등록 오류', status=400)
        else:
            return Response('수업 유형 오류', status=400)

# 월간 수업 일정 가져오기  
class MonthlyScheduleAPI(APIView):
    def get(self, request):
        year = request.GET.get("year")
        month = request.GET.get("month")
        lessons = list(Lesson.objects.filter(lesson_at__year=year).filter(lesson_at__month=month).values())
        print(lessons)
        
        if lessons:
            result = LessonSerializer(lessons, many=True)
            return Response(result.data)
        else:
            return Response('수업 일정 없음', status=400)