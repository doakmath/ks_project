from django.urls import path
from . import views

urlpatterns = [
    # Lessons endpoints
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/create/', views.lesson_create, name='lesson_create'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:pk>/update/', views.lesson_update, name='lesson_update'),
    path('lessons/<int:pk>/delete/', views.lesson_delete, name='lesson_delete'),
    # User Progress endpoints
    path('progress/<int:user_id>/', views.get_lessons_and_progress, name='get_lessons_and_progress'),
    path('progress/update/<int:pk>/', views.update_progress, name='update_progress'),
    # Quotes endpoints
    path('quotes/', views.quotes_list, name='quotes_list'),
    path('quotes/create/', views.quotes_create, name='quotes_create'),
    path('quotes/<int:pk>/', views.quotes_detail, name='quotes_detail'),
    path('quotes/<int:pk>/update/', views.quotes_update, name='quotes_update'),
    path('quotes/<int:pk>/delete/', views.quotes_delete, name='quotes_delete'),
    # Image endpoints
    path('image/', views.image_list, name='image_list'),
    path('image/create/', views.image_create, name='image_create'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    path('image/<int:pk>/update/', views.image_update, name='image_update'),
    path('image/<int:pk>/delete/', views.image_delete, name='image_delete'),
    # Resource endpoints
    path('resource/', views.resource_list, name='resource_list'),
    path('resource/create/', views.resource_create, name='resource_create'),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('resource/<int:pk>/update/', views.resource_update, name='resource_update'),
    path('resource/<int:pk>/delete/', views.resource_delete, name='resource_delete'),
    # Video endpoints
    path('video/', views.video_list, name='video_list'),
    path('video/create/', views.video_create, name='video_create'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('video/<int:pk>/update/', views.video_update, name='video_update'),
    path('video/<int:pk>/delete/', views.video_delete, name='video_delete'),
    # Sound endpoints
    path('sound/', views.sound_list, name='sound_list'),
    path('sound/create/', views.sound_create, name='sound_create'),
    path('sound/<int:pk>/', views.sound_detail, name='sound_detail'),
    path('sound/<int:pk>/update/', views.sound_update, name='sound_update'),
    path('sound/<int:pk>/delete/', views.sound_delete, name='sound_delete'),
    # Comment endpoints
    path('comment/', views.comment_list, name='comment_list'),
    path('comment/create/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    # Reply endpoints
    path('reply/', views.reply_list, name='reply_list'),
    path('reply/create/', views.reply_create, name='reply_create'),
    path('reply/<int:pk>/', views.reply_detail, name='reply_detail'),
    path('reply/<int:pk>/update/', views.reply_update, name='reply_update'),
    path('reply/<int:pk>/delete/', views.reply_delete, name='reply_delete'),
    # Sync user endpoints
    path('sync_user/', views.sync_user, name='sync_user'),
]
