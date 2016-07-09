# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = ({'id': 1,
                 'first_name': u'Грибок',
                 'last_name': u'Подоба',
                 'ticket': 235,
                 'image': 'img/me.jpg'},
                {'id': 2,
                 'first_name': u'Корост',
                 'last_name': u'Андрій',
                 'ticket': 2123,
                 'image': 'img/me.jpg'},
                {'id': 3,
                 'first_name': 'Лютый',
                 'last_name': u'Слава',
                 'ticket': 2120,
                 'image': 'img/me.jpg'})

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