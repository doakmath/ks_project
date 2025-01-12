from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import (
    Lesson,
    UserLessonProgress,
    Image,
    Resource,
    Video,
    Sound,
    Comment,
    Reply,
    Quotes,
)

# Inline class to display lesson progress within the user page
class UserLessonProgressInline(admin.TabularInline):
    model = UserLessonProgress
    extra = 0
    fields = ('lesson', 'is_complete')
    can_delete = False
    readonly_fields = ('lesson', 'is_complete')


# Extend the built-in User admin to include lesson progress
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    inlines = [UserLessonProgressInline]

# Unregister the default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register the other models
admin.site.register(Lesson)
admin.site.register(Image)
admin.site.register(Resource)
admin.site.register(Video)
admin.site.register(Sound)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Quotes)
