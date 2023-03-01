from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'username', 'bet')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'bet')


class WebinarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'course')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Webinar, WebinarAdmin)
admin.site.register(Course, CourseAdmin)
