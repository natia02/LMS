from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from university.models import Subject


def get_subjects(request):
    subjects = Subject.objects.all().order_by('title')
    paginator = Paginator(subjects, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'other/subject_list.html', {'subjects': page_obj})


def get_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    faculties = subject.faculty.all()
    lecturers = subject.professors.all()
    return render(request, 'other/subject_detail.html',
                  {'lecturers': lecturers, 'faculties': faculties, 'subject': subject})