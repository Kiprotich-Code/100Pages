# Generated by Django 4.2.4 on 2023-12-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_stage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
