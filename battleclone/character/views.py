from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Parameters


def placeholder_func(attr):
    if attr == 'strength':
        print('strength')
    elif attr == 'agility':
        print('agility')
    elif attr == 'defense':
        print('defense')
    elif attr == 'durability':
        print('durability')
    elif attr == 'luck':
        print('luck')


class CharacterView(TemplateView):
    template_name = "character.html"

    def get(self, request,attr=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if attr:
            placeholder_func(attr)
        context['character_attributes'] = Parameters.objects.get(id=1)
        return super(TemplateView, self).render_to_response(context)