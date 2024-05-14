from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    name = models.CharField(max_length=100, verbose_name=_('First Name'))
    surname = models.CharField(max_length=100, verbose_name=_('Last Name'))
    email = models.EmailField(verbose_name=_('Email'), unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professors')
