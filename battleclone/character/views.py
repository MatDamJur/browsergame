from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .models import Parameters


def placeholder_func(attr):
    character_parameters  = Parameters.objects.get(id=1)
    if attr == 'strength':
        character_parameters.strength += 1
        character_parameters.save()

    elif attr == 'agility':
        print('agility')
        character_parameters.agility += 1
        character_parameters.save()

    elif attr == 'defense':
        print('defense')
        character_parameters.defense += 1
        character_parameters.save()

    elif attr == 'durability':
        print('durability')
        character_parameters.durability += 1
        character_parameters.save()

    elif attr == 'luck':
        print('luck')

        character_parameters.luck += 1
        character_parameters.save()


class CharacterView(TemplateView):
    template_name = "character.html"

    def get(self, request, attr=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if attr:
            placeholder_func(attr)
            return redirect('character:CharacterView')

        context['character_attributes'] = Parameters.objects.get(id=1)
        return super(TemplateView, self).render_to_response(context)