from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Parameters(models.Model):
    """ Character parameters:
    strength, agility, luck etc

    """
    strength = models.PositiveIntegerField(
        verbose_name=_("Strength"),
        help_text=_("Character's stregnth"),
        default=1,
        validators=[MinValueValidator(1)]
    )

    agility = models.PositiveIntegerField(
        verbose_name=_("Agility"),
        help_text=_("Character's agility"),
        default=1,
        validators=[MinValueValidator(1)]
    )

    defense = models.PositiveIntegerField(
        verbose_name=_("Defense"),
        help_text=_("Character's defense"),
        default=1,
        validators=[MinValueValidator(1)]
    )

    durability = models.PositiveIntegerField(
        verbose_name=_("Durability"),
        help_text=_("Character's durability"),
        default=1,
        validators=[MinValueValidator(1)]
    )

    luck = models.PositiveIntegerField(
        verbose_name=_("Luck"),
        help_text=_("Character's Luck"),
        default=1,
        validators=[MinValueValidator(1)]
    )

    # TODO: what more?

    def __str__(self):
        return 'Str: {}, Agi: {}, Def: {}, Dur: {}, Luck:{}'.format(
            self.strength, self.agility, self.defense, self.durability, self.luck
        )


class Character(models.Model):
    nickname = models.CharField(
        verbose_name=_('Nickname'),
        help_text=_("Character's nickname"),
        max_length=30,
    )

    level = models.PositiveSmallIntegerField(
        verbose_name=_("Level"),
        help_text=_("Character's actual level"),
        default=1,
        validators=[MinValueValidator(1)]
    )

    experience_points = models.IntegerField(
        verbose_name=_("Experience points"),
        help_text=_('Actual experience points'),
        default=1,
        validators=[MinValueValidator(1)]
    )

    health = models.PositiveSmallIntegerField(
        verbose_name=_("Health"),
        help_text=_("Actual character'health value"),
        default=100,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    action_points = models.PositiveSmallIntegerField(
        verbose_name=_('Action points'),
        help_text=_('Avaiable points to be used in mission etc.'),
        default=1000,
        validators=[MaxValueValidator(1000), MinValueValidator(0)]
    )

    parameters = models.OneToOneField(
        to=Parameters,
        on_delete=models.CASCADE,
        verbose_name=_('Parameters'),
        help_text=_("Character's parameters"),
    )

    on_mission = models.BooleanField(
        verbose_name=_("On Mission flag"),
        help_text=_("Is character on mission flag"),
        default=False
    )

    mission_start_time = models.DateTimeField(
        verbose_name=_("Mission start time"),
        help_text=_("Mission start time"),
        blank=True, null=True
    )

    at_work = models.BooleanField(
        verbose_name=_("At work flag"),
        help_text=_("Is character on work flag"),
        default=False
    )

    work_start_time = models.DateTimeField(
        verbose_name=_("Work start time"),
        help_text=_("Work start time"),
        blank=True, null=True
    )

    def __str__(self):
        return 'id: {}. {} level: {} HP:{} AP:{}'.format(
            self.id, self.nickname, self.level, self.health, self.action_points
        )
