from django.urls import path
from django.contrib.auth import views as auth_views

from university import views
from university.views import (get_faculty, get_lecturers,
                              get_lecturer, get_subjects,
                              get_subject, student_subjects,
                              create_task, list_tasks, edit_task)

urlpatterns = [
    path('', views.home, name='home'),
    path('faculty/<int:faculty_id>/', get_faculty, name='faculty'),
    path('tasks/create/', create_task, name='create-task'),
    path('lecturer/<int:lecturer_id>', get_lecturer, name='lecturer'),
    path('lecturers/', get_lecturers, name='lecturers'),
    path('subjects/', get_subjects, name='subjects'),
    path('tasks/', list_tasks, name='list_tasks'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('student/subjects/', student_subjects, name='student_subject'),
    path('subject/<int:subject_id>', get_subject, name='subject'),
    path('login/', auth_views.LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='other/faculty_list.html'), name='logout'),
]
