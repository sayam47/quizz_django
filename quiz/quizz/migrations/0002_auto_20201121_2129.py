# Generated by Django 2.1.15 on 2020-11-21 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
