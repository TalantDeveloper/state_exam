from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),

    path('students/', views.students_view, name='students'),
    path('students/<int:student_id>/', views.student_view, name='student'),

    path('titles/', views.titles_view, name='titles'),
    path('station/<int:pk>/', views.station_view, name='station'),

    path('groups/', views.groups_view, name='groups'),
    path('group/<int:pk>/', views.group_view, name='group'),

    path('exam/', views.exams_view, name='exam'),
    path('check/', views.check_exam, name='check'),

    path('test/<int:student_id>/', views.test_result, name='test'),
    path('tests/', views.tests_view, name='tests')

]
