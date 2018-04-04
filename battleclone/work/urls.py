from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^work/', views.WorkView.as_view(), name='work'),
    url(r'work_finish/', views.finish_work, name='finish_work'),
    url(r'work_stop/', views.stop_work, name='stop_work'),
]