# Generated by Django 4.1.2 on 2022-10-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_rename_cats_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='source_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
