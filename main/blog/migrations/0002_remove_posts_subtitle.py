# Generated by Django 4.2.13 on 2024-06-09 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='subtitle',
        ),
    ]