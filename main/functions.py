from .models import Student, Group, Title, Station, General, ResultTest, Result, Exam


def contexts_func(request):
    stations = Station.objects.all()
    groups = Group.objects.all()
    generals = General.objects.all()
    students = Student.objects.all()
    # hour_pirsent = [student for student in generals if student.exam.result == 100.0]
    # eyti_pirsent = [student for student in generals if student.exam.result > 85 and student.exam.result < 100.0]
    # six_pirsent = [student for student in generals if student.exam.result > 60 and student.exam.result < 85.1]
    # pass_pirsent = [student for student in generals if student.exam.result < 60.0]
    context = {
        'stations': stations,
        'groups': groups,
        'generals': generals,
        'students': students,
        # 'hour_pirsent': hour_pirsent,
        # 'eyti_pirsent': eyti_pirsent,
        # 'six_pirsent': six_pirsent,
        # 'pass_pirsent': pass_pirsent,
    }
    return context


def get_group(student):
    groups = Group.objects.all()
    for group in groups:
        if student in group.students.all():
            return group
    return None


def get_result_test(student):
    result_tests = ResultTest.objects.all()
    for result in result_tests:
        if result.student.id == student.id:
            return result
    return None


def get_exam(student):
    results = Exam.objects.all()
    for result in results:
        if result.student.id == student.id:
            return result
    return None


def get_general(student):
    generals = General.objects.all()
    for general in generals:
        if general.student.id == student.id:
            return general
    return None


def get_student_info(request, student):
    group = get_group(student)
    result_test = get_result_test(student)
    result_exam = get_exam(student)
    general = get_general(student)
    stations = Station.objects.all()
    context = {
        'student': student,
        'group': group,
        'result_test': result_test,
        'result_exam': result_exam,
        'general': general,
        'stations': stations,
    }
    return context
