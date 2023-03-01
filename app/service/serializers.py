from rest_framework import serializers

from .models import Course, Teacher, Webinar


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'bet', 'courses')


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ('id', 'title', 'description', 'status', 'created_at', 'course')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'teacher_set')


class TeacherDetailSerializer(serializers.ModelSerializer):
    courses_detail = CourseSerializer(many=True, read_only=True, source='courses')

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'bet', 'courses_detail')


class CourseDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True, source='teacher_set')
    webinars = WebinarSerializer(many=True, read_only=True, source='webinar_course')

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'teachers', 'webinars')
