from django.utils.translation import ugettext, ugettext_lazy as _
from rest_framework import serializers

from core.models.mixins import ContentMixin
from .lesson import LessonSerializer


class Discipleship(ContentMixin):
    class Meta:
        verbose_name = _('Discipulado')
        verbose_name_plural = _('Discipulados')
        permissions = (
            ('read_discipleship', 'Can read ' + ugettext('Discipulado')),
        )


# Serialization
class DiscipleshipSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Discipleship
        fields = '__all__'
