# Generated by Django 3.2.7 on 2021-09-09 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_photo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='file_url',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
    ]