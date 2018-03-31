from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from .forms import WorkModelForm
from battleclone.account.models import UserProfile
from .models import Work
from .managers.work_manager import WorkManager

# TODO: TESTS TEsts tesTSTSTSTS
def get_character(user):
    return UserProfile.objects.get(user=user).character


class WorkView(FormView):
    template_name = 'work/work_view.html'
    success_url = '/work'
    form_class = WorkModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['work'] = Work.objects_utils.latest_by_user(self.request.user)
        except Work.DoesNotExist as e:
            # TODO: ADD LOGGING
            print('Work object does not exists', e)

        return context

    def post(self, request, *args, **kwargs):
        form = WorkModelForm(request.POST)
        if form.is_valid():
            character = get_character(self.request.user)

            instance = form.save(commit=False)
            instance.character = character
            instance.save()

            character.update_status('WORK')

        return super().post(request, *args, **kwargs)


@login_required
def finish_work(request):
    character = get_character(request.user)
    character.update_status('FREE')

    # TODO: character.update_work() AND TESTS
    work_object = Work.objects_utils.latest_by_character(character)
    work_manager = WorkManager(work_object)

    reward = work_manager.get_reward()

    character.update_money(reward.money)

    return WorkView.as_view()(request)


@login_required
def stop_work(request):
    get_character(request.user).update_status('FREE')
    return WorkView.as_view()(request)
