# from django.db import models
from mongoengine import *
from mongdo_lab.settings import MONGODB_NAME
import datetime

connect(MONGODB_NAME)
# Create your models here.


class LabUser(DynamicDocument):
    uid = IntField(required=True)
    username = StringField(min_length=6, max_length=30, required=True)
    # password = StringField(min_length=6, max_length=30, required=True)
    wechat = StringField(max_length=30, required=True)
    staff = BooleanField(required=True, default=False)
    join_time = DateTimeField(default=datetime.datetime.now)

    meta = {
        'indexes': ['join_time', '$username']
    }


class UserInfo(DynamicDocument):
    GENDER_CHOICES = (
        ('S', '保密'),
        ('M', '男'),
        ('F', '女'),
    )
    AGE_CHOICES = (
        ('S', '保密'),    # Secret
        ('C', '童年'),    # Childhood
        ('J', '少年'),    # Juvenile
        ('P', '青年'),    # Puberty
        ('P', '壮年'),    # Prime of life
        ('M', '中年'),    # Middle-aged
        ('O', '老年'),    # Old Age
    )
    age = StringField(max_length=2, default='S', choices=AGE_CHOICES)
    gender = StringField(max_length=2, default='S', choices=GENDER_CHOICES)
