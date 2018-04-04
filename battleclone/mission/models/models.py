from django.db import models
from django.utils.translation import gettext as _
from battleclone.character.models import Character
from django.utils import timezone

# Create your models here.
# TODO: CHECK MIGRATIONS!!!!!!!!!!!!! COULD CAUSE PROBLEMS


class MissionModel(models.Model):
    character = models.ForeignKey(
        to=Character, on_delete=models.CASCADE,
        verbose_name=_("Character"),
        help_text=_("Character assigned to mission"),
    )

    started = models.DateTimeField(
        verbose_name=_('Started datetime'),
        help_text=_('Time when mission started'),
        auto_now=True
    )

    mission_type = models.IntegerField(
        verbose_name=_('Mission type'),
        help_text=_('Mission type'),
        default=1
    )
