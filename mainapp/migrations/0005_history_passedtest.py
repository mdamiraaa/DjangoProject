# Generated by Django 2.1.7 on 2019-04-09 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_auto_20190408_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptest', djongo.models.fields.ArrayModelField(model_container=mainapp.models.PassedTest)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PassedTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', djongo.models.fields.EmbeddedModelField(model_container=mainapp.models.Testt, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
