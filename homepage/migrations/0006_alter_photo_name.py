# Generated by Django 3.2.7 on 2021-09-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20210909_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
