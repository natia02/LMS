from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from university.models import Professor, Task
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from university.forms import TaskForm


def get_lecturers(request):
    professors = Professor.objects.all().order_by('name')
    paginator = Paginator(professors, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'other/professor_list.html', {'lecturers': page_obj})


def get_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Professor, pk=lecturer_id)
    subjects = lecturer.subjects.all()
    faculties = set()
    for subject in subjects:
        faculties.update(subject.faculty.all())
    return render(request, 'other/professor_detail.html',
                  {'lecturer': lecturer, 'faculties': faculties, 'subjects': subjects})


@login_required
def create_task(request):
    if hasattr(request.user, 'professor'):
        professor = request.user.professor
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                if task.subject in professor.subjects.all():
                    task.save()
                    return redirect('home')
        else:
            form = TaskForm()
            form.fields['subject'].queryset = professor.subjects.all()
        return render(request, 'other/create_task.html', {'form': form})
    else:
        return redirect('login')


@login_required
def list_tasks(request):
    if hasattr(request.user, 'professor'):
        professor = request.user.professor
        subjects = professor.subjects.all()
        tasks = Task.objects.filter(subject__in=subjects)
        return render(request, 'other/task_list.html', {'tasks': tasks})
    else:
        return redirect('login')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'other/task_edit.html', {'form': form})

