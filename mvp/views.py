from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Lesson, UserLessonProgress
from .serializers import LessonSerializer, UserLessonProgressSerializer



#                                   Lessons endpoints

@api_view(['GET'])
def lesson_list(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def lesson_create(request):
    serializer = LessonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def lesson_detail(request, pk):
    lesson = Lesson.objects.get(id=pk)
    serializer = LessonSerializer(lesson, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def lesson_update(request, pk):
    lesson = Lesson.objects.get(id=pk)
    serializer = LessonSerializer(instance=lesson, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def lesson_delete(request, pk):
    lesson = Lesson.objects.get(id=pk)
    lesson.delete()
    return Response('Lesson deleted successfully')

#                                     User Progress

@api_view(['GET', 'POST'])
def user_progress(request):
    if request.method == 'GET':
        user_id = request.query_params.get('user')
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        progress = UserLessonProgress.objects.filter(user_id=user_id)
        serializer = UserLessonProgressSerializer(progress, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = UserLessonProgressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
