from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models.custom_fields import FixedCharField


class Person(models.Model):
    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')
    gender_choices = (
        ('M', _('Masculino')),
        ('F', _('Femenino')),
    )
    first_name = models.CharField(_('Nombre'), max_length=50)
    last_name = models.CharField(_('Apellido'), max_length=50)
    birthday = models.DateField(_('Cumpleaños'), null=True)
    new_birthday = models.DateField(_('Nuevo Nacimiento'), null=True)
    gender = FixedCharField(_('Género'), max_length=1, choices=gender_choices, default='M')
    direction_main = models.CharField(_('Dirección principal'), max_length=255, null=True)
    direction_extra = models.CharField(_('Dirección extra'), max_length=255, null=True)
    baptized = models.BooleanField(_('Bautizado'))
    last_visit = models.DateField(_('Ultima Visita'), null=True)
    integration_level = models.ForeignKey(
        'pmm.IntegrationLevel',
        on_delete=models.CASCADE,
        null=True
    )
    occupation = models.ForeignKey(
        'pmm.Occupation',
        on_delete=models.CASCADE,
        null=True
    )
    civil_status = models.ForeignKey(
        'pmm.CivilStatus',
        on_delete=models.CASCADE,
        null=True
    )
    invited_by = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True
    )