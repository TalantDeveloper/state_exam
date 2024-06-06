from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),

    path('exam/<int:student_pk>/<int:station_pk>/', views.pass_exams_view, name='exam'),

]
