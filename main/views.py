from django.shortcuts import render, redirect

from .functions import contexts_func, get_group, get_result_test, get_general, get_student_info
from .models import Student, Group, Title, Station, General, Result, Exam, ResultTest


def welcome_view(request):
    context = contexts_func(request)
    context['talaba'] = Student.objects.all().count()
    return render(request, 'main/welcome.html', context)


def students_view(request):
    """Students of the TSDI"""
    context = contexts_func(request)
    return render(request, 'students/students.html', context)


def student_view(request, student_id):
    """Student view """
    student = Student.objects.get(id=student_id)
    context = get_student_info(request, student)

    return render(request, 'students/student.html', context)


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
    general = get_general(student)
    if general is not None:
        pass
    context['student'] = student
    context['station'] = station
    return render(request, 'main/exam.html', context)


def pass_exams_view(request, student_pk, station_pk):
    if request.method == 'POST':
        pass

    return render(request, 'main/exam.html', {'student_pk': student_pk, 'station_pk': station_pk, 'list_s': range(1, 6)})


def test_result(request, student_id):
    context = contexts_func(request)
    student = Student.objects.get(id=student_id)
    group = get_group(student)
    result_test = get_result_test(student)
    context['student'] = student
    context['group'] = group
    context['result_test'] = result_test
    if request.POST:
        result = float(request.POST.get('result'))
        result_test = ResultTest.objects.create(student=student, group=group, result=result)
        result_test.save()
        return redirect('main:groups')
    return render(request, 'test/test.html', context)


def tests_view(request):
    contexts = contexts_func(request)
    tests = ResultTest.objects.all()
    contexts['result_tests'] = tests
    return render(request, 'test/tests.html', contexts)


def check_exam(request):
    context = contexts_func(request)
    station = Station.objects.get(id=request.POST.get('station'))
    student = Student.objects.get(id=request.POST.get('student'))
    group = get_group(student)
    result_test = get_result_test(student)
    general = get_general(student)

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
        exam = Exam.objects.create(student=student, group=group, station=station, result=float((k/station.titles.all().count())*100))
        exam.save()
        if result_test is None:
            result_test = ResultTest.objects.create(student=student, group=group, result=0.0)
            result_test.save()
        if general is None:
            general = General.objects.create(student=student, group=group, exam=exam, result_test=result_test)
            general.result_sum = exam.result / 2
            general.save()
        return redirect('main:groups')

    return render(request, 'main/exam.html', context)


