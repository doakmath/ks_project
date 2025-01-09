from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__ (self):
        return self.title


class UserLessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.lesson.title} - {"Complete" if self.is_complete else "Incomplete"}'


class Quotes(models.Model):
    quote = models.TextField()

    def __str__(self):
        return self.quote


class Image(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Sound(models.Model):
    title = models.CharField(max_length=255)
    sound_url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message[:30]}...'


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.user.username}'
