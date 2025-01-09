from rest_framework import serializers
from .models import Lesson, UserLessonProgress


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content']


class UserLessonProgressSerializer(serializers.ModelSerializer):
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())

    class Meta:
        model = UserLessonProgress
        fields = ['id', 'user', 'lesson', 'is_complete']
