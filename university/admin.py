from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from university.models import Professor, Subject, Student, Faculty


class ProfessorInline(admin.StackedInline):
    model = Professor
    can_delete = False
    verbose_name_plural = 'professors'


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'students'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfessorInline, StudentInline)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email']
    search_fields = ['name', 'surname']
    list_filter = ['name', 'surname']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'faculty']
    search_fields = ['name', 'surname', 'faculty']
    list_filter = ['name', 'surname', 'faculty']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
    search_fields = ['title']
    list_filter = ['title']
