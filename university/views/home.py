from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from university.models import Faculty


def home(request):
    faculties = Faculty.objects.all().order_by('name')
    paginator = Paginator(faculties, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'other/faculty_list.html', {'faculties': page_obj})


def get_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    subjects = faculty.subjects.all()
    professors = set()
    for subject in subjects:
        lecturers_set = subject.professors.all()
        professors.update(lecturers_set)
    return render(request, 'other/faculty_detail.html',
                  {'faculty': faculty, 'subjects': subjects, 'lecturers': professors})
