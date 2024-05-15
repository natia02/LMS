from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    subject = models.ForeignKey(to='university.Subject', on_delete=models.CASCADE, verbose_name=_("Subject"))
    description = models.TextField(verbose_name=_("Description"))
    due_date = models.DateField(verbose_name=_("Due Date"))

    def __str__(self):
        return f"{self.subject.title} - Due: {self.due_date}"

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
