from django.conf.urls import url, include
from labcrm import views

urlpatterns = [
    url(r'^users', views.user_list, name='list'),
    url(r'^detail', views.user_detail, name='detail'),
    url(r'^conf', views.ques_conf, name='conf'),
    url(r'^fill', views.ques_fill, name='fill'),
]
