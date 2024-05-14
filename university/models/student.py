from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'))
    faculty = models.ForeignKey(
        to='Faculty',
        on_delete=models.CASCADE,
        verbose_name=_("Faculty"))
    subjects = models.ManyToManyField(
        to='Subject',
        related_name="subjects",
        verbose_name=_("Subjects"),
        blank=True)
    professors = models.ManyToManyField(
        to='Professor',
        related_name="professors",
        verbose_name=_("Professors"))
    name = models.CharField(max_length=100, verbose_name=_("First Name"))
    surname = models.CharField(max_length=100, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
