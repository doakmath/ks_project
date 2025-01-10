from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
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

@api_view(['GET'])
def get_lessons_and_progress(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    lessons = Lesson.objects.all()

    # Create progress records if they don't exist
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

# PUT request to update the progress of a lesson
@api_view(['PUT'])
def update_progress(request, pk):
    try:
        progress = UserLessonProgress.objects.get(pk=pk)
    except UserLessonProgress.DoesNotExist:
        return Response({'error': 'Progress not found'}, status=404)

    serializer = UserLessonProgressSerializer(progress, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# @api_view(['GET', 'POST'])
# def user_progress(request):
#     if request.method == 'GET':
#         user_id = request.query_params.get('user')
#         if not user_id:
#             return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

#         progress = UserLessonProgress.objects.filter(user_id=user_id)
#         serializer = UserLessonProgressSerializer(progress, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = request.data
#         serializer = UserLessonProgressSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update_progress(request, pk):
#     try:
#         progress = UserLessonProgress.objects.get(pk=pk)
#     except UserLessonProgress.DoesNotExist:
#         return Response({'error': 'Progress not found'}, status=404)

#     serializer = UserLessonProgressSerializer(progress, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)

# @api_view(['GET'])
# def get_lessons_and_progress(request, user_id):
#     try:
#         user = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return Response({'error': 'User not found'}, status=404)

#     lessons = Lesson.objects.all()

#     # Create progress records for each lesson if they don't exist
#     for lesson in lessons:
#         UserLessonProgress.objects.get_or_create(user=user, lesson=lesson)

#     # Serialize the lessons and progress
#     lesson_serializer = LessonSerializer(lessons, many=True)
#     progress_serializer = UserLessonProgressSerializer(
#         UserLessonProgress.objects.filter(user=user), many=True
#     )

#     return Response({
#         'lessons': lesson_serializer.data,
#         'progress': progress_serializer.data
#     })


#                                  Quotes endpoints

@api_view(['GET'])
def quotes_list(request):
    quotes = Quotes.objects.all()
    serializer = QuotesSerializer(quotes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def quotes_create(request):
    serializer = QuotesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def quotes_detail(request, pk):
    quote = Quotes.objects.get(id=pk)
    serializer = QuotesSerializer(quote, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def quotes_update(request, pk):
    quote = Quotes.objects.get(id=pk)
    serializer = QuotesSerializer(instance=quote, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def quotes_delete(request, pk):
    quote = Quotes.objects.get(id=pk)
    quote.delete()
    return Response('Quote deleted successfully')


#                                   Image endpoints

@api_view(['GET'])
def image_list(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def image_create(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def image_detail(request, pk):
    image = Image.objects.get(id=pk)
    serializer = ImageSerializer(image, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def image_update(request, pk):
    image = Image.objects.get(id=pk)
    serializer = ImageSerializer(instance=image, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def image_delete(request, pk):
    image = Image.objects.get(id=pk)
    image.delete()
    return Response('Image deleted successfully')


#                                   Resource endpoints

@api_view(['GET'])
def resource_list(request):
    resources = Resource.objects.all()
    serializer = ResourceSerializer(resources, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def resource_create(request):
    serializer = ResourceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def resource_detail(request, pk):
    resource = Resource.objects.get(id=pk)
    serializer = ResourceSerializer(resource, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def resource_update(request, pk):
    resource = Resource.objects.get(id=pk)
    serializer = ResourceSerializer(instance=resource, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def resource_delete(request, pk):
    resource = Resource.objects.get(id=pk)
    resource.delete()
    return Response('Resource deleted successfully')


#                                   Video endpoints

@api_view(['GET'])
def video_list(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def video_create(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def video_detail(request, pk):
    video = Video.objects.get(id=pk)
    serializer = VideoSerializer(video, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def video_update(request, pk):
    video = Video.objects.get(id=pk)
    serializer = VideoSerializer(instance=video, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def video_delete(request, pk):
    video = Video.objects.get(id=pk)
    video.delete()
    return Response('Video deleted successfully')


#                                   Sound endpoints

@api_view(['GET'])
def sound_list(request):
    sounds = Sound.objects.all()
    serializer = SoundSerializer(sounds, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def sound_create(request):
    serializer = SoundSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def sound_detail(request, pk):
    sound = Sound.objects.get(id=pk)
    serializer = SoundSerializer(sound, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def sound_update(request, pk):
    sound = Sound.objects.get(id=pk)
    serializer = SoundSerializer(instance=sound, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def sound_delete(request, pk):
    sound = Sound.objects.get(id=pk)
    sound.delete()
    return Response('Sound deleted successfully')


#                                   Comment endpoints

@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user_sub = request.data.get('user_sub')
        try:
            user = User.objects.get(username=user_sub)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['user'] = user.id  # Associate the comment with the user

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def comment_create(request):
    user_sub = request.data.get('user_sub')
    nickname = request.data.get('nickname')

    try:
        user = User.objects.get(username=user_sub)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

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



@api_view(['GET'])
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def comment_update(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response('Comment deleted successfully')


#                                   Reply endpoints

@api_view(['GET'])
def reply_list(request):
    replies = Reply.objects.all()
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def reply_create(request):
    user_sub = request.data.get('user_sub')
    nickname = request.data.get('nickname')
    comment_id = request.data.get('comment')
    reply_text = request.data.get('reply')

    if not comment_id or not reply_text:
        return Response({"error": "Missing comment or reply text"}, status=400)

    user, created = User.objects.get_or_create(username=user_sub, defaults={'first_name': nickname})

    try:
        comment = Comment.objects.get(id=comment_id)
        reply = Reply.objects.create(
            comment=comment,
            user=user,
            nickname=nickname,  # Save the nickname
            reply=reply_text
        )
        return Response({"message": "Reply created successfully", "reply": {
            "id": reply.id,
            "comment": reply.comment.id,
            "nickname": reply.nickname,
            "reply": reply.reply,
            "created_at": reply.created_at
        }}, status=201)
    except Comment.DoesNotExist:
        return Response({"error": "Comment not found"}, status=404)



@api_view(['GET'])
def reply_detail(request, pk):
    reply = Reply.objects.get(id=pk)
    serializer = ReplySerializer(reply, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def reply_update(request, pk):
    reply = Reply.objects.get(id=pk)
    serializer = ReplySerializer(instance=reply, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def reply_delete(request, pk):
    reply = Reply.objects.get(id=pk)
    reply.delete()
    return Response('Reply deleted successfully')


#                                 Auth0 user sync endpoints

@api_view(['POST'])
def sync_user(request):
    user_data = request.data
    sub = user_data.get('sub')
    email = user_data.get('email')

    user, created = User.objects.get_or_create(username=sub, defaults={'email': email})
    return JsonResponse({'id': user.id, 'created': created})
