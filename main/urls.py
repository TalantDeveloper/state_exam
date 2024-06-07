from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('titles/', views.titles_view, name='titles'),
    path('station/<int:pk>/', views.station_view, name='station'),
    path('students/', views.student_view, name='students'),

    path('group/<int:pk>/', views.group_view, name='group'),


    path('exam/<int:student_pk>/<int:station_pk>/', views.pass_exams_view, name='exam'),

]
