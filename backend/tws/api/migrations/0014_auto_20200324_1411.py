# Generated by Django 3.0.3 on 2020-03-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200324_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='accountType',
            field=models.CharField(choices=[('private', 'private'), ('public', 'public')], default='private', max_length=10),
        ),
    ]
