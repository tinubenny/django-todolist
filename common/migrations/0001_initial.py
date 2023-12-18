# Generated by Django 5.0 on 2023-12-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField(default=0)),
                ('password', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'user_tb',
            },
        ),
    ]
