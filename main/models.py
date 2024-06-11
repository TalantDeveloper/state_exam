from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    title = models.CharField(max_length=100, verbose_name="Title", null=True, blank=True)

    def __str__(self):
        return self.full_name


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    students = models.ManyToManyField(Student, verbose_name="Students", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_students(self):
        students = [student.full_name for student in self.students.all()]
        return students


class Title(models.Model):
    title = models.TextField(verbose_name="Title", null=True, blank=True)

    def __str__(self):
        return self.title


class Station(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    titles = models.ManyToManyField(Title, verbose_name="Titles", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_titles(self):
        titles = [tt.title for tt in self.titles.all()]
        return titles


class Result(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE)
    title = models.ForeignKey(Title, verbose_name="Title", on_delete=models.CASCADE)
    station = models.ForeignKey(Station, verbose_name="Station", on_delete=models.CASCADE)
    result = models.BooleanField(verbose_name="Result", default=False)

    def __str__(self):
        return f"{self.title}: {self.station}"


class Exam(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Group", on_delete=models.SET_NULL, null=True, blank=True)
    station = models.ForeignKey(Station, verbose_name="Station", on_delete=models.SET_NULL, null=True, blank=True)
    result = models.FloatField(verbose_name="Result", null=True, blank=True)

    def __str__(self):
        return f"{self.result} %"


class ResultTest(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Group", on_delete=models.SET_NULL, null=True, blank=True)
    result = models.FloatField(verbose_name="Result", null=True, blank=True)

    def __str__(self):
        return f"{self.result} %"


class General(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Group", on_delete=models.SET_NULL, null=True, blank=True)
    result_test = models.ForeignKey(ResultTest, verbose_name="Result", on_delete=models.SET_NULL, null=True, blank=True)
    exam = models.ForeignKey(Exam, verbose_name="Exam", on_delete=models.SET_NULL, null=True, blank=True)
    result_sum = models.FloatField(verbose_name="ResultSum", null=True, blank=True)

    def __str__(self):
        return f"{(self.exam.result + self.result_test.result)/2}"

