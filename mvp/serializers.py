# core/serializers.py
from rest_framework import serializers
from .models import Lesson, UserLessonProgress, Quotes, Image, Resource, Video, Sound, Comment, Reply

# Lesson Serializer
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content']

# UserLessonProgress Serializer
class UserLessonProgressSerializer(serializers.ModelSerializer):
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())

    class Meta:
        model = UserLessonProgress
        fields = ['id', 'user', 'lesson', 'is_complete']

# Quote Serializer
class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id', 'quote']

# Image Serializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'image_url', 'description']

# Resource Serializer
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'title', 'link', 'description']

# Video Serializer
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_url', 'description']

# Sound Serializer
class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['id', 'title', 'sound_url', 'description']

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'message', 'created_at']

# Reply Serializer
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'user', 'reply', 'created_at']
