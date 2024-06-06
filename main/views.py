from django.shortcuts import render
from .models import Student, Group, Title, Station


def welcome_view(request):

    return render(request, 'base.html')


def student_view(request):
    students = Student.objects.all()
    groups = Group.objects.all()
    context = {
        'students': students,
        'groups': groups
    }
    return render(request, 'main/students.html', context)


def groups_view(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'main/groups.html', context)


def titles_view(request):
    titles = Title.objects.all()
    stations = Station.objects.all()
    context = {
        'titles': titles,
        'stations': stations
    }
    return render(request, 'main/titles.html', context)


def stations_view(request):
    stations = Station.objects.all()
    context = {'stations': stations}
    return render(request, 'main/students.html', context)


def exams_view(request):

    return render(request, 'main/exam.html')


def pass_exams_view(request, student_pk, station_pk):
    # student = Student.objects.get(pk=student_pk)
    # station = Station.objects.get(pk=station_pk)
    if request.method == 'POST':
        print(request.POST.get('1'))
        print(request.POST.get('2'))
        print(request.POST.get('3'))
        print(request.POST.get('4'))

    return render(request, 'main/exam.html', {'student_pk': student_pk, 'station_pk': station_pk, 'list_s': range(1, 6)})



