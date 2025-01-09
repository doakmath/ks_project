from django.contrib import admin
from .models import (
    Lesson,
    UserLessonProgress,
    Image,
    Resource,
    Video,
    Sound,
    Comment,
    Reply
    )


admin.site.register(Lesson)

admin.site.register(UserLessonProgress)

admin.site.register(Image)

admin.site.register(Resource)

admin.site.register(Video)

admin.site.register(Sound)

admin.site.register(Comment)

admin.site.register(Reply)
