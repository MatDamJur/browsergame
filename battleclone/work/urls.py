from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^work/', views.WorkView.as_view(), name='work'),
    url(r'work_finish/', views.finish_work, name='finish_work'),
]