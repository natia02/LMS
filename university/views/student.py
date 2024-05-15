from django.shortcuts import render, redirect


def student_subjects(request):
    if request.user.is_authenticated and hasattr(request.user, 'student'):
        student = request.user.student
        subjects = student.subjects.all()
        return render(request, 'other/student_subjects.html', {"subjects": subjects})
    else:
        print(request.user.is_authenticated )
        print(hasattr(request.user, 'student'))
        return redirect('login')
