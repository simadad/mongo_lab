from django.shortcuts import render
from django.http import HttpResponse
from .models import LabUser, UserInfo
# Create your views here.


def user_list(request):
    return render(request, 'labcrm/user_list.html')


def user_detail(request):
    return render(request, 'labcrm/user_detail.html')


def ques_conf(request):
    return render(request, 'labcrm/ques_conf.html')


def ques_fill(request):
    return render(request, 'labcrm/ques_fill.html')
