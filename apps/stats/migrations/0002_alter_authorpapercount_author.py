# Generated by Django 3.2.1 on 2021-06-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorpapercount',
            name='author',
            field=models.CharField(max_length=128),
        ),
    ]
