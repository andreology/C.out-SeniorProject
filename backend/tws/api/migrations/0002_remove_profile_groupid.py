# Generated by Django 3.0.3 on 2020-03-30 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='groupID',
        ),
    ]
