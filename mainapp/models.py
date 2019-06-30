from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone

from djongo import models as model
from django.db import models


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    money = models.IntegerField(default=0, verbose_name="Баланс")


class Question(model.Model):
    q=model.TextField(max_length=10000)
    q_id=model.CharField(max_length=10)
    text_id = model.CharField(max_length=30, blank=True, null=True)
    chosen_ans = model.CharField(max_length=10,blank=True, null=True)
    a=model.CharField(max_length=1000)
    b = model.CharField(max_length=1000)
    c=model.CharField(max_length=1000)
    d=model.CharField(max_length=1000)
    e=model.CharField(max_length=1000)
    topic_id = model.CharField(max_length=30)
    topic_name = model.CharField(max_length=200)
    topic_video_link = model.CharField(max_length=100)
    year = model.CharField(max_length=10)
    weight = model.CharField(max_length=10)

    def __str__(self):
        return self.q_id


class Question2(model.Model):
    q=model.TextField(max_length=10000)
    q_id=model.CharField(max_length=10)
    chosen_ans = model.CharField(max_length=10,blank=True, null=True)
    right_ans_nums = model.CharField(max_length=10)
    a=model.CharField(max_length=1000)
    b = model.CharField(max_length=1000)
    c=model.CharField(max_length=1000)
    d=model.CharField(max_length=1000)
    e=model.CharField(max_length=1000)
    f = model.CharField(max_length=1000)
    g = model.CharField(max_length=1000)
    h = model.CharField(max_length=1000)
    topic_id = model.CharField(max_length=30)
    topic_name = model.CharField(max_length=200)
    topic_video_link = model.CharField(max_length=100)
    year = model.CharField(max_length=10)
    weight = model.CharField(max_length=10)

    def __str__(self):
        return self.q_id


class Text(model.Model):
    text = model.TextField()
    text_id = model.CharField(max_length=10)
    question_number = model.CharField(max_length=10)


class Subject(model.Model):
    subject_name = model.CharField(max_length=100)
    questions = model.ArrayModelField(model_container=Question)


class SubjectWithTexts(model.Model):
    subject_name = model.CharField(max_length=100)
    texts = model.ArrayModelField(model_container=Text)
    questions = model.ArrayModelField(model_container=Question)


class SubjectWithEightAnswer(model.Model):
    subject_name = model.CharField(max_length=200)
    questions1_20 = model.ArrayModelField(model_container=Question)
    questions21_30 = model.ArrayModelField(model_container=Question2)


class Testt(model.Model):
    _id = model.ObjectIdField(default='5c4827ae923dac16a72a9d61')
    num_id = model.IntegerField(default="1")
    lang_id = model.IntegerField(default="1")
    lang_name = model.CharField(max_length=200, default="")
    cost = model.IntegerField(default=200)
    subject_1 = model.EmbeddedModelField(model_container=Subject)
    subject_2 = model.EmbeddedModelField(model_container=SubjectWithTexts)
    subject_3 = model.EmbeddedModelField(model_container=Subject)
    subject_12 = model.EmbeddedModelField(model_container=SubjectWithEightAnswer)
    subject_13 = model.EmbeddedModelField(model_container=SubjectWithEightAnswer)


class Test(model.Model):
    name = model.CharField(max_length=50, verbose_name="Название", default='SOME STRING')
    variant = model.IntegerField(verbose_name="Вариант", default=1)
    price = model.IntegerField(verbose_name="Цена", default=1)


class PassedTest(model.Model):
    test = model.EmbeddedModelField(model_container=Testt)
    date = model.DateTimeField()


class History(model.Model):
    user_id = model.ForeignKey(User, on_delete=model.CASCADE,null=False)
    ptest = model.ArrayModelField(model_container=PassedTest)

