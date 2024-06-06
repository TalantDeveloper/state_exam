from django.contrib import admin
from .models import Student, Group, Title, Station, Exam, ResultTest, General


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'title')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'title')
    list_per_page = 20


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_students')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_per_page = 20


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_titles')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_per_page = 20


class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'station', 'result')
    list_display_links = ('id', 'student', 'group', 'station', 'result')
    search_fields = ('student', 'group', 'station', 'result')
    list_per_page = 20


class ResultTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'result')
    list_display_links = ('id', 'student', 'group', 'result')
    search_fields = ('student', 'group', 'result')
    list_per_page = 20


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'result_test', 'exam', 'result_sum')
    list_display_links = ('id', 'student', 'group', 'result_test', 'exam', 'result_sum')
    search_fields = ('student', 'group', 'result_test', 'exam', 'result_sum')
    list_per_page = 20


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(ResultTest, ResultTestAdmin)
admin.site.register(General, GeneralAdmin)



