from .models import Teacher, Webinar


def get_teacher_webinars(teacher: Teacher) -> list[Webinar]:
    """
    Возвращает список доступных преподавателю вебинаров
    :param teacher: Teacher
    :return: list[Webinar]
    """

    teacher = Teacher.objects.get(pk=teacher.pk)
    webinars: list[Webinar] = []

    for course in teacher.courses.all():
        for webinar in course.webinar_course.all():
            webinars.append(webinar)

    return webinars


def calculate_salary(teacher: Teacher) -> int:
    """
    Подсчёт зарплаты, с учётом уже выплаченной
    :param teacher: Teacher
    :return: int
    """
    teacher = Teacher.objects.get(pk=teacher.pk)
    spent = 0

    for webinar in get_teacher_webinars(teacher):
        if webinar.status == webinar.Status.FINISHED:
            if webinar.pk not in teacher.paid_courses:
                spent += 1  # я предположил, что занятие длится один час
                teacher.paid_courses.append(webinar.pk)

    teacher.save()
    return spent * teacher.bet
