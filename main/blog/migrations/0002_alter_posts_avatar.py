# Generated by Django 4.2.13 on 2024-06-09 12:56

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='avatar',
            field=models.ImageField(default='default.jpeg', upload_to=blog.models.user_directory_path),
        ),
    ]