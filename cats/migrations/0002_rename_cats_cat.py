# Generated by Django 4.1.2 on 2022-10-12 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cats',
            new_name='Cat',
        ),
    ]