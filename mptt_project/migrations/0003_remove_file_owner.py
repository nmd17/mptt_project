# Generated by Django 2.2.5 on 2019-09-27 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mptt_project', '0002_file_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
    ]