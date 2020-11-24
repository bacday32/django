from django.contrib import admin
from .models import Question
from .models import Course

admin.site.register(Question)


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'num_lessons')


admin.site.register(Course, CourseAdmin)
