# Generated by Django 5.0 on 2023-12-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_task_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
    ]
