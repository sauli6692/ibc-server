from rest_framework import viewsets

from pmm.models import Lesson, LessonSerializer
from core.views.mixins import CreateListMixin


class LessonViewSet(CreateListMixin, viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_fields = ('name', 'discipleship__name', 'discipleship__description',)
    search_fields = ('name', 'discipleship__name', 'discipleship__description',)
