from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.models import User


from .models import (
    Lesson,
    UserLessonProgress,
    Quotes,
    Image,
    Resource,
    Video,
    Sound,
    Comment,
    Reply,
    )
from .serializers import (
    LessonSerializer,
    UserLessonProgressSerializer,
    QuotesSerializer,
    ImageSerializer,
    ResourceSerializer,
    VideoSerializer,
    SoundSerializer,
    CommentSerializer,
    ReplySerializer
)




# Lessons endpoints

@api_view(['GET'])
def lesson_list(request):
    try:
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lesson_create(request):
    try:
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def lesson_detail(request, pk):
    try:
        lesson = get_object_or_404(Lesson, id=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def lesson_update(request, pk):
    try:
        lesson = get_object_or_404(Lesson, id=pk)
        serializer = LessonSerializer(instance=lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def lesson_delete(request, pk):
    try:
        lesson = get_object_or_404(Lesson, id=pk)
        lesson.delete()
        return Response({'message': 'Lesson deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# User Progress

@api_view(['GET'])
def get_lessons_and_progress(request, user_id):
    try:
        user = get_object_or_404(User, pk=user_id)
        lessons = Lesson.objects.all()

        for lesson in lessons:
            UserLessonProgress.objects.get_or_create(user=user, lesson=lesson)

        lesson_serializer = LessonSerializer(lessons, many=True)
        progress_serializer = UserLessonProgressSerializer(
            UserLessonProgress.objects.filter(user=user), many=True
        )
        return Response({
            'lessons': lesson_serializer.data,
            'progress': progress_serializer.data
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_progress(request, pk):
    try:
        progress = get_object_or_404(UserLessonProgress, pk=pk)
        serializer = UserLessonProgressSerializer(progress, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Quotes endpoints

@api_view(['GET'])
def quotes_list(request):
    try:
        quotes = Quotes.objects.all()
        serializer = QuotesSerializer(quotes, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def quotes_create(request):
    try:
        serializer = QuotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def quotes_detail(request, pk):
    try:
        quote = get_object_or_404(Quotes, id=pk)
        serializer = QuotesSerializer(quote)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def quotes_update(request, pk):
    try:
        quote = get_object_or_404(Quotes, id=pk)
        serializer = QuotesSerializer(instance=quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def quotes_delete(request, pk):
    try:
        quote = get_object_or_404(Quotes, id=pk)
        quote.delete()
        return Response({'message': 'Quote deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Image endpoints

@api_view(['GET'])
def image_list(request):
    try:
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def image_create(request):
    try:
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def image_detail(request, pk):
    try:
        image = get_object_or_404(Image, id=pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def image_update(request, pk):
    try:
        image = get_object_or_404(Image, id=pk)
        serializer = ImageSerializer(instance=image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def image_delete(request, pk):
    try:
        image = get_object_or_404(Image, id=pk)
        image.delete()
        return Response({'message': 'Image deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Resource endpoints

@api_view(['GET'])
def resource_list(request):
    try:
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resource_create(request):
    try:
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def resource_detail(request, pk):
    try:
        resource = get_object_or_404(Resource, id=pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def resource_update(request, pk):
    try:
        resource = get_object_or_404(Resource, id=pk)
        serializer = ResourceSerializer(instance=resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def resource_delete(request, pk):
    try:
        resource = get_object_or_404(Resource, id=pk)
        resource.delete()
        return Response({'message': 'Resource deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Video endpoints

@api_view(['GET'])
def video_list(request):
    try:
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def video_create(request):
    try:
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def video_detail(request, pk):
    try:
        video = get_object_or_404(Video, id=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def video_update(request, pk):
    try:
        video = get_object_or_404(Video, id=pk)
        serializer = VideoSerializer(instance=video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def video_delete(request, pk):
    try:
        video = get_object_or_404(Video, id=pk)
        video.delete()
        return Response({'message': 'Video deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Sound endpoints

@api_view(['GET'])
def sound_list(request):
    try:
        sounds = Sound.objects.all()
        serializer = SoundSerializer(sounds, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sound_create(request):
    try:
        serializer = SoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def sound_detail(request, pk):
    try:
        sound = get_object_or_404(Sound, id=pk)
        serializer = SoundSerializer(sound)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def sound_update(request, pk):
    try:
        sound = get_object_or_404(Sound, id=pk)
        serializer = SoundSerializer(instance=sound, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def sound_delete(request, pk):
    try:
        sound = get_object_or_404(Sound, id=pk)
        sound.delete()
        return Response({'message': 'Sound deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#                                   Comment endpoints

@api_view(['GET', 'POST'])
def comment_list(request):
    try:
        if request.method == 'GET':
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            user_sub = request.data.get('user_sub')
            user = get_object_or_404(User, username=user_sub)

            data = request.data
            data['user'] = user.id  # Associate the comment with the user

            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request):
    try:
        user_sub = request.data.get('user_sub')
        nickname = request.data.get('nickname')

        user = get_object_or_404(User, username=user_sub)

        data = request.data
        data['user'] = user.id

        # Save nickname
        comment = Comment.objects.create(
            user=user,
            nickname=nickname,
            message=data['message']
        )

        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def comment_detail(request, pk):
    try:
        comment = get_object_or_404(Comment, id=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def comment_update(request, pk):
    try:
        comment = get_object_or_404(Comment, id=pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def comment_delete(request, pk):
    try:
        comment = get_object_or_404(Comment, id=pk)
        comment.delete()
        return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#                                   Reply endpoints

@api_view(['GET'])
def reply_list(request):
    try:
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def reply_create(request):
    try:
        user_sub = request.data.get('user_sub')
        nickname = request.data.get('nickname')
        comment_id = request.data.get('comment')
        reply_text = request.data.get('reply')

        if not comment_id or not reply_text:
            return Response({"error": "Missing comment or reply text"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(username=user_sub, defaults={'first_name': nickname})

        comment = get_object_or_404(Comment, id=comment_id)
        reply = Reply.objects.create(
            comment=comment,
            user=user,
            nickname=nickname,
            reply=reply_text
        )

        return Response({"message": "Reply created successfully", "reply": {
            "id": reply.id,
            "comment": reply.comment.id,
            "nickname": reply.nickname,
            "reply": reply.reply,
            "created_at": reply.created_at
        }}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def reply_detail(request, pk):
    try:
        reply = get_object_or_404(Reply, id=pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def reply_update(request, pk):
    try:
        reply = get_object_or_404(Reply, id=pk)
        serializer = ReplySerializer(instance=reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def reply_delete(request, pk):
    try:
        reply = get_object_or_404(Reply, id=pk)
        reply.delete()
        return Response({'message': 'Reply deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#                                 Auth0 user sync endpoints

@api_view(['POST'])
def sync_user(request):
    try:
        user_data = request.data
        sub = user_data.get('sub')
        email = user_data.get('email')

        if not sub or not email:
            return Response({"error": "Missing 'sub' or 'email' in request data"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(username=sub, defaults={'email': email})
        return JsonResponse({'id': user.id, 'created': created})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
