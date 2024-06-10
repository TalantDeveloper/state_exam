from django.shortcuts import render

from .functions import contexts_func
from .models import Student, Group, Title, Station, General, Result


def welcome_view(request):
    context = contexts_func(request)
    context['talaba'] = Student.objects.all().count()
    return render(request, 'main/welcome.html', context)


def students_view(request):
    context = contexts_func(request)
    return render(request, 'main/students.html', context)


def student_view(request, student_id):
    context = contexts_func(request)
    context['student'] = Student.objects.get(id=student_id)
    if request.method == 'POST':
        print(request.POST.get('student'))
        print(request.POST.get('station'))
    return render(request, 'main/student.html', context)


def groups_view(request):
    context = contexts_func(request)
    context['groups'] = Group.objects.all()
    return render(request, 'main/groups.html', context)


def group_view(request, pk):
    context = contexts_func(request)
    context['group'] = Group.objects.get(pk=pk)
    return render(request, 'main/group.html', context)


def titles_view(request):
    titles = Title.objects.all()
    stations = Station.objects.all()
    context = {
        'titles': titles,
        'stations': stations
    }
    return render(request, 'main/titles.html', context)


def station_view(request, pk):
    context = contexts_func(request)
    context['station'] = Station.objects.get(pk=pk)
    return render(request, 'main/station.html', context)


def exams_view(request):
    context = contexts_func(request)
    student = Student.objects.get(id=request.POST.get('student'))
    station = Station.objects.get(id=request.POST.get('station'))
    context['student'] = student
    context['station'] = station
    print(context['student'])
    print(context['station'])
    return render(request, 'main/exam.html', context)


def pass_exams_view(request, student_pk, station_pk):
    if request.method == 'POST':
        pass

    return render(request, 'main/exam.html', {'student_pk': student_pk, 'station_pk': station_pk, 'list_s': range(1, 6)})


def check_exam(request):
    context = contexts_func(request)
    station = Station.objects.get(id=request.POST.get('station'))
    student = Student.objects.get(id=request.POST.get('student'))
    if request.method == 'POST':
        k = 0
        for title in station.titles.all():
            result = Result.objects.create(title=title, student=student, station=station)
            if request.POST.get(str(title.id)) == 'on':
                k += 1
                result.result = True
            else:
                result.result = False
            result.save()
        general = General.objects.get(student=student)
        if general is not None:
            print("Topshirmagan")
        else:
            print("Topshirgan")
        print(k/station.titles.all().count() * 100)

    return render(request, 'main/exam.html', context)


