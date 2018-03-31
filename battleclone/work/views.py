from django.views.generic import FormView, DetailView
from django.contrib.auth.decorators import login_required
from .forms import WorkModelForm
from battleclone.account.models import UserProfile
from .models import Work
from .managers.work_manager import WorkManager


class WorkView(FormView):
    template_name = 'work/work_view.html'
    success_url = '/work'
    form_class = WorkModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        try:
            context['work'] = Work.objects_utils.work_latest(user)
        except Work.DoesNotExist as e:
            print('Work object does not exists', e)

        return context

    def post(self, request, *args, **kwargs):
        form = WorkModelForm(request.POST)
        if form.is_valid():
            character = UserProfile.objects.get(user=self.request.user).character

            instance = form.save(commit=False)
            instance.character = character
            instance.save()

            character.update_status('WORK')

        return super().post(request, *args, **kwargs)


@login_required
def finish_work(request):
    character = UserProfile.objects.get(user=request.user).character
    character.update_status('FREE')

    work_object = Work.objects.filter(character=character).latest('started')
    work_manager = WorkManager(work_object)

    reward = work_manager.get_reward()
    print('reward', reward)

    character.update_money(reward)

    return WorkView.as_view()(request)


@login_required
def stop_work(request):
    pass





# TODO: login required
# TODO: work detail view
# TODO: work list view
# TODO: work table?
