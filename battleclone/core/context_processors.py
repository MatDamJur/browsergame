from battleclone.account.models import UserProfile


def get_user_profile(request):
    if request.user.is_authenticated():
        return {'user_profile': UserProfile.objects.get(user=request.user)}

    return {'user_profile': None}
