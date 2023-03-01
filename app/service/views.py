from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Teacher, Webinar, Course
from .serializers import TeacherSerializer, WebinarSerializer, CourseSerializer, TeacherDetailSerializer,\
    CourseDetailSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .service import calculate_salary

response_400 = openapi.Response('BAD_REQUEST')
teacher_response_get = openapi.Response('Teachers list', TeacherSerializer(many=True))
teacher_response_detail_get = openapi.Response('Teacher object', TeacherDetailSerializer)

webinar_response_get = openapi.Response('Webinars list', WebinarSerializer(many=True))
webinar_response_detail_get = openapi.Response('Webinar object', WebinarSerializer)

course_response_get = openapi.Response('Courses list', CourseSerializer(many=True))
course_response_detail_get = openapi.Response('Course object', CourseDetailSerializer)


@swagger_auto_schema(method='get', responses={200: teacher_response_get})
@swagger_auto_schema(method='post', request_body=TeacherSerializer)
@api_view(['GET', 'POST'])
def api_teacher(request):
    if request.method == 'GET':
        clients = Teacher.objects.all()
        serializer = TeacherSerializer(clients, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: teacher_response_detail_get})
@swagger_auto_schema(methods=['put', 'patch'], request_body=TeacherSerializer)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherDetailSerializer(teacher)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: webinar_response_get})
@swagger_auto_schema(method='post', request_body=WebinarSerializer)
@api_view(['GET', 'POST'])
def api_webinar(request):
    if request.method == 'GET':
        webinars = Webinar.objects.all()
        serializer = WebinarSerializer(webinars, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = WebinarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: webinar_response_detail_get})
@swagger_auto_schema(methods=['put', 'patch'], request_body=WebinarSerializer)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_webinar_detail(request, pk):
    try:
        webinar = Webinar.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WebinarSerializer(webinar)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = WebinarSerializer(webinar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        webinar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: course_response_get})
@swagger_auto_schema(method='post', request_body=CourseSerializer)
@api_view(['GET', 'POST'])
def api_course(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: course_response_detail_get})
@swagger_auto_schema(methods=['put', 'patch'], request_body=CourseSerializer)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', operation_description="Выполняет подсчёт заработной платы для преподавателя", responses={
    200: 'int',
    404: 'Teacher not found'
})
@api_view(['GET'])
def api_calculate_salary(request, pk):
    """
    Выполняет подсчёт заработной платы для преподавателя
    :param request:
    :param pk: int
    :return:
    """
    try:
        teacher = Teacher.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response('Teacher not found', status=status.HTTP_404_NOT_FOUND)

    return Response(calculate_salary(teacher), status=status.HTTP_200_OK)
