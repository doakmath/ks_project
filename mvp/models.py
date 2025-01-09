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
