from django.contrib.auth.models import User
from .models import Student, Professor


def user_roles(request):
    context = {}
    if request.user.is_authenticated:
        try:
            context['is_student'] = hasattr(request.user, 'student')
        except Student.DoesNotExist:
            context['is_student'] = False

        try:
            context['is_professor'] = hasattr(request.user, 'professor')
        except Professor.DoesNotExist:
            context['is_professor'] = False

    return context
