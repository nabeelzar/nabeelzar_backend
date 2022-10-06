# Generated by Django 4.1.1 on 2022-10-06 04:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_projectimages_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_started',
            field=models.DateField(default=datetime.date(2022, 10, 6)),
        ),
        migrations.AlterField(
            model_name='projectimages',
            name='img_path',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='img_path',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]