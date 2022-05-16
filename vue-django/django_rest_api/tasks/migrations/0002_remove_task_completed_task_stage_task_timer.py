# Generated by Django 4.0.4 on 2022-05-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='stage',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='timer',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
