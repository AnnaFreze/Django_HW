from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students_all=Student.objects.all()
    students=students_all.order_by('group').values()
    teachers = Teacher.objects.all()
    context = {'students':students,
               'teachers': teachers,
               }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
