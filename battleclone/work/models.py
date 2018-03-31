from django.db import models
from django.utils.translation import gettext as _
from battleclone.character.models import Character
from django.utils import timezone


HOURS = [(hour, '{} hours'.format(hour)) for hour in range(1, 25)]


class WorkManager(models.Manager):
    def latest_by_user(self, user):
        return super().get_queryset().filter(
            character__userprofile__user=user
        ).latest('started')

    def latest_by_character(self, character):
        return super().get_queryset().filter(character=character).latest('started')


class Work(models.Model):
    character = models.ForeignKey(
        verbose_name=_('Character mission'),
        help_text=_('Mission belongs to character'),
        to=Character,
        on_delete=models.CASCADE
    )

    work_type = models.IntegerField(
        verbose_name=_('Mission type'),
        help_text=_('Mission type'),
        choices=HOURS,
        default=1,
        max_length=20
    )

    reward = models.IntegerField(
        verbose_name=_('Reward'),
        help_text=_('Reward for work'),
        null=True, blank=True
    )

    started = models.DateTimeField(
        verbose_name=_('Started time'),
        help_text=_('Started time'),
        default=timezone.now
    )

    objects = models.Manager()
    objects_utils = WorkManager()

    def __str__(self):
        return self.character.nickname
