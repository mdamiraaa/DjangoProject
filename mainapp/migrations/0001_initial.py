# Generated by Django 2.1.7 on 2019-04-04 17:45

from django.conf import settings
from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0, verbose_name='Баланс')),
                ('user', models.ForeignKey(on_delete=models.SET(mainapp.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Testt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_id', models.IntegerField(default='1')),
            ],
        ),
    ]
