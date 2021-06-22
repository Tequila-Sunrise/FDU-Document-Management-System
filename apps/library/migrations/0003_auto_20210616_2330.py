# Generated by Django 3.2.1 on 2021-06-16 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_paper_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='download_link',
            field=models.URLField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
