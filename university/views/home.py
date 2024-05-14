from django.core.paginator import Paginator
from django.shortcuts import render

from university.models import Faculty


def home(request):
    faculties = Faculty.objects.all().order_by('name')
    paginator = Paginator(faculties, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'other/faculty_list.html', {'faculties': page_obj})

