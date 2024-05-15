from django import forms
from university.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['subject', 'description', 'due_date']
