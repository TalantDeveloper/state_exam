from .models import Student, Group, Title, Station, General


def contexts_func(request):
    stations = Station.objects.all()
    groups = Group.objects.all()
    generals = General.objects.all()
    students = Student.objects.all()
    hour_pirsent = [student for student in generals if student.exam.result == 100.0]
    eyti_pirsent = [student for student in generals if student.exam.result > 85 and student.exam.result < 100.0]
    six_pirsent = [student for student in generals if student.exam.result > 60 and student.exam.result < 85.1]
    context = {
        'stations': stations,
        'groups': groups,
        'generals': generals,
        'students': students,
        'hour_pirsent': hour_pirsent,
        'eyti_pirsent': eyti_pirsent,
        'six_pirsent': six_pirsent,
    }
    return context

