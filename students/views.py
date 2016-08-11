# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student


def students_list(request):
    students = Student.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    return render(request, 'students/students_list.html', {'students': students})




def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
     return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
     return HttpResponse('<h1>Delete Student %s</h1>' % sid)

#Groups Wiews

def groups_list(request):
    groups = ({'id': 1,
                'name': 'МтМ21',
                'leader': 'Подоба'},
              {'id': 1,
                'name': 'МтМ22',
                'leader': 'Лютый'},
              {'id': 1,
                'name': 'МтМ23',
                'leader': 'Гавр'},
                )
    return render(request, 'students/groups_list.html', {'groups': groups})



def groups_add(request):
     return HttpResponse('<h1>Group Add Form</h1>')



def groups_edit(request, gid):
     return HttpResponse('<h1>Edit Group %s</h1>' % gid)



def groups_delete(request, gid):
     return HttpResponse('<h1>Delete Group %s</h1>' % gid)