# Generated by Django 3.0.2 on 2020-03-23 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200319_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupWorkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=360)),
                ('weight', models.FloatField(default=0)),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]
