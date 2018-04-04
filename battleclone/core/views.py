from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from battleclone.account.models import UserProfile


@login_required
def game(request):
    template_name = 'core/game.html'
    # context = {'object': UserProfile.objects.get(user=request.user)}
    return render(request, template_name, {})
