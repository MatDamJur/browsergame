from battleclone.account.models import UserProfile


def get_user_profile(request):
    return {'user_profile': UserProfile.objects.get(user=request.user)}
